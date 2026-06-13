import streamlit as st
import os
from config.setup_page import logo
logo()
#-------------------
st.title("System Analysis & Control Design Laboratory")
st.subheader("Jurusan Matematika, FMIPA, Universitas Riau")
st.image("assets/LOGO-SACD.PNG",width=200)
#-------------------
st.divider()
tabhome,tabVMT,tabriset,tabMK,tabmhs = st.tabs(
    ["Home", "Visi-Misi", "Riset" ,"Pengajaran","Mahasiswa"]
)


with tabhome:
    st.title("Selamat datang di platform riset berbasis website")
    st.subheader("System Analysis & Control Design")
    st.write("""
    
        Jurusan Matematika,
        
        Fakultas Matematika dan Ilmu Pengetahuan Alam,
        
        Universitas Riau
    """)
    
    
    
    st.write("""
        Dikelola oleh Dr. Khozin Mu'tamar
    """)
with tabMK:
    st.title("Bidang Pengajaran")
    st.header("Jenjang Sarjana")
    st.write("1. Pengantar kontrol linier")
    st.write("2. Pengantar optimisasi numerik")
    st.write("3. Pemodelan Matematika")
    st.write("4. Persamaan diferensial biasa")
    st.write("5. Masalah nilai batas")
    st.write("xxx. xxx")
    st.write("xxx. xxx")
    
    st.divider()
    st.header("Jenjang Magister")
    st.write("1. Teori Kontrol Optimum")
    st.write("2. Teori Kontrol Taklinier")
    
    st.divider()
    st.header("Layanan")
    st.write("1. Matematika I Teknik")
    st.write("2. Matematika II Teknik")
    st.write("3. Matematika III Teknik")
    st.write("4. Matematika IV Teknik")
    st.write("5. Kalkulus Teknik")
    st.write("6. Matematika Dasar FMIPA")

with tabriset:
    st.title("Bidang Riset")
    st.header("1. Kontrol Adaptive dan Taklinier")
    st.write("a. IOFL")
    st.write("b. Sistem fase takminimum")
    st.write("c. Sistem dengan parameter takpasti")
    st.write("d. Backstepping")
    st.write("e. Kontrol Lyapunov/Sontag Formula")
    st.write("f. Sliding mode control")
    st.write("g. Implementasi kontrol taklinier ke epidemik")
    
    st.divider()
    st.header("2. Pemodelan")
    st.write("a. Predator-Prey")
    st.write("b. Model Epidemi")

    st.divider()
    st.header("3. Minor")
    st.write("a. Metode numerik")
    st.write("b. Optimisasi numerik")
    st.write("c. Optimisasi heuristik (PSO)")