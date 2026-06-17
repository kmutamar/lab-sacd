import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from config.setup_page import logo
logo()

from kuliah.project.basin.fungsi1 import (
    f as f1,
    df as df1,
    d2f as d2f1,
    akar as akar1)
from kuliah.project.basin.fungsi2 import (
    f as f2,
    df as df2,
    d2f as d2f2,
    akar as akar2)
from kuliah.project.basin.gambar import gambar
from kuliah.project.basin.newton_basin import newton_basin_func
from kuliah.project.basin.halley_basin import halley_basin_func
from kuliah.project.basin.newton_GM_basin import newton_gm_basin_func
from kuliah.project.basin.newton_AM_basin import newton_am_basin_func


# --------------------
# import metode dan fungsi
# --------------------
print("LOADING project basin...")

st.title("Project Kuliah : Basin Metode Newton")
st.markdown(r"""
    Fungsi yang dipakai dalam simulasi adalah
    $$
    f(x)=x^4-1
    $$
    dengan $x\in\mathcal{C}$, yang akar analitiknya adalah
    $$
    \alpha=\{1,1,-i,i\}.
    $$
    
    Simulasi dilakukan dengan metode Newton
    $$
    x_{n+1}=x_{n}-\dfrac{f(x_n)}{f'(x_n)}
    $$
    dengan $n=0,1,2,\ldots,M$, dimana $M$ adalah iterasi maksimum, 
    dan $x_0$ adalah tebakan awal. 
    
    $x_0$ diambil dari area $[-1,-1]\times [-i,i]$ 
    dengan partisi $n=1000\times 1000$. Iterasi maksimum adalah $1000$
    sementara toleransi maksimum adalah $1e-30$.


""")

st.divider()
st.header('Simulasi membutuhkan proses, harap tunggu....')

    
# simulasi
itmax=40
tolmax=1e-100
# Mendefinisikan area
a=-0.5
b=0.5
n=1000

with st.container(border=True):
    st.subheader("Konfigurasi Basin")
    col1, col2 = st.columns(2)
    with col1:
        fungsi = st.radio(
            "Fungsi",
            [
                r"$z^4-1$",
                r"$z^6-1$"
            ]
        )
    with col2:
        metode = st.radio(
            "Metode",
            [
                "Newton",
                "Halley",
                "AM-Newton",
                "GM-Newton",
            ]
        )

#--- proses 
if st.button("Proses Basin"):
    # pilih fungsi
    if fungsi == r"$z^4-1$":
        f=f2
        df=df2
        d2f=d2f2
        akar=akar2
    else:
        f=f1
        df=df1
        d2f=d2f1
        akar=akar1
    # metode
    if metode == "Newton":
        sol,waktu=newton_basin_func(f,df,a,b,n,tolmax,itmax)
    elif metode=="Halley":
        sol,waktu=halley_basin_func(f,df,d2f,a,b,n,tolmax,itmax)        
    elif metode=="AM-Newton":
        sol,waktu=newton_am_basin_func(f,df,a,b,n,tolmax,itmax)
    else:
        sol,waktu=newton_gm_basin_func(f,df,a,b,n,tolmax,itmax)
    
    st.write('partisi = ',np.shape(sol))
    st.write('waktu komputasi = ',waktu)
    # gambar
    # Memanggil fungsi gambar
    domain=[a,b,a,b]
    gambar(sol,n,akar,domain,tolmax)
    
    
  
