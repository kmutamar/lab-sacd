import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from config.setup_page import logo
logo()

from metode.lm_jacobian import func_lm_jacobian
from metode.lm_ls import func_lm_ls
from fungsi.lm_residu import func_lm_residu


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
tab1, tab2, tab3 , tab4 = st.tabs(
    ["Data", "Pola", "Simulasi Estimasi","Simulasi Fungsi"]
)

with tab1:
    st.title("Data dan Kurva")
    st.write("""**Sumber data**:  Ria Indah Sari, 
    Tomi Z., 
    Era Napra Tilopa Sihombing, Mahiroh, Rado Yendra, Arisman Adnan, 
    The Analysist Impacts of Covid-19 on Zakat, Revenue in Indonesia using an Exponential, Smoothing Model, 
    *International Journal of Mathematics Trends and Technology*, 
    Vol 68, Issue 5, 2022.
   """)
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
    """)
    
    st.markdown(r"""
        Penentuan $K$ dan $a$ menggunakan metode Levenberg-Marquardt.
    
    """)
    
    st.markdown(r"""
        Fungsi error yang digunakan adalah jumlahan kuadrat error,
        $$
            E=\dfrac{1}{n}\sum\limits_{i=1}^{n}{(K\exp{(at_i)}-d_i)^2}
        $$
        dengan $d_i$ adalah data ke-$i$ dan $n$ adalah banyak data.
    """)

with tab3:
    st.header("Levenberg-Marquardt")
    st.divider()
    st.header("Parameter")

    K0 = st.slider(
        "Nilai awal K",
        min_value=1.0,
        max_value=500.0,
        value=90.00,
        step=1.0
    )

    a0 = st.slider(
        "Nilai awal a",
        min_value=-2.0,
        max_value=2.0,
        value=0.40,
        step=0.01
    )

    lambda_lm = st.slider(
        "Lambda",
        min_value=0.001,
        max_value=1.0,
        value=0.80,
        step=0.001
    )
    
    hasil=func_lm_ls(func_lm_jacobian,
        func_lm_residu,
        datat=data_t,
        datay=data_f,
        itmax=500,
        tolmax=1e-8,
        lambd=lambda_lm,
        init=[K0,a0]
)
    iterasi, param, fx, waktu = hasil
    st.divider()
    st.header("Hasil Simulasi")    
    st.metric('Iterasi = ',iterasi)
    st.metric('Nilai K = ',param[0])
    st.metric('Nilai a = ',param[1])
    
    st.write('Hampiran = ',param[0],' exp(',param[1],'t)')
    #st.metric('Nilai error = ',func_lm_residu(data_t,data_f,param[0],param[1]))
    res = func_lm_residu(
        data_t,
        data_f,
        param[0],
        param[1]
    )

    error = float(0.5*(res.T @ res))

    st.metric(
        'Nilai Error',
        f'{error:.6e}'
    )

    st.divider()
    st.header('Perbandingan data dan hampiran')
    def f_tebakan(k,a,t):
        return k*np.exp(a*t)
    t=np.arange(0,20)
    fungsi_tebakan=f_tebakan(param[0],param[1],t)
    fig, ax = plt.subplots(figsize=(6,4))

    ax.plot(data_t,data_f,'or',label='Data')
    ax.plot(data_t,fungsi_tebakan,'-b',label='Model')

    ax.set_xlabel('Waktu')
    ax.set_ylabel('Zakat')
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)    
        
with tab4:
    st.title("dalam pengembangan")


