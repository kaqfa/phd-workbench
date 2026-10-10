# Modul: data-sensitif

**Untuk:** data institusi, pasien, siswa, karyawan, atau data pribadi apa pun.

**Struktur:** `06-subjek-data/`
- `sensitif/`: data asli. **Di-ignore Git** dan tidak pernah dibaca agen
- `teranonimisasi/`: hasil anonimisasi dengan skrip yang tercatat (tetap diperlakukan hati-hati)
- `sintetis/`: data tiruan untuk pengembangan dan demo

**Aturan tambahan:**
- Tambahkan path di atas ke `data.folder_sensitif` di `workbench.yaml`.
- `data.boleh_ke_model_tertutup` tetap `false` kecuali ada izin tertulis dari pemilik data (simpan di `00-admin/izin-etik/`).
- Sebelum commit: periksa `git status`; pastikan tidak ada `.csv`/`.sql`/`.xlsx` dari folder sensitif yang ter-*staged*.
- Hasil hanya keluar dalam bentuk agregat (ATURAN §2.4).
