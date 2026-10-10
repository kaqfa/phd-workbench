# Modul: eksperimen-komputasi

**Untuk:** software engineering, machine learning, sistem, HPC.

**Aktifkan:** tambahkan `eksperimen-komputasi` ke `riset.jenis` di `workbench.yaml`, lalu buat:
- `07-artefak/<nama-artefak>/`: kode prototype (atau submodule Git)
- `07-artefak/konfigurasi-lingkungan/`: `requirements.txt`/`environment.yml`/`Dockerfile`, versi pustaka, spesifikasi perangkat keras

**Aturan tambahan:**
- Setiap run eksperimen mencatat commit hash, seed, versi pustaka, dan perangkat keras di `05-riset/rqN-*/eksperimen/`.
- Hasil di `hasil/` harus bisa dibangkitkan ulang dari `data/raw/` dengan satu perintah yang tercatat.
