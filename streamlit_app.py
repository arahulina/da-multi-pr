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

# Вставка стилів для фонового зображення
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://depositphotos.com/photo/scenic-view-volcanic-rocky-mountain-bright-sunset-581699896.html");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Виклик функції для додавання фону
add_bg_from_url()