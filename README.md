# 🏦 Sistem Prediksi Kelayakan Pinjaman Bank

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](MASUKKAN_LINK_STREAMLIT_KAMU_DISINI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Hai fella! 👋 Selamat datang di project **Loan Prediction App**. 
Aplikasi web sederhana ini dibangun menggunakan **Python** dan **Streamlit** untuk memprediksi apakah seorang nasabah layak mendapatkan pinjaman bank atau tidak berdasarkan profil data mereka.

## 🚀 Fitur Utama
- **Prediksi Real-Time:** Masukkan data nasabah dan dapatkan hasilnya seketika.
- **Konversi Mata Uang:** Input gaji dalam Rupiah (IDR) otomatis dikonversi ke Dollar (USD) untuk diproses model.
- **Data Preprocessing Otomatis:** Menggunakan Scikit-Learn Pipeline untuk menangani data kosong (Imputation) dan mengubah teks ke angka (Encoding) secara otomatis.
- **UI Ramah Pengguna:** Tampilan bersih dan dalam Bahasa Indonesia.

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
├── requirements.txt      # Daftar library yang dibutuhkan
└── README.md             # Dokumentasi project ini
