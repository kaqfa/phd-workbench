# Aturan Kerja PhD-Workbench

Dokumen ini adalah **satu-satunya sumber aturan** untuk manusia dan agen AI. Berkas lain
(`CLAUDE.md`, `AGENTS.md`, README folder, skill) hanya merujuk ke sini. Bila ada yang bertentangan,
dokumen inilah yang berlaku.

---

## 1. Sitasi: gate tiga langkah

Sebuah referensi baru boleh dipakai di naskah yang dikirim (ke promotor, panitia, atau venue) bila
**ketiga langkah** berikut terpenuhi:

1. **Ada sumbernya.** PDF/teks lengkap tersimpan di `04-literatur/pdf/<klaster>/`, atau tercatat
   alasan kenapa tidak bisa diunduh (berbayar, buku cetak) disertai lokasi aksesnya.
2. **Ada resumenya.** `04-literatur/resume/<bibkey>.md` tersedia. Untuk klaim substantif (angka,
   temuan, definisi) resume harus bertingkat `penuh`, dengan **kutipan verbatim + nomor halaman**.
3. **Bib terverifikasi.** Entri di `04-literatur/bibliografi/references.bib` memiliki
   `note = {VERIFIED: <bukti>}`. Buktinya berupa DOI yang di-resolve, URL penerbit, atau ID
   arXiv/OpenAlex, lengkap dengan tanggal pengecekan.

Catatan penting: metadata yang valid hanya membuktikan paper itu **ada**. Itu tidak membuktikan isinya
sesuai dengan yang diingat. Kebenaran isi diperiksa dengan membaca kutipan verbatim di resume.

- Paper yang disebut tetapi belum diverifikasi ditulis `[CARI: penulis, tahun, kata kunci]`.
  Jangan menulis kunci sitasi yang tampak meyakinkan untuk paper semacam ini.
- Resume tingkat `cepat` cukup untuk menunjukkan posisi dan eksistensi ("X juga meneliti Y"), tetapi
  tidak cukup untuk klaim angka.
- Pemeriksaan otomatis dijalankan dengan `python3 scripts/wb.py cek sitasi <naskah>`.

## 2. Data

1. **`data/raw/` tidak pernah diedit.** Semua transformasi dilakukan lewat skrip di `analisis/`,
   dan hasilnya disimpan di `data/processed/`.
2. **Folder sensitif** (`data.folder_sensitif` di `workbench.yaml`) tidak pernah di-commit dan
   tidak pernah dibaca agen, kecuali pemilik data mengizinkannya secara eksplisit.
3. **Model tertutup.** Data sensitif tidak dikirim ke layanan AI pihak ketiga kecuali
   `data.boleh_ke_model_tertutup: true` **dan** ada izin dari pemilik data.
4. **Hasil keluar hanya dalam bentuk agregat.** Baris individual, identitas, dan kutipan wawancara yang
   bisa dikenali tidak boleh masuk ke naskah atau repo publik.
5. Sebelum commit, periksa `git status`. Jangan menjalankan `git add .` secara membabi buta di folder data.

## 3. Protokol sebelum data

1. Setiap RQ memiliki `protokol/protokol.md` (dari `_templates/protokol-studi.md`) yang **dibekukan**
   (`status: beku`, dengan tanggal) **sebelum** data dikumpulkan atau eksperimen utama dijalankan.
2. Perubahan setelah pembekuan dicatat di bagian **Penyimpangan dari protokol**, beserta alasannya.
   Protokol tidak ditulis ulang diam-diam.
3. Eksplorasi (pilot, *sanity check*) boleh dilakukan sebelum pembekuan, tetapi ditandai sebagai
   eksplorasi dan tidak dilaporkan sebagai konfirmasi.

## 4. Keputusan dan gate

1. Setiap keputusan riset penting (topik, RQ, metode, subjek, venue, pembatalan) dicatat sebagai
   decision record: TDR untuk topik di `02-eksplorasi-topik/keputusan/`, selebihnya ADR di
   `11-jurnal-riset/keputusan/`. Yang dicatat adalah **alasannya**, bukan hanya hasilnya.
2. Gate di `_gate/` dinyatakan lolos bila semua butir `[x]` dan ada tautan ke decision record.
3. **Hanya mahasiswa yang meloloskan gate.** Agen boleh melaporkan butir yang belum terpenuhi,
   tetapi tidak mencentang butir gate atas inisiatif sendiri.
4. Gate boleh dilewati dengan catatan alasan tertulis. Workbench ini alat bantu, bukan birokrasi.
5. **Syarat formal kampus** (jumlah/kuartil publikasi, format, tahapan) hanya diisi dari dokumen di
   `00-admin/regulasi-kampus/`. Bila belum ada, tulis `BELUM DICEK`. Syarat tidak boleh dikarang
   dari ingatan.

## 5. Etika dan integritas akademik

1. **Agen tidak menulis disertasi atas nama mahasiswa.** Draf dari agen selalu ditandai dan disunting
   penuh oleh pemiliknya. Workbench ini tidak boleh dijadikan alat joki.
2. **Tidak mengarang referensi.** Lihat §1.
3. **Tidak mengarang data atau hasil.** Gunakan placeholder eksplisit, misalnya
   `[TODO: butuh data dari RQ-2]`.
4. **Ikuti kebijakan penggunaan AI** dari kampus dan venue. Ungkapkan penggunaan AI bila diwajibkan
   (butir ini ada di `checklist-submit.md`).
5. **Bedakan temuan, rencana, dan spekulasi** di setiap draf.
6. **Hindari plagiarisme dan *self-plagiarism*.** Parafrase dari agen tetap harus dicek terhadap
   sumbernya. Tidak boleh ada pengiriman ganda atau *salami slicing*.

## 6. Penanda draf agen

Teks yang disusun agen dan masuk ke naskah (proposal, paper, disertasi) dibungkus penanda berikut:

```markdown
<!-- DRAF-AGEN: YYYY-MM-DD, <skill/konteks> -->
...teks...
<!-- /DRAF-AGEN -->
```

Penanda baru dihapus oleh mahasiswa setelah ia menyunting dan memahami teks tersebut. Setiap draf
panjang dari agen ditutup dengan daftar **bagian terlemah** yang perlu diperiksa.

## 7. Gaya dan berkas

1. Nama berkas memakai huruf kecil dengan tanda hubung (`kebab-case`). Tanggal ditulis `YYYY-MM-DD`.
2. Berkas yang memakai template wajib memiliki frontmatter YAML sesuai templatenya, karena
   `wb status` membaca frontmatter tersebut.
3. Satu nomor folder untuk satu folder. Folder baru di akar tidak dibuat tanpa catatan keputusan.
4. Semua path ditulis relatif terhadap akar repo, bukan path absolut mesin pribadi.
5. `STATUS.md` tidak diedit tangan. Perbarui dengan `python3 scripts/wb.py status`.
6. Berkas usang tidak dihapus. Pindahkan ke `99-arsip/YYYY-MM-DD-<nama>/`.
