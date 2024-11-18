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

# Завантаження даних
@st.cache_data
def load_data():
    return pd.read_csv('data/earthquake_1995-2023.csv')

data = load_data()

# Перетворення колонки з датами на формат datetime
data['date_time'] = pd.to_datetime(data['date_time'], errors='coerce')
# Додавання колонки для року
data['year'] = data['date_time'].dt.year