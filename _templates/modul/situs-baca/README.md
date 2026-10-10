# Modul: situs-baca (opsional)

**Untuk:** membaca naskah dari HP atau berbagi bacaan ke promotor lewat situs statis privat (mis. MkDocs).

**Pendekatan:**
- Buat `allowlist.txt` berisi path yang **boleh** dipublikasi (default: tidak ada). Jangan memakai denylist sebagai satu-satunya pengaman.
- Skrip ekspor menyalin hanya berkas di allowlist ke folder build, lalu menjalankan `mkdocs build`.
- Jangan pernah menyertakan `04-literatur/pdf/`, `06-subjek-data/`, `data/raw/`.
- Situs dihosting privat (akses berpassword); jangan memakai host pribadi tanpa autentikasi.

Belum ada skrip bawaan; modul ini adalah pedoman.
