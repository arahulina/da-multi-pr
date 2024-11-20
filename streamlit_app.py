import streamlit as st
import pandas as pd
import base64

# Головна сторінка
st.title("Earthquake Data Analysis")
st.write("""
Welcome to the Earthquake Data Analysis Project! 
Use the sidebar to navigate through different analysis tools:
- Interactive Map
- Trends Analysis
- Tsunami vs Depth & Magnitude Analysis
""")

# Функція для додавання фонового зображення з локального файлу
def add_local_bg(image_file):
    # Читаємо зображення у base64
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    
    # Вставка стилів у Streamlit
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Використання локального зображення
add_local_bg("background.jpg")


@st.cache_data
def load_data():
    return pd.read_csv('data/earthquake_1995-2023.csv')

data = load_data()
#st.write(data.head())