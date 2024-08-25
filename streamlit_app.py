# import streamlit as st

# # Set the page configuration
# st.set_page_config(page_title="AlertMinds")

# # Automatically redirect to /Home
# st.markdown("""
#     <meta http-equiv="refresh" content="0; url=/Home">
# """, unsafe_allow_html=True)


import streamlit as st

# Set the page configuration
st.set_page_config(page_title="AlertMinds", layout="wide")

# Check if the current URL path is root and redirect to /Home
if st.experimental_get_query_params().get("page", [""])[0] == "":
    st.experimental_set_query_params(page="Home")
    st.experimental_rerun()
else:
    st.markdown("""
        <meta http-equiv="refresh" content="0; url=/Home">
    """, unsafe_allow_html=True)
