import pandas as pd
import streamlit as st


@st.cache
def load_data():
    """
    # Отвечает за выгрузку датасета
    # Используем кэширование чтобы работало быстрее
    :return: очищенный датасет с конвертированной датой
    """
    df = pd.read_csv('./data/GlobalLandTemperaturesByCity.csv')
    # Очистка нуллов
    df = df.dropna(subset=['AverageTemperature'])
    df = df.dropna(subset=['City'])

    # Конвертация даты в тип datetime
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    df['Month'] = df['dt'].dt.month
    return df


@st.cache
def load_data_from_country_df():
    """
    # Отвечает за выгрузку датасета по странам
    # Используем кэширование чтобы работало быстрее
    :return: очищенный датасет с конвертированной датой
    """
    df = pd.read_csv('./data/GlobalLandTemperaturesByCountry.csv')
    # Очистка нуллов
    df = df.dropna(subset=['AverageTemperature'])

    # Конвертация даты в тип datetime
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    df['Month'] = df['dt'].dt.month
    df['Decade'] = (df['Year'] // 10) * 10
    df.set_index('Country')
    return df


@st.cache
def load_cities(df):
    """
    # Используем кэширование чтобы работало быстрее
    :param df: датасет
    :return: датасет городов и их координат чтобы нарисовать на карте
    """
    cities_data = df[['City', 'Latitude', 'Longitude']].drop_duplicates().reset_index(drop=True)

    def convert_coordinates(coord):
        value = float(coord[:-1])
        if coord[-1] in ['S', 'W']:
            return -value
        return value

    cities_data['lat'] = cities_data['Latitude'].apply(convert_coordinates)
    cities_data['lon'] = cities_data['Longitude'].apply(convert_coordinates)
    return cities_data
