#!/usr/bin/env python3
"""PhD-Workbench CLI (stdlib saja).

  python3 scripts/wb.py status              bangkitkan STATUS.md
  python3 scripts/wb.py cek gate G1         butir gate yang belum terpenuhi
  python3 scripts/wb.py cek sitasi [berkas] periksa kunci sitasi di naskah
"""
import argparse
import datetime as dt
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / "04-literatur/bibliografi/references.bib"
RESUME_DIR = ROOT / "04-literatur/resume"
FASE = ["Profiling diri", "Eksplorasi topik", "Validasi celah", "Proposal & seminar",
        "Review sistematis", "Riset per RQ", "Publikasi", "Perakitan disertasi", "Seminar hasil & ujian"]
FASE_GATE = {0: "G0", 1: "G1", 2: "G2", 3: "G3", 5: "G4", 6: "G6", 7: "G7"}
NASKAH_DEFAULT = ["03-proposal/draf", "03-proposal/naskah-resmi", "08-publikasi", "09-disertasi/naskah"]


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def frontmatter(path: Path) -> dict:
    """Parser `key: value` minimal untuk frontmatter YAML datar."""
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"([\w-]+):\s*(.*)", line)
        if kv:
            val = re.sub(r"\s+#.*$", "", kv.group(2)).strip().strip("\"'")
            data[kv.group(1)] = val
    return data


def fase_aktif() -> int:
    cfg = (ROOT / "workbench.yaml").read_text(encoding="utf-8")
    m = re.search(r"^\s*fase_aktif:\s*(\d+)", cfg, re.M)
    return int(m.group(1)) if m else 0


def gate_items(path: Path):
    items = re.findall(r"^\s*- \[([ xX])\] (.+)$", path.read_text(encoding="utf-8"), re.M)
    return [(c.lower() == "x", t.strip()) for c, t in items]


def gate_files(gate: str):
    return sorted((ROOT / "_gate").glob(f"{gate}*.md"))


def parse_bib() -> dict:
    """bibkey -> True bila note memuat VERIFIED (bukan UNVERIFIED)."""
    if not BIB.exists():
        return {}
    entries = {}
    for chunk in re.split(r"\n(?=@)", "\n" + BIB.read_text(encoding="utf-8", errors="replace")):
        m = re.match(r"\s*@\w+\s*\{\s*([^,\s]+)\s*,", chunk)
        if m and not chunk.lstrip().lower().startswith(("@comment", "@string", "@preamble")):
            note = re.search(r"note\s*=\s*[{\"](.*?)[}\"]\s*,?\s*$", chunk, re.I | re.M | re.S)
            entries[m.group(1)] = bool(note and re.search(r"(?<!UN)VERIFIED", note.group(1)))
    return entries


def resumes() -> dict:
    return {p.stem: frontmatter(p) for p in RESUME_DIR.glob("*.md") if p.name != "README.md"}


def docs(folder: str, pattern="*.md"):
    return [p for p in (ROOT / folder).glob(pattern) if p.name != "README.md"]


# ---------------------------------------------------------------- status

