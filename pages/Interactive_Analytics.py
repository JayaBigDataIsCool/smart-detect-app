import streamlit as st
import os

def load_css():
    css_file = os.path.join(os.path.dirname(__file__), '../styles.css')
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def render():
    load_css()

    st.markdown("""
        <div class="main-container">
            <h1>Interactive Analytics</h1>
            <h2>Discover insights effortlessly by talking directly to your data.</h2>
            <div class="card-container">
                <div class="card">
                    <p>This is where you will interact with your data and perform analysis.</p>
                    <a href="/Home" target="_self"><button class="card-button">Home</button></a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
