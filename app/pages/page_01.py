import streamlit as st

st.write('This is page 1')

spell = st.secrets['spell']
key = st.secrets.some_magic_api.key

st.write(f"Key: {key}")