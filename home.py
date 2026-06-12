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
tabhome, tabVMT, tabriset,tabMK,tabmhs = st.tabs(
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
