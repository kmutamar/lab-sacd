import streamlit as st
from config.setup_page import logo
logo()

# --------------------
# Import halaman model
# --------------------

from riset.korupsi.sch_k import sch_k_show
#from riset.korupsi.sch import show_sech
#from riset.korupsi.sech import show_sech_k

# --------------------
# Database model
# --------------------

riset_model = {
    "Epidemi": [
        "SCH Kontrol",
        #"SECH",
        #"SECH Kontrol"
    ],

    "Predator-Prey": [
        "Alley",
        "Alley+Kontrol"
    ],

    "Nonlinear Control": [
        "IOFL",
        "Backstepping"
    ]

}

# --------------------
# Judul
# --------------------

st.title("Penelitian")

# --------------------
# Topik
# --------------------

topik = st.radio(
    "Pilih Topik",
    list(riset_model.keys()),
    horizontal=True
)

# --------------------
# Daftar model tersedia
# --------------------

st.subheader("Model Tersedia")

for item in riset_model[topik]:
    st.write("* ", item)

# --------------------
# Pilih model
# --------------------

model = st.selectbox(
    "Pilih Model",
    riset_model[topik]
)

st.divider()

# --------------------
# Tampilkan model
# --------------------
if model == "SCH Kontrol":
    sch_k_show()  
#elif model == "SCH Kontrol":
#    sch_k_show()  