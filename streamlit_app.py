import streamlit as st

# Set the page configuration
st.set_page_config(page_title="AlertMinds")

# Automatically redirect to /Home
st.markdown("""
    <meta http-equiv="refresh" content="0; url=/Home">
""", unsafe_allow_html=True)


