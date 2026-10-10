---
name: skor-ide
description: Menilai dan membandingkan kartu ide dengan matriks skor berbobot untuk membuat shortlist (Fase 1). Pakai ketika pengguna minta ide-idenya dinilai, dibandingkan, atau diranking.
---

# Skor Ide — matriks berbobot

## Prinsip
**Skor adalah alat diskusi, bukan keputusan.** Agen mengusulkan skor beserta alasannya, sedangkan
**pengguna yang menetapkan** skor akhirnya. Ide dengan skor tertinggi tetap harus lolos uji tekan dan scoping.

## Langkah
1. Siapkan `02-eksplorasi-topik/matriks-skor.md` (salin dari template bila belum ada). Tanyakan apakah pengguna ingin mengubah bobot. Bila ya, catat alasannya di berkas tersebut.
2. **Saring gugur langsung** untuk semua kartu berstatus `baru`: data mustahil diakses, dana di luar jangkauan, atau melanggar etika. Kartu yang gugur diubah ke `status: gugur` dengan `alasan_gugur`, dan atas persetujuan pengguna.
3. Untuk setiap ide yang tersisa (bisa dicicil 3–5 ide per giliran):
   - Usulkan skor K1–K7 masing-masing dengan **satu kalimat alasan** yang merujuk profil, aset, atau kartu ide.
   - Tandai skor yang paling tidak pasti, terutama K3 (kebaruan), karena itu baru hipotesis.
   - Minta pengguna mengonfirmasi atau mengubah skor.
4. Hitung total berbobot (Σ skor × bobot) dan tulis tabelnya ke matriks. Alasan ditulis di bagian "Alasan skor".
5. Ubah status kartu menjadi `diskor`. Ambil 3 teratas (atau pilihan pengguna) dan ubah menjadi `shortlist`.
6. Tunjukkan **sensitivitas**: apakah urutan berubah bila bobot K2 atau K3 digeser ±10%? Bila ya, sampaikan bahwa pilihannya belum kokoh.

## Penutup
Perbarui log dan status. Usulkan langkah berikutnya, yaitu skill `uji-tekan` untuk setiap ide shortlist.

## Batasan
- Jangan menaikkan skor ide favorit pengguna untuk menyenangkannya. Jangan pula menurunkannya untuk terlihat kritis.
- Skor tidak boleh menjadi satu-satunya dasar TDR.
