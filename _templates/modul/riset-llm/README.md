# Modul: riset-llm

**Untuk:** riset yang memakai LLM sebagai alat atau objek penelitian.

**Aktifkan:** tambahkan `riset-llm` ke `riset.jenis`, lalu buat:
- `07-artefak/prompt-library/`: satu berkas per prompt, berversi (`nama-v1.md`, `nama-v2.md`), dengan frontmatter `versi`, `tanggal`, `dipakai_di`
- `07-artefak/konfigurasi-model/`: satu berkas per konfigurasi berisi provider, nama & versi model persis, temperature, top_p, seed, max_tokens, dan **tanggal akses**

**Aturan tambahan:**
- Model yang "sama" bisa berubah di balik API. Tanggal akses dan versi persis wajib dicatat.
- Simpan keluaran mentah LLM di `data/raw/`; penilaian/anotasi di `data/processed/`.
- Bila data sensitif ikut ke prompt, berlaku ATURAN §2.3.
