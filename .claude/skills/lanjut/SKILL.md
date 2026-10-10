---
name: lanjut
description: Melanjutkan pekerjaan S3 dan menentukan langkah berikutnya. Pakai ketika pengguna berkata "kita lanjutkan", "apa lagi yang perlu dikerjakan", "sampai mana kita", "aku harus ngapain sekarang", atau membuka sesi baru tanpa permintaan spesifik.
---

# Lanjut — orientasi sesi & langkah berikutnya

## Langkah

1. **Baca konteks** (jangan tampilkan semuanya ke pengguna):
   - `workbench.yaml` → `proyek.fase_aktif`, `proyek.pemilik`, `riset.topik`, `pembaca`, `data`.
   - Bila `proyek.pemilik` kosong **dan** `01-profil-diri/profil.md` belum ada → pengguna baru. Hentikan skill ini, sambut pengguna, dan tawarkan skill `profil`.
   - Jalankan `python3 scripts/wb.py status`, lalu baca `STATUS.md`.
   - Baca 1–2 log terakhir di `11-jurnal-riset/log/` (bagian "Berikutnya" dan "Buntu").
   - Baca bimbingan terakhir di `11-jurnal-riset/bimbingan/`, khususnya action item yang statusnya `belum` dan tenggatnya.
   - Jalankan `python3 scripts/wb.py cek gate G<fase_aktif>` (untuk fase 4 dan 8, lewati langkah ini).
   - Periksa `.agents/kanban/doing/` dan `review/`.

2. **Cek pemicu khusus** (sebutkan bila ada):
   - Action item bimbingan yang sudah lewat tenggat.
   - `tinjau_ulang` pada TDR yang sudah lewat → usulkan meninjau TDR.
   - Lebih dari 90 hari sejak retrospeksi terakhir → usulkan skill `retro`.
   - Semua butir gate fase aktif sudah `[x]` → usulkan naik fase (minta konfirmasi sebelum mengubah `fase_aktif`).
   - Rekomendasi `[CARI: ...]` yang menumpuk di kartu ide → usulkan verifikasi.

3. **Sampaikan ringkasan** dalam ≤10 baris:
   ```
   Posisi: Fase N — <nama>, gate G<N>: x/y butir terpenuhi.
   Terakhir: <dari log terakhir, 1–2 kalimat>.
   Tertunda: <action item / tugas kanban, bila ada>.

   Usulan langkah berikutnya:
   1. <langkah paling penting> — (skill `...`, ±durasi)
   2. ...
   3. ...
   ```
   Urutan prioritas: tenggat bimbingan → butir gate fase aktif yang belum terpenuhi → utang sitasi → hal lain.

4. **Tunggu pilihan pengguna**, lalu jalankan skill yang sesuai. Jangan langsung mengerjakan sendiri tanpa persetujuan.

## Panduan per fase (bila tidak ada pemicu khusus)

| Fase | Langkah tipikal |
|---|---|
| 0 | Lanjutkan wawancara `profil` pada tema yang belum terisi |
| 1 | `gali-ide` sampai ≥10 kartu → `skor-ide` → `uji-tekan` untuk shortlist → tulis TDR |
| 2 | `scoping` untuk topik TDR; `resume` tingkat penuh untuk paper terdekat |
| 3 | Draf proposal di `03-proposal/draf/`; `rantai`; `kritik-naskah`; `cek sitasi` |
| 4 | Protokol review sistematis di `04-literatur/review-sistematis/`; screening |
| 5 | Protokol RQ → G4 → eksperimen; ADR untuk setiap keputusan metode |
| 6 | `checklist-submit`; respons reviewer |
| 7 | `09-disertasi/pemetaan.md`; `kritik-naskah` per bab |
| 8 | `uji-tekan` dengan persona penguji ujian |

## Penutup
Setelah pekerjaan sesi selesai: perbarui log hari ini (`_templates/log-harian.md`), jalankan `python3 scripts/wb.py status`, lalu sampaikan langkah berikutnya.
