import streamlit as st
import pandas as pd

# Головна сторінка
st.title("Earthquake Data Analysis")
st.write("""
Welcome to the Earthquake Data Analysis Project! 
Use the sidebar to navigate through different analysis tools:
- Interactive Map
- Trends Analysis
- Tsunami vs Depth & Magnitude Analysis
""")

# CSS для додавання фонового зображення
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('image/background.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""

# Вставка стилів на сторінку
st.markdown(page_bg, unsafe_allow_html=True)