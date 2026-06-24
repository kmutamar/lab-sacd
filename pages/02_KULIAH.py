import streamlit as st
from config.setup_page import logo
logo()


# --------------------
# Import halaman model
# --------------------

from kuliah.numerik.rf_newton import rf_newton_show
from kuliah.pemodelan.sir import sir_show

# --------------------
# Database materi
# --------------------

kuliah = {

    "Numerik": [

        "Newton",
        "Interpolasi",
        "Integral Numerik",
        "Turunan Numerik"
    ],

    "Optimisasi": [
        "Golden Section",
        "Gauss Newton"

    ],

    "Pemodelan": [
        "SIR",
        "Eksponensial",
        "Predator-Prey"
    ]

}

# --------------------
# Judul
# --------------------

st.title("Pengajaran")

# --------------------
# Topik
# --------------------

topik = st.radio(
    "Pilih Kuliah",
    list(kuliah.keys()),
    horizontal=True
)

# --------------------
# Daftar model tersedia
# --------------------

st.subheader("Materi yang tersedia")

for item in kuliah[topik]:
    st.write("* ", item)

# --------------------
# Pilih materi perkuliahan
# --------------------

materi = st.selectbox(
    "Pilih Materi",
    kuliah[topik]
)

st.divider()

# --------------------
# Tampilkan materi
# --------------------
if materi == "Newton":
    rf_newton_show()
elif materi == "SIR":
    sir_show()   