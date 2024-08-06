import streamlit as st
from Home import button_style, logo

st.set_page_config(page_title="Encyclopedia", layout="centered", page_icon=logo)
st.markdown(button_style, unsafe_allow_html=True)
logo_sidebar_style = """<style>
    img[data-testid="stLogo"] {
        height: 2rem !important;
    }
</style>"""
st.markdown(logo_sidebar_style, unsafe_allow_html=True)
st.logo("./assets/logo-with-inline-text-brightened.png", icon_image="./assets/logo-only-no-bg-brightened.png")