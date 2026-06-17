import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
# Menyiapkan vektor warna
def gambar(x,n,akar,domain,tolmax):
    #x2=np.reshape(x,[n*n,1])
    #x2c=np.zeros([n*n,1])
    #for i in range(0,np.shape(akar)[0]):
    #    x2c[abs(x2-akar[i])<=tolmax]=i+1
    #x2c=np.reshape(x2c,[n,n])
    x2=np.reshape(x,[n*n])
    akar_np = np.array(akar)
    jarak = np.abs(x2[:,None] - akar_np[None,:])
    x2c = np.argmin(jarak,axis=1)+1
    x2c = np.reshape(x2c,[n,n])
    
    # tampil gambar
    fig, ax = plt.subplots(figsize=(6,4))
    ax.imshow(x2c,cmap='jet',extent=domain)
    ax.set_xlabel('$Re{(x)}$')
    ax.set_ylabel('$Im{(x)}$')
    ax.grid(True)
    #ax.legend()
    st.pyplot(fig)      