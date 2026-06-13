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
from model.schk import schk

def sch_k_show():
    #st.page_link("Home.py", label="🏠 Home")
    st.title("Model SCH dengan kontrol parameter")

    tab1, tab2, tab3 = st.tabs(
        ["Teori", "Analisis", "Simulasi"]
    )

    with tab1:
        st.markdown(""" Model Dasar Penyebaran Perilaku Korup""")
        st.latex(r'''
        \left\{
        \begin{array}{lcl}
        \dfrac{ds}{dt}&=&\Gamma-(1-u)\kappa c s-\mu s+\omega h\\[12pt]
        \dfrac{dc}{dt}&=&(1-u)\kappa c s-\beta c-\mu c\\[12pt]
        \dfrac{dh}{dt}&=&\beta c-(\mu+\omega)*h
        \end{array}
        \right.
        ''')
        st.markdown(r"""
            dengan:

            - $s(t)$ : individu rentan,
            - $c(t)$ : individu korup,
            - $h(t)$ : individu sadar,
            - $u$    : parameter kontrol pencegahan,
            """)

    with tab2:
        st.header("Dalam Pengembangan")
        st.markdown(r"""
        Bilangan reproduksi model ini adalah
        $$
        R_0=\dfrac{(1-u1)\kappa\Gamma}{\mu(\beta+\mu)}
        $$
        
        """)

    with tab3:   
        st.markdown(r"""
            Simulasi dilakukan dengan parameter berikut:
            - $\Gamma$ : $50$
            - $\kappa$ : $0.000234$
            - $\mu$    : $0.0160$
            - $\omega$ : $0.0021$
            - $\beta$  : $0.07$
            """)
        Gamma = 50
        kappa = 0.000234
        mu = 0.0160
        omega = 0.0021
        beta = 0.07
        s0 = 3125
        #i0 = 100
        r0 = 100

        col1, col2 = st.columns([1,2])
        with col1:
            i0 = st.slider(
                r"$I(0)$",
                min_value=0.1,
                max_value=100.00,
                value=1.00,
                step=0.5
            )        
            u1 = st.slider(
                r"$u_1$",
                min_value=0.00,
                max_value=1.00,
                value=0.2,
                step=0.01
            )
            u2 = st.slider(
                r"$u_2(t)$",
                min_value=0.00,
                max_value=1.00,
                value=0.8,
                step=0.01
            )
            tf = st.slider(
                r"$t_f$",
                min_value=1,
                max_value=100,
                value=10,
                step=1
            )
        t=np.linspace(0,tf,tf*int(1e2)) 
        R01=(1-u1)*kappa*Gamma/(mu*(beta+mu))
        R02=(1-u2)*kappa*Gamma/(mu*(beta+mu))
        
        y1=euler(schk,[s0,i0,r0],t,[Gamma,kappa,mu,omega,beta,u1])   
        y2=euler(schk,[s0,i0,r0],t,[Gamma,kappa,mu,omega,beta,u2])   
        
        st.write(r"""$R_0 (u_1)=$""",R01)
        st.write(r"""$R_0 (u_2)=$""",R02)
        #
        with col2:
            fig, ax = plt.subplots(figsize=(4,2))
            ax.plot(t,y1[:,1],'b-',label='u_1')
            ax.plot(t,y2[:,1],'r-',label='u_2')
            ax.set_xlabel("waktu")
            ax.set_ylabel("I(t)")
            ax.legend()
            ax.grid(True)
            fig.tight_layout()
            st.pyplot(fig)
        
               


