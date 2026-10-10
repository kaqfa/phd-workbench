# Board Tugas Agen

Tugas agen yang panjang atau berulang (pencarian literatur, unduh PDF, draf resume massal, skrip analisis)
dicatat sebagai berkas Markdown yang dipindah antar-folder: `todo/` → `doing/` → `review/` → `done/`.

Nama berkas: `YYYY-MM-DD-<slug>.md`. Format:

```markdown
---
peran: pekerja          # pekerja | supervisor
dibuat: YYYY-MM-DD
---
# <judul tugas>

## Goal
## Scope (yang termasuk / tidak termasuk)
## Acceptance Criteria
- [ ]
## Verification Commands
(perintah yang bisa dijalankan ulang untuk mengecek hasil)
## Bukti / hasil
```

Tugas di `review/` diperiksa supervisor (agen atau manusia) sebelum dipindah ke `done/`.
Keputusan riset tidak pernah diambil di board ini.
