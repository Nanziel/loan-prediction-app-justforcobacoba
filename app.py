import streamlit as st
import pandas as pd
import pickle

# 1. Load Model "Robot" kamu
model = pickle.load(open('best_loan_model.sav', 'rb'))

st.title("Aplikasi Prediksi Kelayakan Pinjaman 🏦")
st.write("Silakan lengkapi formulir di bawah ini untuk menganalisis peluang persetujuan pinjaman nasabah.")
# 2. Buat Inputan (Pastikan urutan kolom sesuai dengan training)
col1, col2 = st.columns(2)

with col1:
    # Kita tampilkan Bahasa Indonesia, tapi simpan pilihan dalam variabel yang model pahami
    gender_ui = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    gender = "Male" if gender_ui == "Laki-laki" else "Female"
    
    married_ui = st.selectbox("Status Pernikahan", ["Sudah Menikah", "Belum Menikah"])
    married = "Yes" if married_ui == "Sudah Menikah" else "No"
    
    dependents = st.number_input("Jumlah Tanggungan (Anak/Keluarga)", min_value=0, max_value=10, step=1)
    
    edu_ui = st.selectbox("Pendidikan Terakhir", ["Sarjana (S1/D4)", "Bukan Sarjana"])
    education = "Graduate" if edu_ui == "Sarjana (S1/D4)" else "Not Graduate"
    
    self_emp_ui = st.selectbox("Pekerjaan Mandiri / Wiraswasta?", ["Ya", "Tidak"])
    self_employed = "Yes" if self_emp_ui == "Ya" else "No"

with col2:
    # --- PENGATURAN KURS ---
    KURS_USD = 16000 # Misal: 1 USD = Rp 16.000
    
    # --- PENDAPATAN PEMOHON ---
    income_idr = st.number_input("Pendapatan Bulanan Anda (Rp)", min_value=0, step=100000)
    # Konversi ke USD untuk Model
    applicant_income = income_idr / KURS_USD
    st.caption(f"Estimasi: ${applicant_income:,.2f} USD")

    # --- PENDAPATAN PASANGAN ---
    co_income_idr = st.number_input("Pendapatan Bulanan Pasangan/Tambahan (Rp)", min_value=0, step=100000)
    coapplicant_income = co_income_idr / KURS_USD
    st.caption(f"Estimasi: ${coapplicant_income:,.2f} USD")

    # --- JUMLAH PINJAMAN ---
    loan_idr = st.number_input("Jumlah Pinjaman yang Diajukan (Rp)", min_value=0, step=1000000)
    # Catatan: Jika model kamu dilatih dengan satuan ribuan dollar, bagi lagi dengan 1000
    # Contoh: loan_amount = (loan_idr / KURS_USD) / 1000
    loan_amount = loan_idr / KURS_USD
    st.caption(f"Estimasi: ${loan_amount:,.2f} USD")
    
    # --- DURASI PINJAMAN ---
    # Jangka waktu tetap dalam satuan hari sesuai data training
    loan_term = st.selectbox("Durasi Pinjaman (Hari)", [360, 180, 120, 84, 60, 36, 12])

    # --- RIWAYAT KREDIT ---
    credit_desc = st.selectbox("Catatan Kredit Sebelumnya", ["Pernah Pinjam & Lancar", "Belum Pernah / Macet"])
    credit_history = 1.0 if credit_desc == "Pernah Pinjam & Lancar" else 0.0

    # --- AREA PROPERTI ---
    prop_ui = st.selectbox("Lokasi Tempat Tinggal / Aset", ["Perkotaan (Urban)", "Pinggir Kota (Semi-Urban)", "Pedesaan (Rural)"])
    property_area = "Urban" if prop_ui == "Perkotaan (Urban)" else "Semiurban" if prop_ui == "Pinggir Kota (Semi-Urban)" else "Rural"

# 3. Proses Prediksi
if st.button("Cek Kelayakan"):
    # Susun data input jadi DataFrame (Harus sama persis urutannya dengan X_train)
    input_data = pd.DataFrame([{
        'Gender': gender, 'Married': married, 'Dependents': dependents,
        'Education': education, 'Self_Employed': self_employed,
        'ApplicantIncome': applicant_income, 'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount, 'Loan_Amount_Term': loan_term,
        'Credit_History': credit_history, 'Property_Area': property_area
    }])
    
    # MAGIC HAPPENS HERE:
    # Model otomatis melakukan encoding dan imputing di dalam sini!
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success("Selamat! Pinjaman Kemungkinan Besar DISETUJUI ✅")
    else:
        st.error("Mohon Maaf, Pinjaman Kemungkinan Besar DITOLAK ❌")