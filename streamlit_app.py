import streamlit as st

# Set the page configuration
st.set_page_config(page_title="AlertMinds", layout="wide")

# Helper function to load the correct page based on query params
def load_page():
    page = st.experimental_get_query_params().get("page", ["Home"])[0]

    if page == "Home":
        from pages import Home
        Home.render()
    elif page == "Data_Ingestion":
        from pages import Data_Ingestion
        Data_Ingestion.render()
    elif page == "Interactive_Analytics":
        from pages import Interactive_Analytics
        Interactive_Analytics.render()
    elif page == "Data_Visualization":
        from pages import Data_Visualization
        Data_Visualization.render()

# Check for page query parameter and handle redirection
query_params = st.experimental_get_query_params()
if not query_params.get("page"):
    # If no page is set, redirect to Home
    st.markdown('<meta http-equiv="refresh" content="0; url=/Home">', unsafe_allow_html=True)
else:
    # Load the appropriate page
    load_page()
