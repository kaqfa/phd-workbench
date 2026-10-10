# Profil Kampus

Satu folder per kampus: `profil-kampus/<kampus>/`. Profil kampus berisi **ringkasan syarat formal**
(diambil dari pedoman resmi, lengkap dengan halaman rujukan) dan template naskah (LaTeX/Word) bila tersedia.

## Membuat profil kampus baru
1. Simpan pedoman resmi (PDF) di `00-admin/regulasi-kampus/`.
2. Salin `udinus/README.md` sebagai kerangka ke `profil-kampus/<kampus>/README.md`.
3. Isi setiap baris **hanya dari pedoman resmi**, dengan rujukan dokumen + halaman. Yang belum ditemukan biarkan `BELUM DICEK`.
4. Taruh template naskah resmi (bila ada) di `profil-kampus/<kampus>/naskah-seleksi/` dan `.../disertasi/`.
5. Set `kampus.profil: <kampus>` di `workbench.yaml`.

Agen boleh membantu meringkas PDF pedoman, tetapi setiap syarat yang ditulis harus menyertakan halaman sumbernya.
