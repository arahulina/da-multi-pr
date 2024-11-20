import streamlit as st
import pandas as pd
import base64
from streamlit_option_menu import option_menu
from pages import InteractiveMap, Prediction, TrendsAnalysis, TsunamiDepthMagnitude

# Головна сторінка
st.title("Earthquake Data Analysis")
st.write("""
Welcome to the Earthquake Data Analysis Project! 
Use the sidebar to navigate through different analysis tools:
- Interactive Map
- Trends Analysis
- Tsunami vs Depth & Magnitude Analysis
- Prediction
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

# Словник для сторінок
PAGES = {
   
    "Аналіз даних": TrendsAnalysis.display,
    "Інтерактивна карта": InteractiveMap.display,
    "Залежності": TsunamiDepthMagnitude.display,
    "Прогнозування": Prediction.display
}

st.set_page_config(page_title="Багатосторінковий застосунок", page_icon="🌟")


# Меню навігації
with st.sidebar:
    selected_page = option_menu(
        menu_title="Навігація",
        options=list(PAGES.keys()),
        icons=["house", "bar-chart-line", "map"],
        menu_icon="list",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f8f9fa"},
            "icon": {"color": "orange", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#02ab21"},
        },
    )

# Відображення вибраної сторінки
if selected_page in PAGES:
    # Оновлюємо параметри в URL
    st.query_params.update({"page": selected_page})
    PAGES[selected_page]()  # Виклик функції сторінки