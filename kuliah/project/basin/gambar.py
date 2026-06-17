import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def gambar(x,n,akar,domain,tolwarna=1e-8):
    x2 = x.ravel()
    akar_np = np.array(akar)
    jarak = np.abs(x2[:,None] - akar_np[None,:])
    # akar terdekat
    idx = np.argmin(jarak,axis=1)
    # jarak minimum
    mindist = np.min(jarak,axis=1)
    # warna awal = 0
    x2c = np.zeros(len(x2),dtype=int)

    # hanya yang cukup dekat akar
    mask = mindist < tolwarna
    x2c[mask] = idx[mask] + 1

    # kembali ke matriks
    x2c = np.reshape(x2c,[n,n])

    # colormap diskrit
    cmap = ListedColormap([
        'black',     # gagal konvergen
        'red',
        'green',
        'blue',
        'yellow',
        'cyan',
        'magenta',
        'orange'
    ])

    # gambar
    fig, ax = plt.subplots(figsize=(6,6))

    ax.imshow(
        x2c,
        cmap=cmap,
        extent=domain,
        origin='lower'
    )

    ax.set_xlabel(r'$Re(z)$')
    ax.set_ylabel(r'$Im(z)$')
    ax.grid(False)
    st.pyplot(fig)