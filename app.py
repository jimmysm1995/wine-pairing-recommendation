import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
@st.cache_data
def load_data():
    # Reemplaza 'data/vivino_clean.csv' con la ruta a tu archivo de datos
    data = pd.read_csv('data/vivino_clean.csv')
    # Mapear valores numéricos a nombres de tipos de vino
    wine_type_mapping = {1: 'blanco', 2: 'tinto'}
    data['wine_type'] = data['wine_type'].map(wine_type_mapping)
    return data

data = load_data()

# Título de la aplicación
st.title('Recomendación de Maridaje de Vinos')

# Mostrar los datos
st.write('Datos de Vinos:')
st.dataframe(data)

# Función para recomendar vinos
def recomendar_vino(tipo_comida, tipo_vino=None, region=None):
    recomendaciones = data[data['pairing'] == tipo_comida]
    if tipo_vino:
        recomendaciones = recomendaciones[recomendaciones['wine_type'] == tipo_vino]
    if region:
        recomendaciones = recomendaciones[recomendaciones['country'] == region]
    # Ordenar por puntuación y seleccionar los 10 mejores
    recomendaciones = recomendaciones.sort_values(by='score', ascending=False).head(10)
    return recomendaciones

# Interfaz de usuario
tipo_comida = st.selectbox('Selecciona el tipo de comida:', data['pairing'].unique())
tipo_vino = st.selectbox('Selecciona el tipo de vino (opcional):', [''] + list(data['wine_type'].unique()))
region = st.selectbox('Selecciona la región (opcional):', [''] + list(data['country'].unique()))

if st.button('Recomendar Vino'):
    recomendaciones = recomendar_vino(tipo_comida, tipo_vino if tipo_vino else None, region if region else None)
    st.write('Vinos recomendados:')
    st.dataframe(recomendaciones)

    # Mostrar descripciones detalladas
    for index, row in recomendaciones.iterrows():
        st.subheader(row['wine_name'])
        st.write(f"Tipo: {row['wine_type']}")
        st.write(f"Región: {row['country']}")
        st.write(f"Descripción: {row['Estilo de vino']}")

    # Mostrar gráfico de distribución de puntuaciones
    st.write('Distribución de puntuaciones:')
    fig, ax = plt.subplots()
    recomendaciones['score'].hist(ax=ax, bins=20)
    st.pyplot(fig)

    # Mostrar tabla con nombres y puntuaciones de los vinos recomendados
    st.write('Nombres y puntuaciones de los vinos recomendados:')
    st.table(recomendaciones[['wine_name', 'score']])
