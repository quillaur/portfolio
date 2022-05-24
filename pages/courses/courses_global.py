import streamlit as st
from PIL import Image

def app():
    teachings = Image.open("images/teachings.png")
    st.image(teachings)
        