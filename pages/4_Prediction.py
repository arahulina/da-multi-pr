import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import streamlit as st

# Завантаження даних
@st.cache_data
def load_data():
    return pd.read_csv('data/earthquake_1995-2023.csv')

data = load_data()

# Перетворення колонки з датами на формат datetime
data['date_time'] = pd.to_datetime(data['date_time'], errors='coerce')
# Додавання колонки для року
data['year'] = data['date_time'].dt.year

st.title("Earthquake Prediction for 2025–2030 Using Machine Learning")

# Підготовка даних
earthquakes_per_year = data.groupby('year').size().reset_index()
earthquakes_per_year.columns = ['Year', 'Earthquake_Count']

# Розділення даних на ознаки (X) та цільову змінну (y)
X = earthquakes_per_year[['Year']].values  # Роки
y = earthquakes_per_year['Earthquake_Count'].values  # Кількість землетрусів

# Розділення даних на тренувальну та тестову вибірки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ініціалізація моделі лінійної регресії
model = LinearRegression()
model.fit(X_train, y_train)

# Прогнозування на тестових даних
y_pred = model.predict(X_test)

# Оцінка моделі
mse = mean_squared_error(y_test, y_pred)
st.write(f"Mean Squared Error (MSE): {mse:.2f}")

# Прогнозування на 2025–2030 роки
future_years = np.array([[2025], [2026], [2027], [2028], [2029], [2030]])
future_predictions = model.predict(future_years)

# Виведення прогнозів
predictions_df = pd.DataFrame({
    "Year": future_years.flatten(),
    "Predicted_Earthquakes": future_predictions.astype(int)
})
st.write("### Predictions for 2025–2030")
st.dataframe(predictions_df)

# Візуалізація
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Historical Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.scatter(future_years, future_predictions, color='green', label='Future Predictions')
plt.xlabel('Year')
plt.ylabel('Number of Earthquakes')
plt.title('Earthquake Predictions (2025–2030)')
plt.legend()
st.pyplot(plt)
