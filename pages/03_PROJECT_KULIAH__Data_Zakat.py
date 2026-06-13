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
    st.title("Disini halaman data dan kurva")
    #st.write(newton)

    fig, ax = plt.subplots(figsize=(6,4))

    ax.plot(data_t,data_f,'or',label='Data')
    #ax.plot(data_t,fungsi_tebakan,'-b',label='Model')

    ax.set_xlabel('Waktu')
    ax.set_ylabel('Zakat')
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)
    
    #st.table(df)
    st.dataframe(df)

with tab2:
    st.title("Disini halaman pendekatan")
    #st.write(newton)

with tab3:
    hasil=dichotomous_pon(fungsi_error_zakat,[0,10],1e-6,data_t,data_f)
    a=hasil[0]
    st.write('a = ',a)
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
        
               


