import streamlit as st
import components.age_cloud, components.decade_cloud, components.gender_cloud
from components.multipage import MultiPage

def app():
    with open('styles/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.markdown('<link rel="preconnect" href="https://fonts.googleapis.com">',
                    unsafe_allow_html=True)

    app = MultiPage()

    app.add_page("Age", components.age_cloud.app)
    app.add_page("Decade", components.decade_cloud.app)
    app.add_page("Gender", components.gender_cloud.app)

    app.run()
