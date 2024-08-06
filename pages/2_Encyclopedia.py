import streamlit as st
from Home import button_style, logo
import pandas as pd

st.set_page_config(page_title="Encyclopedia", layout="centered", page_icon=logo)
st.markdown(button_style, unsafe_allow_html=True)
logo_sidebar_style = """<style>
    img[data-testid="stLogo"] {
        height: 2rem !important;
    }
</style>"""
st.markdown(logo_sidebar_style, unsafe_allow_html=True)
st.logo("./assets/logo-with-inline-text-brightened.png", icon_image="./assets/logo-only-no-bg-brightened.png")


st.markdown("# Slang Encyclopedia")
st.markdown("*Powered by :blue[GenLingo]*")

df = pd.read_csv("dataset/dataset-encyclopedia.csv", dtype=str).fillna("")

# Make slangs lowercase so that users can search without case sensitive keywords
slangs = df['Slang'].apply(lambda x : x.lower())

text_search = st.text_input("Search slangs by name", value="")

# Filter by keyword
mask = slangs.str.contains(text_search.lower())
df_search = df[mask]

if df_search.empty:
    st.markdown(f"### Sorry, there are currently no slangs with :blue[{text_search}] in our Encyclopedia 🙏")
    st.markdown("Refer to our :blue[GenLingo Bot] for the latest update on Gen Z and Gen Alpha language.")
    if st.button('Chat with GenLingo Bot'):
        st.switch_page('./pages/1_GenLingo.py')

# Dsiplay neatly with cards (3 per row)
N_cards_per_row = 3
if text_search:
    for n_row, row in df_search.reset_index().iterrows():
        i = n_row%N_cards_per_row
        if i==0:
            st.write("---")
            cols = st.columns(N_cards_per_row, gap="large")
        with cols[n_row%N_cards_per_row]:
            st.caption(f"Gen {row['Gen'].strip()}")
            st.markdown(f"**{row["Slang"]} :**")
            st.markdown(f"*{row['Meaning'].strip()}*")
