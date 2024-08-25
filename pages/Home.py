import streamlit as st

# Force wide layout
st.set_page_config(layout="wide")


# Apply CSS styles
@st.cache_data
def load_css():
    with open("styles.css") as f:
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

st.markdown("""
    <div class="main-container">
        <h1>Welcome to AlertMinds</h1>
        <h2>Empowering You to Stay Ahead of Fraud with Ease and Confidence</h2>
        <div class="card-container">
            <div class="card">
                <h3>Data Ingestion</h3>
                <p>Effortlessly gather data from multiple sources and watch your analytics soar.</p>
                <a href="/Data_Ingestion" target="_self"><button class="card-button">Explore</button></a>
            </div>
            <div class="card">
                <h3>Interactive Analytics</h3>
                <p>Discover insights effortlessly by talking directly to your data.</p>
                <a href="/Interactive_Analytics" target="_self"><button class="card-button">Explore</button></a>
            </div>
            <div class="card">
                <h3>Data Visualization</h3>
                <p>Bring your data to life with stunning visuals by uncovering hidden patterns.</p>
                <a href="/Data_Visualization" target="_self"><button class="card-button">Explore</button></a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
