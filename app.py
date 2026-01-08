import streamlit as st

st.title("Aplikasi Nilai Siswa")

nama = st.text_input("Nama Siswa")
nilai = st.number_input("Nilai", 0, 100)

if st.button("Cek Hasil"):
    if nilai >= 75:
        st.success(f"{nama} TUNTAS")
    else:
        st.error(f"{nama} BELUM TUNTAS")
