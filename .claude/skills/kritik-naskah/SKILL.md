---
name: kritik-naskah
description: Mengkritik struktur, argumen, dan integritas naskah (proposal, paper, bab disertasi). Pakai ketika pengguna minta naskahnya direview, dikritik, dicek sebelum dikirim ke promotor/venue.
---

# Kritik Naskah

## Langkah
1. Tanyakan konteksnya: jenis naskah, pembaca sasaran (promotor, reviewer venue, penguji), dan tenggat. Ambil `pembaca.latar_penguji` dari `workbench.yaml`.
2. Jalankan `python3 scripts/wb.py cek sitasi <naskah>` dan laporkan hasilnya.
3. Baca seluruh naskah, lalu kritik dalam tiga lapis (dari besar ke kecil):
   1. **Argumen & struktur:** Apakah masalah, celah, kontribusi, dan bukti tersambung? Apakah tiap bagian menjalankan fungsinya? Apakah ada lompatan logika?
   2. **Integritas:**
      - Klaim tanpa data atau rujukan.
      - Sitasi tanpa resume, atau sitasi yang menopang klaim angka dengan resume `cepat`.
      - Angka yang tidak bisa dilacak ke `hasil/`.
      - Temuan, rencana, dan spekulasi yang tercampur.
      - Sisa penanda `DRAF-AGEN`, `[TODO`, atau `[CARI:`.
   3. **Keterbacaan:** kalimat lebih dari ±40 kata, istilah yang tidak konsisten, istilah inti yang perlu padanan untuk penguji lintas bidang, serta paragraf tanpa kalimat topik.
4. Tulis kritik dalam bentuk tabel `lokasi | masalah | saran`, diurutkan dari yang paling berat. Sertakan kritik di chat, atau simpan di `<folder-naskah>/kritik-YYYY-MM-DD.md` bila panjang.
5. Akhiri dengan **3 bagian terlemah** yang paling perlu dikerjakan.

## Batasan
- Defaultnya adalah **mengkritik, bukan menulis ulang**. Bila pengguna meminta contoh perbaikan, berikan untuk 1–2 paragraf saja, dengan penanda `DRAF-AGEN`.
- Jangan menilai naskah "sudah bagus" tanpa alasan spesifik.
