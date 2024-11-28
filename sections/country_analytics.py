import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def load_by_country(df_country):
    country_list = df_country['Country'].unique()

    st.title("Климатический анализ по странам")

    default_country_index = list(country_list).index('Kazakhstan')

    # Выпадающий список для выбора страны
    country_name = st.selectbox("Выберите страну", options=country_list, index=default_country_index)

    st.write(f"Вы выбрали: {country_name}")

    if len(country_name) > 0:
        df_by_country = df_country[df_country['Country'] == country_name].copy()

        df_by_country['SmoothedTemperature'] = (
            df_by_country['AverageTemperature']
                .rolling(window=25, center=True)
                .mean()
        )

        # Plot the smoothed temperature trend
        plt.figure(figsize=(12, 6))
        sns.lineplot(x="dt", y="SmoothedTemperature", data=df_by_country, color="green", label="Сглаженная температура")

        # Add annotations for key points
        max_temp = df_by_country.loc[df_by_country['AverageTemperature'].idxmax()]
        min_temp = df_by_country.loc[df_by_country['AverageTemperature'].idxmin()]
        plt.annotate(f'Max: {max_temp["AverageTemperature"]:.2f}°C',
                     xy=(max_temp['dt'], max_temp['AverageTemperature']),
                     xytext=(max_temp['dt'], max_temp['AverageTemperature'] + 1),
                     arrowprops=dict(arrowstyle='->', color='black'))
        plt.annotate(f'Min: {min_temp["AverageTemperature"]:.2f}°C',
                     xy=(min_temp['dt'], min_temp['AverageTemperature']),
                     xytext=(min_temp['dt'], min_temp['AverageTemperature'] - 1),
                     arrowprops=dict(arrowstyle='->', color='black'))

        # Add labels, title, and grid
        plt.title("Средняя температура по стране " + country_name + " с течением времени", fontsize=14, pad=15)
        plt.xlabel("Год", fontsize=12)
        plt.ylabel("Средняя температура (°C)", fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.legend(fontsize=10)
        plt.tight_layout()

        st.pyplot(plt)

        st.title("Анализ десятилетий с наибольшим повышением температуры")

        st.markdown("Расчитываем среднюю температуру за каждое десятилетие")

        decade_avg_temp = df_country.groupby('Decade')['AverageTemperature'].mean().reset_index()

        # Improved visualization of average temperature by decade in Brazil
        plt.figure(figsize=(20.5, 10))

        # Plot the bar chart with a gradient color
        colors = plt.cm.YlGn([i / len(decade_avg_temp) for i in range(len(decade_avg_temp))])
        bars = plt.bar(decade_avg_temp['Decade'], decade_avg_temp['AverageTemperature'], color=colors, width=8)

        # Add exact values on top of each bar
        for bar, temp in zip(bars, decade_avg_temp['AverageTemperature']):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                     f'{temp:.2f}', ha='center', fontsize=10)

        # Add labels and title
        plt.xlabel('Десятилетие', fontsize=12)
        plt.ylabel('Средняя температупа (°C)', fontsize=12)
        plt.title('Историческая средняя температура в ' + country_name + ' за десятилетия', fontsize=14)

        # Add horizontal gridlines for better readability
        plt.grid(axis='y', linestyle='--', alpha=0.6)

        # Improve layout
        plt.tight_layout()

        # Show the plot
        st.pyplot(plt)

        st.title("Сравнение температур за разные десятилетия")

        # ср годовая температура
        annual_temp_by_country = df_by_country.groupby('Year')['AverageTemperature'].mean().reset_index()

        # ср движение за последние 10 лет
        annual_temp_by_country['Скользящая средняя за 10 лет'] = annual_temp_by_country['AverageTemperature'].rolling(window=10).mean()
        annual_temp_by_country.head(n=20)

        # Enhanced visualization of the temperature trend in Brazil with 10-Year Moving Average
        plt.figure(figsize=(12, 6))

        # Plot the original data and the 10-year moving average
        plt.plot(annual_temp_by_country['Year'], annual_temp_by_country['AverageTemperature'], color='green', label='Cр температура за год', alpha=0.6)
        plt.plot(annual_temp_by_country['Year'], annual_temp_by_country['Скользящая средняя за 10 лет'], color='red', linewidth=2,
                 label='Скользящая средняя за 10 лет')

        # Highlight key points
        max_temp = annual_temp_by_country.loc[annual_temp_by_country['AverageTemperature'].idxmax()]
        min_temp = annual_temp_by_country.loc[annual_temp_by_country['AverageTemperature'].idxmin()]
        plt.annotate(f'Max: {max_temp["AverageTemperature"]:.2f}°C',
                     xy=(max_temp['Year'], max_temp['AverageTemperature']),
                     xytext=(max_temp['Year'] + 10, max_temp['AverageTemperature'] + 0.2),
                     arrowprops=dict(arrowstyle='->', color='black'))
        plt.annotate(f'Min: {min_temp["AverageTemperature"]:.2f}°C',
                     xy=(min_temp['Year'], min_temp['AverageTemperature']),
                     xytext=(min_temp['Year'] - 20, min_temp['AverageTemperature'] - 0.3),
                     arrowprops=dict(arrowstyle='->', color='black'))

        # Add labels, title, and legend
        plt.xlabel('Год', fontsize=12)
        plt.ylabel('Температура (°C)', fontsize=12)
        plt.title('Исторический тренд. Скользящая средняя за последние 10 лет', fontsize=14)
        plt.legend(fontsize=10)

        # Add horizontal gridlines
        plt.grid(axis='y', linestyle='--', alpha=0.6)

        # Tight layout for better spacing
        plt.tight_layout()

        # Show the plot
        st.pyplot(plt)
    else:
        st.warning('Нет такой страны!', icon="⚠️")
