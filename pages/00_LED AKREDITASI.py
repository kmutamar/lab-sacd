import streamlit as st
import streamlit.components.v1 as components

# Membuat judul atau subjudul di halaman Streamlit
st.title("Portal Monitoring Akreditasi")
st.markdown("### Progres Kendali LED LAMSAMA 3.1")
st.write("Dashboard ini terhubung langsung dengan form kendali tim akreditasi dan diperbarui secara otomatis.")

# Ganti teks di dalam tanda kutip di bawah ini dengan link yang Anda salin dari Looker Studio
looker_url = "https://datastudio.google.com/embed/reporting/eb30a5c0-0a6a-4256-9974-ed556bccc813/page/QSU4F"

# Menampilkan Looker Studio menggunakan iframe
components.iframe(looker_url, width=1000, height=800, scrolling=True)