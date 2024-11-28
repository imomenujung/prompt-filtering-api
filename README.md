
# Prompt Filtering API

## Deskripsi
Prompt Filtering API adalah aplikasi berbasis FastAPI yang dirancang untuk memfilter input teks berdasarkan kata kunci tertentu dan mengukur kemiripan semantik menggunakan model *sentence embeddings*. Tujuan utama API ini adalah untuk memastikan prompt aman digunakan dengan memadukan pendekatan berbasis aturan dan pembelajaran mesin.

## Fitur Utama
1. **Pemeriksaan berdasarkan kata kunci eksplisit**: Deteksi prompt yang mengandung kata kunci tidak diinginkan.
2. **Pemeriksaan berbasis embeddings**: Menggunakan model `SentenceTransformer` untuk mengukur kemiripan semantik antara prompt dan daftar kata kunci filter.
3. **Endpoint API yang mudah digunakan**: Menyediakan endpoint `/check_prompt` untuk memvalidasi prompt.

## Teknologi yang Digunakan
- **FastAPI**: Framework web untuk membangun API yang cepat dan efisien.
- **Sentence Transformers**: Library pembelajaran mesin untuk *sentence embeddings*.
- **Python**: Bahasa pemrograman utama.

## Prasyarat
1. Python 3.8 atau lebih baru.
2. File `filter_keywords.json` yang berisi kata kunci filter dalam format berikut:
    ```json
    {
        "keywords": ["keyword1", "keyword2", "keyword3"]
    }
    ```

## Cara Instalasi dan Penggunaan

### 1. Instalasi Dependensi
```bash
pip install fastapi uvicorn sentence-transformers
```

### 2. Jalankan API
```bash
uvicorn main:app --reload
```

### 3. Endpoint API
- **GET /**: Mengembalikan pesan sambutan.
- **POST /check_prompt**: Memvalidasi prompt berdasarkan kriteria keamanan.

### Contoh Payload untuk Endpoint `/check_prompt`
```json
{
    "prompt": "Contoh teks yang ingin diperiksa"
}
```

### Respon
- Jika aman:
    ```json
    {
        "safe": true
    }
    ```
- Jika tidak aman:
    ```json
    {
        "safe": false
    }
    ```

## Alur Logika
1. **Memuat Kata Kunci**: Kata kunci dimuat dari file `filter_keywords.json`.
2. **Pemeriksaan Embedding**: Mengukur kesamaan semantik antara prompt dan kata kunci.
3. **Pemeriksaan Eksplisit**: Memeriksa apakah prompt mengandung kata kunci secara langsung.
4. **Hasil Validasi**: Menggabungkan hasil dari kedua pemeriksaan untuk menentukan keamanan prompt.

## Struktur Direktori
```
.
├── main.py                 # File utama API
├── filter_keywords.json    # File kata kunci
├── README.md               # Dokumentasi
```

## Catatan
Pastikan file `filter_keywords.json` berada di direktori yang sama dengan `main.py`.
