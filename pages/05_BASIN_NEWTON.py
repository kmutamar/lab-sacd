import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from config.setup_page import logo
logo()

from kuliah.project.basin.fungsi2 import f,df,akar
from kuliah.project.basin.gambar import gambar
from kuliah.project.basin.newton_basin import newton_basin_func


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
tolmax=1e-30
# Mendefinisikan area
a=-1.5
b=1.5
n=1000
sol,waktu=newton_basin_func(f,df,a,b,n,tolmax,itmax)
st.write('partisi = ',np.shape(sol))
st.write('waktu komputasi = ',waktu)
# gambar
# Memanggil fungsi gambar
domain=[a,b,a,b]
gambar(sol,n,akar,domain,tolmax)
    
    
  