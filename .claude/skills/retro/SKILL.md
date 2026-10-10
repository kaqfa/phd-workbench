---
name: retro
description: Retrospeksi kuartalan - membandingkan rencana dan realisasi dari log, meninjau ulang TDR dan RQ, dan menyusun rencana kuartal berikutnya. Pakai ketika pengguna minta evaluasi kuartal/semester, retrospeksi, atau merasa stuck.
---

# Retro — retrospeksi kuartalan

## Langkah
1. Tentukan periodenya (default: kuartal terakhir). Baca:
   - semua log dan bimbingan pada periode itu;
   - retrospeksi sebelumnya beserta rencananya;
   - ADR baru;
   - TDR (kriteria pembatalan, `tinjau_ulang`);
   - `STATUS.md`.
2. Buat `11-jurnal-riset/retrospeksi/YYYY-QN.md` dari template.
3. Isi tabel **rencana vs realisasi** dari data log, bukan dari ingatan. Hitung pola sederhana seperti jumlah hari dengan log dan fase yang dominan dikerjakan.
4. Ajukan pertanyaan reflektif satu per satu:
   - Apa yang berubah?
   - Apakah RQ masih relevan?
   - Apakah ada kriteria pembatalan TDR yang terpicu?
   - Apa yang menghambat paling banyak?
   - Apakah beban kerja realistis terhadap batasan di profil?
5. Sampaikan dengan jujur bila terjadi *drift*, misalnya banyak waktu terserap kegiatan yang tidak memajukan gate. Sampaikan tanpa menghakimi.
6. Bantu menyusun **rencana kuartal berikutnya**: 3–5 target konkret yang terkait gate, dan masukkan ke `.agents/kanban/todo/` bila relevan.
7. Bila TDR perlu ditinjau, perbarui `tinjau_ulang` atau ubah status TDR atas keputusan pengguna, beserta ADR-nya.

## Penutup
Perbarui log dan status.
