---
jenis: checklist-submit
paper: paper-N-slug
venue: ""
tanggal: YYYY-MM-DD
status: belum           # belum | siap | terkirim
---

# Checklist Submit: <judul paper>

## Venue
- [ ] Indeks diverifikasi langsung di sumber (Scopus/WoS/SINTA/DBLP), bukan dari situs venue saja
- [ ] Bukan predator/hijacked (cek URL resmi, alamat penerbit, kecepatan review yang wajar, biaya)
- [ ] Ruang lingkup cocok; format & batas halaman sesuai author guidelines
- [ ] Kebijakan AI venue dibaca: <ringkas>
- [ ] Syarat kampus untuk publikasi ini (kuartil/indeks): BELUM DICEK → `00-admin/regulasi-kampus/`

## Integritas
- [ ] Tidak sedang dikirim ke venue lain
- [ ] Tidak salami: kontribusi berbeda dari paper lain saya (sebutkan pembedanya)
- [ ] Pernyataan penggunaan AI ditulis (bila diwajibkan)
- [ ] Tidak ada penanda `DRAF-AGEN`, `[TODO`, `[CARI:` tersisa
- [ ] Cek similarity dilakukan

## Isi
- [ ] `python3 scripts/wb.py cek sitasi <naskah>` lulus
- [ ] Setiap angka di naskah dapat dilacak ke `05-riset/rq*/hasil/`
- [ ] Gambar/tabel dibangkitkan ulang dari skrip
- [ ] Replication package dirakit (kode, data yang boleh dibagi, README)
- [ ] Semua penulis menyetujui naskah final
