---
name: resume
description: Membuat resume paper dari PDF dengan kutipan verbatim dan nomor halaman, serta memverifikasi entri bib. Pakai ketika pengguna minta paper diresume, dibaca, dirangkum, atau ditambahkan ke literatur.
---

# Resume — dari PDF ke resume terverifikasi

## Prasyarat
Teks lengkap tersedia di `04-literatur/pdf/<klaster>/<bibkey>.pdf`, atau diberikan pengguna. **Tanpa teks lengkap, hanya resume tingkat `cepat` dari abstrak yang boleh dibuat**, dan hal ini dicatat di `sumber_teks`.

## Langkah
1. Tentukan `bibkey` (format `penulisTAHUNkata`, atau ikuti kunci dari Zotero/Better BibTeX). Pastikan entri ada di `references.bib`.
2. **Verifikasi metadata** lewat DOI, Crossref, OpenAlex, atau arXiv bila ada akses. Isi `note = {VERIFIED: doi:<doi> dicek YYYY-MM-DD}`. Bila tidak bisa diverifikasi, tulis `note = {UNVERIFIED}`.
3. Tanyakan tingkat resume: `cepat` (posisi/eksistensi) atau `penuh` (dipakai untuk klaim substantif).
4. Baca PDF, lalu buat `04-literatur/resume/<bibkey>.md` dari template. Isi `oleh: agen`.
5. **Tingkat penuh — aturan kutipan:**
   - Setiap kutipan verbatim harus **persis** sama dengan teks di PDF, sehingga bisa ditemukan dengan pencarian teks. Sertakan nomor halaman sesuai halaman cetak; bila tidak ada, gunakan halaman PDF dan tandai `(pdf)`.
   - Klaim yang dicari tetapi tidak ditemukan ditulis "tidak ditemukan di naskah". Jangan ditebak.
   - Angka disalin persis, termasuk satuan dan kondisi eksperimennya.
6. Isi "Relevansi untuk riset saya" dengan merujuk topik di TDR atau RQ di `workbench.yaml`.
7. Bila banyak paper diproses sekaligus, buat tugas pekerja di `.agents/kanban/`. Supervisor (atau pengguna) memeriksa sampel acak kutipan terhadap PDF sebelum tugas dipindah ke `done/`.

## Penutup
Sampaikan bahwa resume berlabel `oleh: agen` perlu dibaca ulang pengguna. Pengguna yang mengubahnya menjadi `oleh: mahasiswa` setelah memeriksa. Perbarui log.

## Batasan
- Jangan pernah membuat kutipan "yang kira-kira seperti itu". Kutipan yang tidak bisa ditemukan di PDF adalah halusinasi.
- Hormati hak cipta. PDF tidak di-commit secara default, dan resume berisi kutipan pendek, bukan salinan bagian panjang.
