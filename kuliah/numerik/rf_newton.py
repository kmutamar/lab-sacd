import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from config.setup_page import logo
logo()

# --------------------
# import metode dan fungsi
# --------------------
from metode.root_finding import newton
from fungsi.fpt import f1 as f
from fungsi.fpt import f1 as df
print("LOADING materi newton...")





def rf_newton_show():
    st.title("Metode Newton")
    tab1, tab2, tab3 = st.tabs(
        ["Overview", "Metode", "Simulasi"]
    )

    with tab1:
        st.title("Disini halaman ringkasan")
        #st.write(newton)

    with tab2:
        st.markdown(r""" 
        Diberikan fungsi $f(x)$. 
        Metode Newton untuk menentukan akar solusi $f(x)=0$ diberikan oleh
        $$
        x_{n+1}=x_{n}-\dfrac{f(x_n)}{f'(x_n)}
        $$
        dengan $x_0$ adalah tebakan awal, $n=0,1,2,\ldots,N-1$, dan $N$ adalah iterasi maksimum.
        
        Iterasi dijalankan sampai kriteria tertentu
        1. Iterasi maksimum $N$ tercapai
        2. Nilai fungsi lebih kecil dari toleransi maksimum, $|f(x_{n+1})|<\mathrm{tolmax}$
        2. Nilai turunan fungsi lebih kecil dari toleransi maksimum, $|f'(x_{n+1})|<\mathrm{tolmax}$
        """ )

    with tab3:
        st.markdown("""
        Diberikan fungsi $f(x)=x^2-3x+2$ yang akar analitiknya adalah $x_1=1$ dan $x_2=2$. 
        Menggunakan metode Newton, akan ditentukan nilai akar secara numerik.
        
        """)
        init = st.number_input("Tebakan Awal",value=10.0)
        tolmax = st.number_input("Toleransi (default:1e-10)",value=1e-10,format="%.12f")
        itmax = st.number_input("Iterasi Maksimum (default:1000)",value=1000)
        animasi = st.checkbox("Tampilkan Animasi")
        if st.button("Proses"):
            if animasi:
                iter,sol,waktu=newton(f,df,init,itmax,tolmax)
                placeholder = st.empty()
                for k in range(len(sol)):
                    fig,ax = plt.subplots(figsize=(4,3))
                    xx = np.linspace(0,init,500)
                    yy = f(xx)
                    ax.plot(xx,yy)
                    ax.axhline(0,color='k')
                    ax.plot(sol[:k+1],f(sol[:k+1]),'ro')
                    ax.set_title(f"Iterasi {k}")
                    placeholder.pyplot(fig)
                    time.sleep(0.5) 
                    
            iter,sol,waktu=newton(f,df,init,itmax,tolmax)       
            st.header("Hasil Simulasi")
            st.metric("Iterasi = ",iter)
            st.metric("Akar    = ",sol[-1])
            st.metric("Nilai fungsi    = ",f"{f(sol[-1]):.5e}")
            st.metric("Nilai turunan   = ",f"{df(sol[-1]):.5e}")
            st.metric("Waktu (detik)   = ",f"{waktu:.3e}")
            
            st.header("Kurva Iterasi")
            fig, ax = plt.subplots(figsize=(4,2))
            ax.plot(range(len(sol)),sol,marker='o',color='red')
            ax.set_xlabel("Iterasi")
            ax.set_ylabel("x")
            ax.grid(True)
            st.pyplot(fig)
        
               


