---
name: gali-ide
description: Membangkitkan ide topik disertasi menjadi kartu ide (Fase 1). Pakai ketika pengguna minta dicarikan ide/topik S3, ingin menambah ide, atau memasukkan ide yang sudah dimiliki.
---

# Gali Ide — dari profil ke kartu ide

## Prasyarat
`01-profil-diri/profil.md` dan `aset-riset.md` sudah terisi (G0). Bila belum, sampaikan bahwa ide akan lebih tajam setelah profiling, lalu tawarkan skill `profil`. Bila pengguna tetap ingin lanjut, teruskan dengan catatan tersebut.

## Empat sumber ide
Bangkitkan ide dari keempat sumber berikut, masing-masing 2–5 ide:
1. **Masalah di pekerjaan.** Masalah nyata yang dialami pengguna atau institusinya.
2. **Aset unik × tren bidang.** Gabungan aset `pasti` atau `perlu-izin` milik pengguna dengan arah riset yang sedang aktif. Ide dari sumber ini sering paling sulit ditiru orang lain.
3. **Future work.** Bagian *future work* atau *limitations* dari paper yang sudah dibaca pengguna (`04-literatur/resume/`), atau dari paper yang pengguna sebutkan.
4. **Kebutuhan institusi.** Roadmap riset prodi atau kampus, minat calon promotor, kebutuhan mitra.

Pengguna P2 yang sudah punya ide: masukkan dulu ide-ide tersebut sebagai kartu, baru tambahkan ide baru.

## Langkah
1. Bacakan ringkasan profil dalam 3 baris dan zona topik dari sesi profiling.
2. Jalankan sumber ide satu per satu dan diskusikan dengan pengguna. Ajukan pertanyaan pemicu, misalnya "Masalah apa di kantor yang paling sering dikeluhkan?"
3. Untuk setiap ide yang disetujui pengguna, buat kartu `02-eksplorasi-topik/kartu-ide/ide-NN-<slug>.md` dari `_templates/kartu-ide.md`. Nomor `NN` melanjutkan nomor terakhir. Isi `sumber` dan `status: baru`.
4. **Paper pemicu**:
   - Paper yang kamu sebut dari ingatan **wajib** ditulis `[CARI: penulis?, tahun?, kata kunci]` dengan status verifikasi `belum`. Jangan menulis judul atau DOI yang terlihat pasti bila belum dicek.
   - Bila ada akses web atau API (OpenAlex, Semantic Scholar, Crossref, arXiv), boleh langsung diverifikasi. Tulis DOI/URL dan tanggal cek, lalu ubah status menjadi `ada (metadata)`. Ingat: metadata hanya membuktikan paper itu ada, bukan isinya.
5. Isi "Risiko terbesar" dengan jujur. Ide tanpa risiko berarti belum dipikirkan dengan serius.
6. Target sesi adalah **10–20 kartu**. Variasi lebih penting daripada kesempurnaan. Ide yang setengah matang tetap ditulis.

## Penutup
- Ringkas dalam bentuk tabel: ID, judul, sumber, aset yang dipakai, satu kalimat risiko.
- Perbarui log hari ini dan jalankan `python3 scripts/wb.py status`.
- Set `fase_aktif: 1` bila masih 0 (setelah G0 dicentang pengguna).
- Usulkan langkah berikutnya: skill `skor-ide` bila sudah ≥10 kartu, atau verifikasi `[CARI: ...]` lebih dulu.

## Batasan
- Jangan mempromosikan ide hanya karena "sedang tren". Kaitkan setiap ide dengan profil.
- Jangan menyatakan ide itu "belum pernah diteliti". Klaim kebaruan baru boleh diuji di Fase 2 (scoping).
