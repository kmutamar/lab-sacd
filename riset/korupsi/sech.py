import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from metode.euler import euler
from metode.euler import sir


# configurasi dan icon
st.set_page_config(
    page_title="SACD-Labs",
    page_icon="assets/LOGO-SACD.png",
    layout="wide"
)

st.page_link("Home.py", label="🏠 Home")

st.title("Model Dasar")

tab1, tab2, tab3 = st.tabs(
    ["Teori", "Analisis", "Simulasi"]
)

with tab1:
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
    st.write("Analisis model")

with tab3:
    beta = st.number_input(r"$\beta$ = ",value=0.2)
    gamma = st.number_input(r"$\gamma$ = ",value=0.1)
    #s0 = st.number_input("S(0)",value=0.9)
    i0 = st.number_input(r"$I(0)$",value=0.1)
    r0=0
    s0=1-i0
    if st.button("Proses"):
        t=np.linspace(0,20,1000)
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
        
               


