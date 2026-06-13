import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from config.setup_page import logo
logo()

# --------------------
# import metode dan fungsi
# --------------------
print("LOADING project kuliah...")





st.title("Project Kuliah : Kurva Fitting Data Zakat")
tab1, tab2, tab3 = st.tabs(
    ["Data", "Pola", "Simulasi"]
)

with tab1:
    st.title("Disini halaman data dan kurva")
    #st.write(newton)

with tab2:
    st.title("Disini halaman pendekatan")
    #st.write(newton)

with tab3:
    st.title("Disini halaman simulasi pendekatan linier")
    #st.write(newton)
        
               


