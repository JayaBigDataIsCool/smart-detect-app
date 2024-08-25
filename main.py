import streamlit as st
from streamlitapps.pages.data_ingestion import data_ingestion_page
from streamlitapps.pages.interactive_analytics import interactive_analytics_page
from streamlitapps.pages.data_visualization import data_visualization_page

# Apply CSS styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Initialize session state for page management
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Main function to control page navigation
def main():
    if st.session_state.page == 'data_ingestion':
        data_ingestion_page()
    elif st.session_state.page == 'interactive_analytics':
        interactive_analytics_page()
    elif st.session_state.page == 'data_visualization':
        data_visualization_page()
    else:
        show_home()

# Function to show the main landing page
def show_home():
    st.markdown("""
        <div class="main-container">
            <h1>Welcome to AlertMinds</h1>
            <h2>Empowering You to Stay Ahead of Fraud with Ease and Confidence</h2>
            <div class="card-container">
                <div class="card">
                    <h3>Data Ingestion</h3>
                    <p>Effortlessly gather data from multiple sources and watch your analytics soar.</p>
                    <button onclick="set_page('data_ingestion')" class="card-button">Explore</button>
                </div>
                <div class="card">
                    <h3>Interactive Analytics</h3>
                    <p>Discover insights effortlessly by talking directly to your data.</p>
                    <button onclick="set_page('interactive_analytics')" class="card-button">Explore</button>
                </div>
                <div class="card">
                    <h3>Data Visualization</h3>
                    <p>Bring your data to life with stunning visuals by uncovering hidden patterns.</p>
                    <button onclick="set_page('data_visualization')" class="card-button">Explore</button>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def set_page(page):
    st.session_state.page = page
    st.experimental_rerun()

if __name__ == "__main__":
    main()
