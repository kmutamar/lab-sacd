import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from config.setup_page import logo
logo()

from metode.dichotomous_PON import dichotomous_pon
from fungsi.fungsi_error_zakat import fungsi_error_zakat

# --------------------
# import metode dan fungsi
# --------------------
print("LOADING project kuliah...")

data = np.loadtxt(
    "data/dataZakat2.txt",
    skiprows=1
)
data_t=data[:,0]
data_f=data[:,1]
df = pd.DataFrame(
    data,
    columns=["Waktu","Penerimaan"]
)




st.title("Project Kuliah : Kurva Fitting Data Zakat")
tab1, tab2, tab3 = st.tabs(
    ["Data", "Pola", "Simulasi"]
)

with tab1:
    st.title("Data dan Kurva")
    st.header('Data')
    #st.table(df)
    st.dataframe(df)
    
    
    st.divider()
    st.header('Kurva')
    fig, ax = plt.subplots(figsize=(6,4))

    ax.plot(data_t,data_f,'or',label='Data')
    #ax.plot(data_t,fungsi_tebakan,'-b',label='Model')

    ax.set_xlabel('Waktu')
    ax.set_ylabel('Zakat')
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)
    st.divider()
    

with tab2:
    st.write('Kurva data menunjukkan bahwa fungsi mengikuti pola eksponensial')
    st.markdown(r"""
        Fungsi yang dipilih adalah
        $$ f(t)=K\exp{(at)}$$
        dengan $K,a$ adalah parameter yang perlu dicari berdasarkan data. 
        Oleh karena ada dua parameter, sementara metode dichotomous hanya untuk optimisasi peubah tunggal,
        maka nilai $K$ ditentukan secara manual. 
    """)
    
    st.markdown(r"""
        Penentuan $K$ digunakaan dari kondisi $t=0$. 
        Kondisi ini mengasumsikan di titik awal, hampiran dan data bernilai sama.
        Menggunakan $t=0$ diperoleh
        $$
        f(0)=K=68.39
        $$
        Jadi, nilai $K$ yang dipakai adalah $K=68.39$
    
    """)

with tab3:
    st.markdown(r"""
        Simulasi dilakukan menggunakan dichotomous, dengan parameter:
        $$
        \begin{array}{lll}
            interval &:& [0,10]\\
            tolmax &:& 1e-6\\
        \end{array}
        $$
    """)
    hasil=dichotomous_pon(fungsi_error_zakat,[0,10],1e-6,data_t,data_f)
    a=hasil[0]
    st.divider()
    st.metric('Nilai a = ',a)
    st.write('Hampiran = 68.39 exp(',a,'t)')
    def f_tebakan(k,a,t):
        return k*np.exp(a*t)
    k=68.39
    t=np.arange(0,20)
    fungsi_tebakan=f_tebakan(k,a,t)
    
    fig, ax = plt.subplots(figsize=(6,4))

    ax.plot(data_t,data_f,'or',label='Data')
    ax.plot(data_t,fungsi_tebakan,'-b',label='Model')

    ax.set_xlabel('Waktu')
    ax.set_ylabel('Zakat')
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)    
        
               


