# 📚 Sistem Manajemen Buku (E-Perpus)

Aplikasi manajemen perpustakaan digital berbasis web yang dibangun menggunakan **Django Framework**. Sistem ini dirancang untuk membantu pengelolaan inventaris buku secara terstruktur sekaligus memudahkan pengguna dalam mencari dan melakukan reservasi buku secara online.

---

## 🚀 Fitur Utama

### 👤 Fitur Pengguna

- Menampilkan katalog buku dengan tampilan responsif menggunakan Bootstrap 5.
- Pencarian buku berdasarkan judul atau nama penulis.
- Filter buku berdasarkan kategori.
- Menampilkan informasi stok dan status ketersediaan buku secara real-time.
- Melakukan reservasi buku secara online.
- Melihat detail buku lengkap beserta gambar sampul.

### 🔐 Fitur Admin

- Login khusus admin menggunakan sistem autentikasi Django.
- CRUD data Buku, Kategori, dan Reservasi.
- Persetujuan (approval) reservasi buku.
- Pengelolaan stok buku secara otomatis.
- Monitoring status reservasi dengan tampilan visual yang mudah dipahami.

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Keterangan |
|-----------|------------|
| Django 4.2+ | Framework Backend |
| Python 3.x | Bahasa Pemrograman |
| HTML5 & CSS3 | Struktur dan Styling |
| Bootstrap 5 | Framework Frontend |
| SQLite | Database |
| Pillow | Pengelolaan gambar sampul buku |

---

## ⚙️ Panduan Instalasi

### 1. Clone Repository

```bash
git clone (https://github.com/slf4A/UAS_SistemManajemenBuku.git)
cd (https://github.com/slf4A/UAS_SistemManajemenBuku.git)
```

### 2. Membuat Virtual Environment

```bash
python -m venv venv
```

### 3. Mengaktifkan Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependency

```bash
pip install -r requirements.txt
```

### 5. Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Membuat Akun Admin

```bash
python manage.py createsuperuser
```

Ikuti instruksi yang muncul untuk membuat username, email, dan password administrator.

### 7. Menjalankan Server

```bash
python manage.py runserver
```

Buka browser dan akses:

- Halaman User: `http://127.0.0.1:8000/`
- Dashboard Admin: `http://127.0.0.1:8000/admin/`

---

## 📂 Struktur Proyek

```
E-Perpus/
│
├── core/               # Konfigurasi utama project Django
├── inventory/          # Aplikasi utama
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── templates/          # Template HTML
├── static/             # CSS, JS, dan asset lainnya
├── media/              # Penyimpanan gambar sampul buku
├── db.sqlite3          # Database SQLite
├── manage.py
└── requirements.txt
```

---

**Sifa Jema (2308107010080)**

Project dibuat sebagai tugas pengembangan aplikasi web menggunakan Django Framework. Dan Project ini dibuat untuk keperluan Ujian Akhir Semester. 

---
