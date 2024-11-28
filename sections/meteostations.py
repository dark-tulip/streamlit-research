import streamlit as st


def load_meteostations_section(cities_data):
    st.title("Карта метеостанций")

    st.markdown("### Метеостанции на разных континентах")

    st.map(cities_data[['lat', 'lon']])

    st.markdown("На карте указаны метеостанции в городах, представленных в датасете.")
