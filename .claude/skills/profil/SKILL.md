---
name: profil
description: Wawancara profiling diri mahasiswa S3 (Fase 0) sekaligus inisialisasi workbench. Pakai ketika pengguna berkata "bantu aku mencari topik S3", "aku baru mulai S3", "aku belum punya topik", "isi profilku", atau saat workbench.yaml masih kosong.
---

# Profil — wawancara Fase 0

Tujuannya adalah mengenal pengguna sebagai peneliti **sebelum** membicarakan topik. Topik yang baik lahir
dari pertemuan antara keahlian, aset, minat, dan batasan, bukan dari daftar "topik tren".

## Prinsip wawancara
- **Satu tema per giliran.** Ajukan 2–4 pertanyaan yang berkaitan, lalu tunggu jawaban.
- Gali lebih dalam bila jawaban kabur. Contoh: "suka AI" → "AI untuk masalah apa? Pernah membangun apa?"
- Minta **bukti** untuk keahlian, misalnya proyek, kode, atau publikasi. Tingkat keahlian 1–5 ditetapkan pengguna, kamu boleh memberi masukan.
- Untuk setiap aset, tanyakan statusnya: `pasti`, `perlu-izin`, atau `spekulatif`. Bersikap skeptis secara sopan, karena "katanya bisa minta data ke kantor" itu `spekulatif`.
- Pengguna boleh menjawab "nanti" atau "lewati". Catat sebagai belum terisi.
- Sesi bisa dihentikan kapan saja. Profil diisi bertahap dan bisa dilanjutkan dengan skill `lanjut`.

## Langkah

### 0. Pembukaan & inisialisasi
- Jelaskan singkat: "Sebelum mencari topik, kita kenali dulu profil riset Anda. Prosesnya sekitar 6–8 tema, bisa dicicil."
- Tanyakan nama, kampus & prodi, bulan mulai studi, dan target lulus. Isi bagian `proyek` dan `kampus` di `workbench.yaml`.
- Bila kampusnya Udinus, set `kampus.profil: udinus`. Untuk kampus lain, biarkan kosong dan sebutkan bahwa profil kampus bisa dibuat nanti (`_templates/profil-kampus/README.md`).
- Tanyakan apakah sudah punya pedoman resmi kampus (PDF). Bila sudah, minta disimpan ke `00-admin/regulasi-kampus/`. Bila belum, catat sebagai tugas.
- Tanyakan persona: belum punya topik (P1), punya beberapa ide (P2), atau topik sudah ada (P3/P4). Untuk P2, persingkat tema 3–4 lalu langsung ke tema 5–6. Untuk P3/P4, isi tema 5–6 saja, set `fase_aktif` sesuai kondisi, dan arahkan ke skill `lanjut`.

### Tema wawancara (urut, satu per giliran)
1. **Latar:** pendidikan S1/S2 dan topik skripsi/tesis, pekerjaan saat ini dan lamanya, publikasi sebelumnya.
2. **Keahlian:** teknis, metodologis, dan menulis (ID/EN), masing-masing dengan bukti.
3. **Minat:** topik yang dibaca tanpa disuruh, masalah di pekerjaan yang membuat penasaran, paper atau tokoh yang menginspirasi.
4. **Motivasi & tujuan:** mengapa S3, mengapa sekarang, dan target karier setelah lulus (akademisi, industri, birokrasi).
5. **Aset riset:** akses ke data, sistem, atau populasi; jaringan dan kolaborator; posisi institusional; komputasi dan dana.
6. **Batasan:** batas beasiswa, waktu per minggu yang realistis, dana, kondisi keluarga dan pekerjaan.
7. **Gaya kerja:** lebih suka membangun sistem, menganalisis data, berinteraksi dengan manusia, atau teori? Seberapa tahan dengan pekerjaan berulang?
8. **Pembaca/penguji:** siapa calon promotor (bila sudah ada) dan apa latar bidang dosen di prodi. Isi `pembaca.latar_penguji` di `workbench.yaml`.

### Setelah setiap tema
- Tulis jawaban ke `01-profil-diri/profil.md` (salin dari `_templates/profil-diri.md` bila belum ada) dan ke `01-profil-diri/aset-riset.md` untuk tema 5.
- Hal yang masih spekulatif atau kontradiktif dicatat di bagian **Catatan agen**.

### Penutup sesi
1. Simpan catatan sesi di `01-profil-diri/refleksi/YYYY-MM-DD-sesi-N.md`. Isinya ringkasan, hal mengejutkan, dan pertanyaan terbuka.
2. Sampaikan **sintesis profil** dalam 5–7 baris: kekuatan khas, aset terkuat, batasan terkeras, dan 2–3 "zona topik" yang tampak cocok. Zona topik masih berupa arah, belum topik.
3. Kritik dengan jujur bila ada yang tidak realistis, misalnya target lulus 3 tahun dengan waktu riset 5 jam per minggu.
4. Isi `riset.disiplin`, lalu usulkan `riset.jenis` (modul) dan tunggu persetujuan pengguna.
5. Perbarui log hari ini dan jalankan `python3 scripts/wb.py status`.
6. Bila tema 1–6 sudah terisi, tawarkan agar pengguna mencentang `_gate/G0.md`. Setelah itu, tawarkan lanjut ke skill `gali-ide`.

## Batasan
- Jangan menyarankan topik spesifik sebelum tema 1–6 terisi. Zona topik boleh.
- Jangan menilai motivasi pengguna secara moral. Cukup periksa realismenya.
- Informasi pribadi tetap ada di repo pengguna. Ingatkan pengguna agar repo tetap **privat** bila profil berisi data sensitif.
