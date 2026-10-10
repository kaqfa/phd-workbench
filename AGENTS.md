# AGENTS.md — Untuk Agen Selain Claude Code

Berkas ini untuk agen AI generik (Codex CLI, Gemini CLI, Cursor, dan sejenisnya). Isinya sama dengan
yang dipakai Claude Code, hanya dirujuk dari sini supaya tidak terjadi duplikasi.

1. **Aturan mengikat:** [`ATURAN.md`](ATURAN.md).
2. **Konteks, protokol awal sesi, dan peran:** [`CLAUDE.md`](CLAUDE.md). Seluruh isinya berlaku
   untukmu, kecuali penyebutan "skill" yang perlu dibaca sebagai berikut.
3. **Prosedur percakapan (skill):** setiap prosedur ada di `.claude/skills/<nama>/SKILL.md`. Bila
   agenmu tidak mendukung skill, buka berkas tersebut dan ikuti langkah-langkahnya secara manual.
   Contohnya, ketika pengguna berkata "kita lanjutkan", baca dan jalankan
   `.claude/skills/lanjut/SKILL.md`.
4. **Konfigurasi proyek:** `workbench.yaml`.
5. **Status:** jalankan `python3 scripts/wb.py status`. Jangan mengedit `STATUS.md` secara langsung.

Aturan tambahan khusus agen ini: tidak ada. Bila suatu saat perlu ditambahkan, tulis di bawah dan
pastikan tidak bertentangan dengan `ATURAN.md`.
