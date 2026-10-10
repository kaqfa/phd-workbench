---
name: scoping
description: Scoping review 1-2 minggu untuk memvalidasi apakah celah riset topik terpilih masih ada (Fase 2). Pakai ketika pengguna minta cek celah, cek apakah topik sudah diteliti orang, atau scoping review.
---

# Scoping — validasi celah

## Prasyarat
Ada TDR yang `berlaku`. Bila belum ada, tawarkan untuk menyelesaikan Fase 1 dulu. Scoping tanpa topik akan menjadi kegiatan membaca tanpa arah.

## Langkah
1. Buat `04-literatur/scoping/scoping-<slug>.md` dari template. Rumuskan bersama pengguna **1–3 celah** dalam satu kalimat yang bisa disanggah.
2. **Susun string pencarian**: sinonim, istilah dari bidang tetangga, dan istilah lama. Tentukan kriteria inklusi dan eksklusi. Tunjukkan semuanya ke pengguna sebelum mencari.
3. **Cari** melalui API bila tersedia: OpenAlex (`api.openalex.org/works?search=`), Semantic Scholar, arXiv, Crossref. Catat setiap query di tabel strategi (sumber, query, tanggal, jumlah hasil). Bila tidak ada akses jaringan, berikan string pencarian untuk dijalankan pengguna secara manual, lalu proses hasil ekspornya.
   - Pencarian yang panjang dicatat sebagai tugas pekerja di `.agents/kanban/` beserta *verification commands*.
4. **Saring** berdasarkan judul dan abstrak. Untuk ±10–20 paper terdekat:
   - Tambahkan ke `references.bib` dengan `note = {VERIFIED: doi:... dicek YYYY-MM-DD}` bila metadatanya terverifikasi lewat API.
   - Buat resume tingkat `cepat`. Untuk ≥5 paper yang paling dekat dengan celah, buat resume tingkat `penuh` dengan skill `resume` (butuh PDF).
5. Untuk setiap celah, isi tabel "paper terdekat" dengan penilaian `mengisi`, `sebagian`, atau `beda`, disertai alasan yang merujuk kutipan di resume.
6. Usulkan verdict celah (`bertahan`, `sebagian`, atau `sudah-terisi`). **Pengguna yang menetapkan.**
7. Bila celah `sudah-terisi`, periksa kriteria pembatalan di TDR. Diskusikan pivot (mempersempit, mengganti konteks, mengganti metode) atau kembali ke Fase 1. Kegagalan di tahap ini murah, jadi sampaikan dengan nada positif.
8. Tulis `04-literatur/scoping/hasil.md`: ringkasan celah yang bertahan, 2–4 draf RQ, dan rencana bila celah ternyata terisi. Isi `riset.rq` di `workbench.yaml` setelah pengguna menyetujuinya.

## Penutup
Perbarui log, status, dan klaster literatur di `workbench.yaml` (`riset.klaster_literatur`). Tawarkan untuk mencentang G2, lalu lanjut ke proposal (Fase 3) dan skill `rantai`.

## Batasan
- "Tidak menemukan" tidak sama dengan "tidak ada". Laporkan keterbatasan pencarian (database yang tidak dicakup, bahasa, rentang tahun).
- Jangan menilai celah berdasarkan abstrak saja untuk paper yang paling dekat. Baca teks lengkapnya.
