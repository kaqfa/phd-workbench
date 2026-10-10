# Template

Salin template, lalu ganti nama berkas sesuai konvensi di README folder tujuan. Frontmatter wajib dipertahankan karena `scripts/wb.py status` membacanya.

| Template | Fase | Tujuan salin |
|---|---|---|
| `profil-diri.md` | 0 | `01-profil-diri/profil.md` |
| `aset-riset.md` | 0 | `01-profil-diri/aset-riset.md` |
| `kartu-ide.md` | 1 | `02-eksplorasi-topik/kartu-ide/ide-NN-<slug>.md` |
| `matriks-skor.md` | 1 | `02-eksplorasi-topik/matriks-skor.md` |
| `uji-tekan.md` | 1–3 | `02-eksplorasi-topik/uji-tekan/uji-tekan-<slug>.md` |
| `TDR.md` | 1 | `02-eksplorasi-topik/keputusan/TDR-NNN-<slug>.md` |
| `scoping-review.md` | 2 | `04-literatur/scoping/scoping-<slug>.md` |
| `rantai-kontribusi.md` | 2–3 | `03-proposal/rantai-kontribusi.md` |
| `resume-paper.md` | semua | `04-literatur/resume/<bibkey>.md` |
| `protokol-studi.md` | 5 | `05-riset/rqN-<slug>/protokol/protokol.md` |
| `log-harian.md` | semua | `11-jurnal-riset/log/YYYY-MM-DD.md` |
| `bimbingan.md` | semua | `11-jurnal-riset/bimbingan/YYYY-MM-DD-bimbingan.md` |
| `keputusan.md` | semua | `11-jurnal-riset/keputusan/ADR-NNN-<slug>.md` |
| `checklist-submit.md` | 6 | `08-publikasi/paper-N-<slug>/checklist-submit.md` |
| `respons-reviewer.md` | 6 | `08-publikasi/respons-reviewer/<paper>-ronde-N.md` |
| `retrospeksi.md` | per kuartal | `11-jurnal-riset/retrospeksi/YYYY-QN.md` |
| `modul/<nama>/` | — | Modul jenis riset (lihat `workbench.yaml` → `riset.jenis`) |
| `profil-kampus/<kampus>/` | 3, 7 | Ringkasan syarat formal & template naskah kampus |
