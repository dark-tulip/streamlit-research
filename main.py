import streamlit as st

from data.data_loader import load_data, load_cities, load_data_from_country_df
from sections.country_analytics import load_by_country
from sections.general_analytics import general_analysis_section
from sections.hypotesis import hypothesis_section
from sections.meteostations import load_meteostations_section
from sections.trends import trend_analysis_section

st.set_page_config(page_title="Климатический анализ", layout="wide")
st.sidebar.title("Климатический анализ")

df = load_data()
cities_data = load_cities(df)
country_df = load_data_from_country_df()

section = st.sidebar.radio(
    "Выберите раздел:",
    ["Общий анализ", "Анализ трендов", "Гипотезы", "Карта метеостанций", "По странам"]
)

if section == "Общий анализ":
    general_analysis_section(df)

elif section == "Анализ трендов":
    trend_analysis_section(df)

elif section == "Гипотезы":
    hypothesis_section(df)

elif section == "Карта метеостанций":
    load_meteostations_section(cities_data)

elif section == "По странам":
    load_by_country(country_df)
