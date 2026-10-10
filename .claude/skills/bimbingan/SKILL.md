---
name: bimbingan
description: Menyiapkan agenda bimbingan promotor dari log kerja, dan merapikan catatan bimbingan menjadi action item bertanggal. Pakai ketika pengguna mau bimbingan, baru selesai bimbingan, atau minta catatan bimbingan dirapikan.
---

# Bimbingan

## Sebelum pertemuan
1. Temukan bimbingan terakhir di `11-jurnal-riset/bimbingan/`. Baca semua log sejak tanggal itu dan ADR yang baru.
2. Buat `11-jurnal-riset/bimbingan/YYYY-MM-DD-bimbingan.md` dari template, lalu isi:
   - **Agenda** (maksimal 3–5 butir): keputusan yang butuh persetujuan promotor didahulukan, kemudian masalah buntu, lalu laporan kemajuan.
   - **Yang dilaporkan**: progres sejak pertemuan lalu dan status action item lama (selesai/belum, dengan alasan).
3. Untuk setiap butir keputusan, siapkan 2–3 opsi beserta rekomendasi pengguna. Promotor lebih mudah memilih daripada mengarang dari nol.
4. Bantu pengguna menyiapkan materi pendukung yang ringkas, misalnya tabel atau diagram.

## Sesudah pertemuan
1. Minta pengguna menuliskan atau menempelkan catatan mentah, termasuk catatan suara yang sudah ditranskripsi.
2. Rapikan catatan ke bagian **Masukan**, **Keputusan**, dan **Action item** (item, PIC, tenggat bertanggal). Tanyakan tenggatnya bila tidak disebut, jangan dikarang.
3. Setiap keputusan riset dicatat sebagai ADR di `11-jurnal-riset/keputusan/`. Perbarui TDR, `workbench.yaml`, atau gate bila terdampak.
4. Bila ada masukan yang bertentangan dengan keputusan sebelumnya, sampaikan ke pengguna.

## Batasan
Catatan bimbingan adalah dokumen pengguna. Jangan menambahkan "masukan promotor" yang tidak ada di catatan mentah.