def cmd_status(_args):
    today = dt.date.today().isoformat()
    fase = fase_aktif()
    out = [
        "# STATUS",
        "",
        f"> Dibangkitkan oleh `python3 scripts/wb.py status` pada {today}. **Jangan diedit tangan.**",
        "",
        f"**Fase aktif:** {fase} — {FASE[fase] if 0 <= fase < len(FASE) else '?'}",
        "",
        "## Gate",
        "",
        "| Gate | Nama | Terpenuhi |",
        "|---|---|---|",
    ]
    for path in sorted((ROOT / "_gate").glob("G*.md")):
        items = gate_items(path)
        done = sum(c for c, _ in items)
        mark = " ✅" if items and done == len(items) else ""
        out.append(f"| {path.stem} | {frontmatter(path).get('nama', '')} | {done}/{len(items)}{mark} |")

    def tally(title, paths, key):
        c = Counter(frontmatter(p).get(key) or "-" for p in paths)
        summary = ", ".join(f"{k}: {v}" for k, v in sorted(c.items())) or "belum ada"
        out.append(f"- **{title}** ({len(paths)}): {summary}")

    out += ["", "## Ringkasan", ""]
    tally("Kartu ide", docs("02-eksplorasi-topik/kartu-ide"), "status")
    tally("Uji tekan", docs("02-eksplorasi-topik/uji-tekan"), "verdict")
    tally("TDR", docs("02-eksplorasi-topik/keputusan"), "status")
    tally("Scoping", docs("04-literatur/scoping", "scoping-*.md"), "status")
    tally("Resume paper", docs("04-literatur/resume"), "tingkat")
    rq_dirs = [p for p in (ROOT / "05-riset").glob("rq*") if p.is_dir()]
    protokol = [p for d in rq_dirs for p in (d / "protokol").glob("*.md") if p.name != "README.md"]
    out.append(f"- **RQ** ({len(rq_dirs)}): " + (", ".join(d.name for d in sorted(rq_dirs)) or "belum ada"))
    tally("Protokol", protokol, "status")
    papers = [p for p in (ROOT / "08-publikasi").glob("paper-*") if p.is_dir()]
    tally("Paper (checklist-submit)", [p / "checklist-submit.md" for p in papers if (p / "checklist-submit.md").exists()], "status")
    tally("Decision record (ADR)", docs("11-jurnal-riset/keputusan"), "status")

    bib, res = parse_bib(), resumes()
    unverified = sorted(k for k, v in bib.items() if not v)
    no_resume = sorted(k for k in bib if k not in res)
    out += ["", "## Utang sitasi", "",
            f"- Entri bib: {len(bib)} · belum VERIFIED: {len(unverified)} · tanpa resume: {len(no_resume)}"]
    for label, keys in (("Belum VERIFIED", unverified), ("Tanpa resume", no_resume)):
        if keys:
            out.append(f"- {label}: " + ", ".join(f"`{k}`" for k in keys[:15]) + (" …" if len(keys) > 15 else ""))
    cari = sum(p.read_text(encoding="utf-8").count("[CARI:") for p in docs("02-eksplorasi-topik/kartu-ide"))
    out.append(f"- Penanda `[CARI: ...]` di kartu ide: {cari}")

    out += ["", "## Jurnal riset", ""]
    logs = sorted(docs("11-jurnal-riset/log"))
    out.append(f"- Log terakhir: {rel(logs[-1]) if logs else 'belum ada'} (total {len(logs)})")
    open_items = []
    for p in sorted(docs("11-jurnal-riset/bimbingan")):
        for row in re.findall(r"^\|(.+)\|\s*$", p.read_text(encoding="utf-8"), re.M):
            cells = [c.strip() for c in row.split("|")]
            if len(cells) >= 4 and cells[-1].lower() == "belum" and cells[0]:
                open_items.append(f"{cells[0]} (tenggat {cells[2]}, {p.stem[:10]})")
    out.append(f"- Action item bimbingan terbuka: {len(open_items)}")
    out += [f"  - {i}" for i in open_items[:10]]
    retros = sorted(docs("11-jurnal-riset/retrospeksi"))
    out.append(f"- Retrospeksi terakhir: {retros[-1].stem if retros else 'belum ada'}")
    kanban = {s: len(list((ROOT / ".agents/kanban" / s).glob("*.md"))) for s in ("todo", "doing", "review", "done")}
    out.append("- Kanban agen: " + ", ".join(f"{k} {v}" for k, v in kanban.items()))

    (ROOT / "STATUS.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


# ---------------------------------------------------------------- cek gate

def cmd_cek_gate(args):
    gate = args.gate.upper()
    files = gate_files(gate)
    if not files:
        sys.exit(f"Gate {gate} tidak ditemukan di _gate/")
    belum = 0
    for path in files:
        items = gate_items(path)
        todo = [t for c, t in items if not c]
        belum += len(todo)
        print(f"{path.stem}: {len(items) - len(todo)}/{len(items)} terpenuhi")
        for t in todo:
            flag = "  ⚠ " if "BELUM DICEK" in t else "  - "
            print(flag + t)
    sys.exit(1 if belum else 0)


# ---------------------------------------------------------------- cek sitasi

LATEX_CITE = re.compile(r"\\[a-zA-Z]*cite[a-zA-Z]*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}")
PANDOC_BLOCK = re.compile(r"\[([^\[\]]*@[^\[\]]*)\]")
PANDOC_KEY = re.compile(r"(?<![\w.])-?@([\w][\w:.#$%&+?<>~/-]*\w)")


def cite_keys(text: str) -> set:
    keys = {k.strip() for grp in LATEX_CITE.findall(text) for k in grp.split(",") if k.strip()}
    for block in PANDOC_BLOCK.findall(text):
        keys.update(PANDOC_KEY.findall(block))
    return keys


def cmd_cek_sitasi(args):
    targets = [Path(f) for f in args.berkas] or [ROOT / d for d in NASKAH_DEFAULT]
    files = []
    for t in targets:
        t = t if t.is_absolute() else Path.cwd() / t
        if t.is_dir():
            files += [p for p in t.rglob("*") if p.suffix in (".md", ".tex") and p.name != "README.md"]
        elif t.exists():
            files.append(t)
        else:
            print(f"lewati (tidak ada): {t}")
    bib, res = parse_bib(), resumes()
    errors = warnings = 0
    for f in sorted(files):
        text = f.read_text(encoding="utf-8", errors="replace")
        keys = cite_keys(text)
        problems = []
        for k in sorted(keys):
            if k not in bib:
                problems.append(("GALAT", k, "tidak ada di references.bib"))
            elif not bib[k]:
                problems.append(("GALAT", k, "note belum VERIFIED"))
            if k not in res:
                problems.append(("GALAT", k, "tidak ada resume di 04-literatur/resume/"))
            elif res[k].get("tingkat") == "cepat":
                problems.append(("PERINGATAN", k, "resume tingkat `cepat` — jangan dipakai untuk klaim substantif"))
        for marker in ("[CARI:", "DRAF-AGEN", "[TODO"):
            if (n := text.count(marker)):
                problems.append(("PERINGATAN", marker, f"{n} penanda tersisa"))
        if keys or problems:
            print(f"\n{rel(f) if f.is_relative_to(ROOT) else f} — {len(keys)} kunci sitasi")
        for level, k, msg in problems:
            print(f"  [{level}] {k}: {msg}")
            errors += level == "GALAT"
            warnings += level == "PERINGATAN"
    print(f"\n{len(files)} berkas diperiksa · {errors} galat · {warnings} peringatan")
    print("Catatan: hanya memeriksa keberadaan & status, bukan kebenaran isi klaim.")
    sys.exit(1 if errors else 0)


def main():
    ap = argparse.ArgumentParser(prog="wb", description="PhD-Workbench CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="bangkitkan STATUS.md").set_defaults(fn=cmd_status)
    cek = sub.add_parser("cek", help="pemeriksaan").add_subparsers(dest="jenis", required=True)
    g = cek.add_parser("gate", help="butir gate yang belum terpenuhi")
    g.add_argument("gate", help="G0..G7")
    g.set_defaults(fn=cmd_cek_gate)
    s = cek.add_parser("sitasi", help="periksa kunci sitasi di naskah")
    s.add_argument("berkas", nargs="*", help="berkas/folder; default: folder naskah standar")
    s.set_defaults(fn=cmd_cek_sitasi)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
