import pickle
import streamlit as st

model = pickle.load(open('prediksi_harga_rumah_smg.sav', 'rb'))

st.title("Prediksi Harga Rumah di Kota Semarang")

# Membagi visualisasi menjadi 2 kolom
col1, col2 = st.columns(2)

with col1:
    Jenis_Rumah = st.number_input('Input Jenis Rumah')
with col2:
    Lokasi = st.number_input('Input Lokasi')
with col1:
    KT = st.number_input('Input Jumlah Kamar Tidur')
with col2:
    KM = st.number_input('Input Jumlah Kamar Mandi')
with col1:
    Garasi = st.number_input('Input Garasi')
with col2:
    LT = st.number_input('Input Luas Tanah')
with col1:
    LB = st.number_input('Input Luas Bangunan')
with col2:
    KPR_Bulanan = st.number_input('Input harga KPR bulanan')

predict = ''

if st.button("Prediksi Harga"):
    predict = model.predict(
        [[Jenis_Rumah, Lokasi, KT, KM, Garasi, LT, LB, KPR_Bulanan]]
    )
    st.write("Prediksi Harga Rumah (dalam juta) : ", predict)