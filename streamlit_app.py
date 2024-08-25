import streamlit as st
import os

# Set global page configuration
st.set_page_config(page_title="AlertMinds")

# Apply CSS styles
@st.cache_data
def load_css():
    css_file = os.path.join(os.path.dirname(__file__), 'styles.css')
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Hide the sidebar
    hide_sidebar_style = """
        <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="stSidebarNav"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
        </style>
    """
    st.markdown(hide_sidebar_style, unsafe_allow_html=True)
    


load_css()

# Handle page navigation
page = st.experimental_get_query_params().get("page", ["Home"])[0]

def switch_page(page_name):
    st.experimental_set_query_params(page=page_name)
    st.experimental_rerun()

if page == "Home":
    from pages import Home
elif page == "Data_Ingestion":
    from pages import Data_Ingestion
elif page == "Interactive_Analytics":
    from pages import Interactive_Analytics
elif page == "Data_Visualization":
    from pages import Data_Visualization
