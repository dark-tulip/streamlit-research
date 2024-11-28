import matplotlib.pyplot as plt
import streamlit as st


def general_analysis_section(df):
    st.title("Общий анализ данных")

    st.markdown("### Пример данных")

    btn = st.radio(
        "Выберите начало просмотра датасета: ",
        ["head", "tail"],
        key="['head']"
    )

    if btn == 'head':
        st.write(df.head())
    else:
        st.write(df.tail())

    st.markdown("### Гистограмма температуры")
    bins = st.slider("Количество бинов для гистограммы", 10, 100, 80)
    plt.figure(figsize=(8, 5))
    plt.hist(df['AverageTemperature'], bins=bins, color='skyblue', edgecolor='black')
    plt.title('Распределение средней температуры')
    plt.xlabel('Средняя температура, °C')
    plt.ylabel('Частота')
    st.pyplot(plt)
