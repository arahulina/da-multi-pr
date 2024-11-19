import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Завантаження даних
@st.cache_data
def load_data():
    return pd.read_csv('data/earthquake_1995-2023.csv')

data = load_data()

# Перетворення колонки з датами на формат datetime
data['date_time'] = pd.to_datetime(data['date_time'], errors='coerce')
# Додавання колонки для року
data['year'] = data['date_time'].dt.year

st.title("Earthquake Prediction for the Next 10 Years")

# Агрегування даних за роками
earthquakes_per_year = data.groupby('year').size().reset_index()
earthquakes_per_year.columns = ['ds', 'y']  # Перейменування для Prophet

# Ініціалізація моделі Prophet
model = Prophet()
model.fit(earthquakes_per_year)

# Створення майбутніх дат (наступні 10 років)
future = model.make_future_dataframe(periods=10, freq='Y')
forecast = model.predict(future)

# Візуалізація прогнозу
fig1 = model.plot(forecast)
fig2 = model.plot_components(forecast)

st.write("### Historical Data and Forecast")
st.pyplot(fig1)

st.write("### Forecast Components")
st.pyplot(fig2)

# Показ прогнозу у вигляді таблиці
st.write("### Forecast Data")
st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10))
