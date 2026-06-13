import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from config.setup_page import logo
logo()
print("LOADING Model SCH......")

# --------------------
# import metode dan fungsi
# --------------------
from metode.euler import euler
from model.sir import sir

    
def sch_show():
    #st.page_link("Home.py", label="🏠 Home")
    st.title("Model Susceptible, Corrupt, Honest (SCH)")

    tab1, tab2, tab3 = st.tabs(
        ["Teori", "Analisis", "Simulasi"]
    )

    with tab1:
        st.header('Dalam pengembangan')
        st.markdown(""" Model Dasar Penyebaran Perilaku Korup""")
        st.latex(r'''
        \left\{
        \begin{array}{lcl}
        \dfrac{ds}{dt}&=&-\beta s i\\[12pt]
        \dfrac{di}{dt}&=&\beta s i-\gamma i\\[12pt]
        \dfrac{dr}{dt}&=&\gamma i
        \end{array}
        \right.
        ''')
        st.markdown(r"""
    dengan:

    - $s(t)$ : individu rentan,
    - $i(t)$ : individu korup,
    - $r(t)$ : individu sadar,

    serta parameter $\beta,\gamma \in \mathbb{R}^{+}.$
    """)

    with tab2:
        st.header('Dalam pengembangan')
        st.header("Titik Ekuilibrium")
        st.markdown(r""" Titik ekuilibrium bebas penyakit adalah
        $$
        x_e=\left(\dfrac{\Gamma}{\psi},0,0\right)
        $$
           
        """)
        st.header("Bilangan Reproduksi")
        st.markdown(r""" Bilangan reproduksi untuk masalah ini adalah
        $$
        R_0=\dfrac{\kappa}{\mu(\beta+\mu)}
        $$
           
        """)
        st.header("Kestabilan DFE")
      

    with tab3:
        tf=50
        t=np.linspace(0,tf,tf*int(1e2))
        #beta = st.number_input(r"$\beta$ = ",value=0.2)
        #gamma = st.number_input(r"$\gamma$ = ",value=0.1)
        
        col1, col2 = st.columns(2)
        with col1:
            beta = st.slider(
                r"$\beta$",
                min_value=0.0,
                max_value=0.9,
                value=0.4,
                step=0.01
            )
        with col2:
            gamma = st.slider(
                r"$\gamma$",
                min_value=0.0,
                max_value=0.9,
                value=0.2,
                step=0.01
            )
        #s0 = st.number_input("S(0)",value=0.9)
        i0 = st.number_input(r"$I(0)$",value=0.1)
        r0=0
        s0=1-i0
        y=euler(sir,[s0,i0,r0],t,[beta,gamma])   
        st.header("Model SIR Dasar")
        fig, ax = plt.subplots(figsize=(4,2))
        ax.plot(t,y[:,0],'b-',label='S(t)')
        ax.plot(t,y[:,1],'r-',label='I(t)')
        ax.plot(t,y[:,2],'m-',label='R(t)')
        ax.set_xlabel("waktu")
        ax.set_ylabel("populasi")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
        _="""
        if st.button("Proses"):
            t=np.linspace(0,tf,tf*int(1e2))
            y=euler(sir,[s0,i0,r0],t,[beta,gamma])   
            st.header("Model SIR Dasar")
            fig, ax = plt.subplots(figsize=(4,2))
            ax.plot(t,y[:,0],'b-',label='S(t)')
            ax.plot(t,y[:,1],'r-',label='I(t)')
            ax.plot(t,y[:,2],'m-',label='R(t)')
            ax.set_xlabel("waktu")
            ax.set_ylabel("populasi")
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)
        """
           