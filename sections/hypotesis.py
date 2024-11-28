import matplotlib.pyplot as plt
import streamlit as st
from scipy.stats import linregress


def hypothesis_section(df):
    st.title("Проверка гипотезы")

    st.markdown("### Гипотеза: Наблюдается глобальное потепление.")
    city = st.text_input("Введите город для проверки гипотезы", value="Almaty")
    if city in df['City'].unique():
        city_data = df[df['City'] == city]

        avg_temp_per_year = city_data.groupby('Year')['AverageTemperature'].mean().reset_index()
        slope, intercept, r_value, p_value, std_err = linregress(avg_temp_per_year['Year'], avg_temp_per_year['AverageTemperature'])

        st.markdown("**Результаты линейной регрессии:**")
        st.write(f"Уклон (slope): {slope:.2f}")
        st.write(f"p-значение: {p_value:.2f}")
        st.write(f"Коэффициент детерминации (R²): {r_value ** 2:.2f}")

        if p_value < 0.05:
            trend = "потепление" if slope > 0 else "похолодание"
            st.markdown(f"**Вывод:** Гипотеза подтверждается, наблюдается {trend}.")
        else:
            st.markdown("**Вывод:** Гипотеза не подтверждается.")

        st.markdown("### Визуализация тренда")
        plt.figure(figsize=(12, 6))
        plt.plot(avg_temp_per_year['Year'], avg_temp_per_year['AverageTemperature'], label='Средние температуры', alpha=0.7)
        plt.plot(avg_temp_per_year['Year'], intercept + slope * avg_temp_per_year['Year'], color='red', label='Тренд')
        plt.title(f'Тренд температуры в городе {city}')
        plt.xlabel('Год')
        plt.ylabel('Средняя температура (°C)')
        plt.legend()
        st.pyplot(plt)
    else:
        st.warning('Нет такого города!', icon="⚠️")
