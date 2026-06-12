import streamlit as st

def logo():
    st.set_page_config(
        page_title="SACD-Labs",
        page_icon="assets/LOGO-SACD.png",
        layout="wide"
    )
    
_ = """
st.write(os.getcwd())
st.write(os.listdir("."))
st.write(os.listdir("./pages"))
"""

_ = """
# menambah navigasi
st.sidebar.success("Navigasi")    
"""

#st.page_link("Home.py", label="🏠 Home")