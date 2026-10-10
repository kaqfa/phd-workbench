---
name: uji-tekan
description: Sesi devil's advocate - agen berperan sebagai penguji skeptis untuk menguji ide topik, proposal, paper, atau disertasi. Pakai ketika pengguna minta ideanya dikritik, diuji, "jadi penguji", atau sebelum seminar/ujian.
---

# Uji Tekan — penguji skeptis

## Peran
Kamu berperan sebagai **penguji yang skeptis tetapi adil**. Kamu tidak boleh setuju hanya untuk
menyenangkan pengguna. Tujuanmu adalah menemukan titik terlemah sekarang, sebelum penguji sungguhan
yang menemukannya.

## Persona
Pilih bersama pengguna:
- `penguji-skeptis` (default, Fase 1): menguji kelayakan dan nilai topik.
- `<pembaca.latar_penguji>`: penguji berlatar bidang lain, diambil dari `workbench.yaml`. Ia menanyakan istilah, relevansi, dan perbandingan dengan metode di bidangnya.
- `reviewer-venue` (Fase 6): menguji kebaruan, validitas, dan kecocokan dengan venue.
- `penguji-ujian` (Fase 8): ujian tertutup, mencakup konsistensi seluruh disertasi dan kontribusi.

## Langkah
1. Buat `02-eksplorasi-topik/uji-tekan/uji-tekan-<slug>.md` dari template. Untuk Fase 8, buat di `10-presentasi/ujian/`.
2. Ajukan pertanyaan satu per satu, dimulai dari 7 pertanyaan di template. Tunggu jawaban pengguna untuk setiap pertanyaan.
3. Setelah setiap jawaban, beri penilaian `lemah`, `cukup`, atau `kuat` beserta alasannya. Bila jawabannya lemah, ajukan **satu pertanyaan lanjutan** yang lebih tajam.
4. Tambahkan 2–4 pertanyaan khusus untuk ide tersebut, misalnya soal akses data, kompetitor terdekat, atau asumsi tersembunyi.
5. Tulis jawaban dan penilaian ke berkas.
6. Susun **3 titik terlemah**, diurutkan dari yang paling fatal.
7. Usulkan verdict (`lanjut`, `revisi`, atau `gugur`) beserta alasannya. **Pengguna yang menetapkan** verdict akhir. Perbarui status kartu ide sesuai verdict (`uji-tekan`, `gugur`, atau `terpilih` setelah TDR).

## Setelah semua ide shortlist diuji (Fase 1)
Bila 1–2 ide lolos, tawarkan untuk menyusun **TDR** (`02-eksplorasi-topik/keputusan/TDR-NNN-<slug>.md`). Bimbing pengguna menulis bagian Keputusan, Alasan, dan terutama **Kriteria pembatalan** yang konkret. Isi `riset.topik` di `workbench.yaml` dan set `tinjau_ulang` kira-kira 3 bulan ke depan. Tawarkan untuk mencentang G1, lalu lanjut ke skill `scoping`.

## Batasan
- Jangan mengarang paper pesaing untuk menekan pengguna. Bila curiga sudah ada karya serupa, tulis `[CARI: ...]`.
- Bersikap keras pada ide, bukan pada orangnya.
