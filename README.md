# 🏦 Sistem Prediksi Kelayakan Pinjaman Bank

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](MASUKKAN_LINK_STREAMLIT_KAMU_DISINI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Hai fella! 👋 Selamat datang di project **Loan Prediction App**. 
Aplikasi web sederhana ini dibangun menggunakan **Python** dan **Streamlit** untuk memprediksi apakah seorang nasabah layak mendapatkan pinjaman bank atau tidak berdasarkan profil data mereka.

## 🚀 Fitur Utama
- **Prediksi Cepat:** Masukkan data nasabah dan dapatkan hasilnya seketika.
- **Konversi Mata Uang:** Input gaji dalam Rupiah (IDR) otomatis dikonversi ke Dollar (USD) untuk diproses model.
- **UI Ramah Pengguna:** Tampilan dalam Bahasa Indonesia.

## 🛠️ Teknologi yang Digunakan
- **Bahasa:** Python 3.13
- **Framework Web:** Streamlit
- **Machine Learning:** Scikit-Learn (Logistic Regression)
- **Data Handling:** Pandas & Numpy
- **Model Storage:** Pickle (.sav)

## 📂 Struktur Folder
```text
.
├── app.py                # Kode utama aplikasi Streamlit
├── best_loan_model.sav   # Model Machine Learning yang sudah dilatih
├── loanprediction.py     # File pembuatan model
├── train.csv             # Data training model
├── test.csv              # Data test model
├── requirements.txt      # Daftar library yang dibutuhkan
└── README.md             # Dokumentasi project ini

---

## 🛠️ Instalasi & Menjalankan Aplikasi

### 1. Clone Repository
```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
```

### 2. Buat Virtual Environment *(Opsional tapi Disarankan)*
```bash
python -m venv venv
```

#### Aktivasi Virtual Environment
**Windows**
```bash
.\venv\Scripts\activate
```

**Mac / Linux**
```bash
source venv/bin/activate
```

---

### 3. Instalasi Library
Gunakan file `requirements.txt` untuk menginstal semua dependensi sekaligus:
```bash
pip install -r requirements.txt
```

---

### 4. Menjalankan Aplikasi
```bash
streamlit run app.py
```
Setelah itu, aplikasi akan terbuka otomatis di browser.

---

## 📝 Catatan Data
Model Machine Learning pada aplikasi ini dilatih menggunakan **dataset historis pinjaman** dengan fitur-fitur berikut:

### 🔹 Profil Nasabah
- Jenis Kelamin
- Status Pernikahan
- Pendidikan
- Jumlah Tanggungan

### 🔹 Informasi Keuangan
- Gaji Utama
- Gaji Pasangan
- Jumlah Pinjaman

### 🔹 Rekam Jejak & Properti
- Riwayat Kredit
- Lokasi Properti
- 
---


## 👨‍💻 Author
Dibuat oleh **Nanziel** sebagai bagian dari eksplorasi **Machine Learning & Web Deployment**. Feel free to use it! 🎉

---
