import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# Завантаження даних
@st.cache_data
def load_data():
    return pd.read_csv('data/earthquake_1995-2023.csv')

data = load_data()

# Перетворення колонки з датами на формат datetime
data['date_time'] = pd.to_datetime(data['date_time'], errors='coerce')
# Додавання колонки для року
data['year'] = data['date_time'].dt.year

#заголовок
st.title("Interactive Map of Earthquakes")

# Вибір континенту з можливістю вибору всіх континентів
continents = sorted(data['continent'].dropna().unique())
continents.insert(0, "All continents")
selected_continent = st.selectbox("Select a continent:", continents, key="continent_select")

# Вибір року з можливістю вибору всіх років
years = sorted(data['year'].dropna().unique())
years.insert(0, "All years")
selected_year = st.selectbox("Select a year:", years, key="year_select")

# Фільтрація даних за вибраними континентом і роком
if selected_continent == "All continents":
    filtered_data = data
else:
    filtered_data = data[data['continent'] == selected_continent]

if selected_year != "All years":
    filtered_data = filtered_data[filtered_data['year'] == selected_year]

# Перевірка наявності даних після фільтрації
if filtered_data.empty:
    st.warning("No data for the selected continent and year.")
else:
    # Функція для визначення кольору залежно від магнітуди
    def magnitude_color(magnitude):
        if magnitude < 4.0:
            return 'green'
        elif 4.0 <= magnitude < 5.0:
            return 'orange'
        elif 5.0 <= magnitude < 6.0:
            return 'red'
        else:
            return 'darkred'

    # Створення базової карти з фокусом на середні координати
    m = folium.Map(location=[filtered_data['latitude'].mean(), filtered_data['longitude'].mean()], zoom_start=3)

    # Вставка CSS для зменшення білого простору після карти
    st.markdown(
    """
    <style>
    iframe {
        height: 500px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    # Додавання точок землетрусів на карту
    for _, row in filtered_data.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,
            popup=f"Магнітуда: {row['magnitude']}\nГлибина: {row['depth']} км",
            color=magnitude_color(row['magnitude']),
            fill=True,
            fill_opacity=0.6
        ).add_to(m)

    # Додавання легенди на карту
    legend_html = """
         <div style="position: fixed;
                     bottom: 50px; left: 50px; width: 150px; height: 150px;
                     background-color: white; border:2px solid grey; z-index:9999; font-size:14px;
                     ">
         &nbsp; <b>Легенда:</b> <br>
         &nbsp; <i style="color:green;">●</i> Магнітуда < 4.0 <br>
         &nbsp; <i style="color:orange;">●</i> 4.0 ≤ Магнітуда < 5.0 <br>
         &nbsp; <i style="color:red;">●</i> 5.0 ≤ Магнітуда < 6.0 <br>
         &nbsp; <i style="color:darkred;">●</i> Магнітуда ≥ 6.0
         </div>
         """
    m.get_root().html.add_child(folium.Element(legend_html))

    # Відображення карти у Streamlit
    st.write(f"Continent: {selected_continent}, Year: {selected_year}")
    st_folium(m, width=700, height=500)


# Заголовок додатку
st.title("Comparison of the number of earthquakes by country or continent")

# Вибір групування: за країнами або континентами
group_by_option = st.radio("Sort by:", ['Country', 'Continent'])

# Групування та підрахунок
if group_by_option == 'Country':
    data_grouped = data['country'].value_counts().dropna().head(10)  # Топ-10 країн
    ylabel = "Number of earthquakes"
    title = "Number of earthquakes by country (Top 10)"
else:
    data_grouped = data['continent'].value_counts().dropna()
    ylabel = "Number of earthquakes"
    title = "Number of earthquakes by continent"

# Побудова стовпчикової діаграми
plt.figure(figsize=(10, 6))
data_grouped.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel(group_by_option)
plt.ylabel(ylabel)
plt.title(title)
plt.xticks(rotation=45)

# Відображення графіка у Streamlit
st.pyplot(plt)