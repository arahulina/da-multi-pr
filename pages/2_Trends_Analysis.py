import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
@st.cache_data
def load_data():
    return pd.read_csv('data/earthquake_1995-2023.csv')

data = load_data()

st.title("Earthquake Trends Analysis")

# Кількість землетрусів за роками
yearly_counts = data.groupby('year').size()

# Візуалізація
fig, ax = plt.subplots(figsize=(10, 6))
yearly_counts.plot(kind='line', ax=ax)
ax.set_title("Number of Earthquakes Per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# Горизонтальна таблиця
st.write("Earthquake Counts by Year:")
st.dataframe(yearly_counts.reset_index().T)
