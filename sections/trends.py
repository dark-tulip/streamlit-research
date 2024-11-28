import matplotlib.pyplot as plt
import streamlit as st
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose


def trend_analysis_section(df):
    st.title("Анализ трендов температуры")

    city = st.text_input("Введите город", value="Almaty")

    if city in df['City'].unique():
        city_data = df[df['City'] == city].set_index('dt').asfreq('MS')
        city_data['AverageTemperature'] = city_data['AverageTemperature'].interpolate(method='linear')

        st.markdown(f"### Температура в городе {city}")
        result = seasonal_decompose(city_data['AverageTemperature'], model='additive', period=12)
        fig = result.plot()
        fig.set_size_inches(12, 8)
        st.pyplot(fig)

        st.markdown("### Тренд с использованием сглаживания")
        model = ExponentialSmoothing(city_data['AverageTemperature'], trend='add', seasonal='add', seasonal_periods=12)
        fitted_model = model.fit()
        city_data['Smoothed'] = fitted_model.fittedvalues

        plt.figure(figsize=(12, 6))
        plt.plot(city_data.index, city_data['AverageTemperature'], label='Исходные данные', alpha=0.5)
        plt.plot(city_data.index, city_data['Smoothed'], label='Сглаженные данные', color='red')
        plt.title(f'Температура в городе {city} с применением сглаживания')
        plt.xlabel('Дата')
        plt.ylabel('Средняя температура (°C)')
        plt.legend()
        st.pyplot(plt)
    else:
        st.warning('Нет такого города!', icon="⚠️")
