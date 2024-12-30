import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
@st.cache_data
def load_data():
    # Ruta a los datos de archivos
    data = pd.read_csv('data/vivino_clean.csv')
    # Mapear valores numéricos a nombres de tipos de vino
    wine_type_mapping = {1: 'Blanco', 2: 'Tinto'}
    data['wine_type'] = data['wine_type'].map(wine_type_mapping)
    return data

data = load_data()

# Extraer tipos de comida únicos
comidas = set()
for pairings in data['pairing']:
    for comida in pairings.split(','):
        comidas.add(comida.strip())

# Título de la aplicación
st.title('Recomendación de Maridaje de Vinos')

# Mostrar los datos
st.write('Datos de Vinos:')
st.dataframe(data)

# Función para recomendar vinos
def recomendar_vino(tipo_comida, tipo_vino=None, region=None):
    recomendaciones = data[data['pairing'].str.contains(tipo_comida, case=False, na=False)]
    if tipo_vino:
        recomendaciones = recomendaciones[recomendaciones['wine_type'] == tipo_vino]
    if region:
        recomendaciones = recomendaciones[recomendaciones['country'] == region]
    # Ordenar por puntuación y seleccionar los 10 mejores
    recomendaciones = recomendaciones.sort_values(by='score', ascending=False).head(10)
    return recomendaciones

# Interfaz de usuario
tipo_comida = st.selectbox('Selecciona el tipo de comida:', sorted(comidas))
tipo_vino = st.selectbox('Selecciona el tipo de vino (opcional):', [''] + list(data['wine_type'].unique()))
region = st.selectbox('Selecciona la región (opcional):', [''] + list(data['country'].unique()))

if st.button('Recomendar Vino'):
    recomendaciones = recomendar_vino(tipo_comida, tipo_vino if tipo_vino else None, region if region else None)
    if recomendaciones.empty:
        st.write('No se ha encontrado ninguna coincidencia relacionada con la búsqueda. Intentelo de nuevo con otras opciones.')
    else:
        st.write('Vinos recomendados:')

        # Mostrar descripciones detalladas
        for index, row in recomendaciones.iterrows():
            st.subheader(row['wine_name'])
            st.write(f"Tipo: {row['wine_type']}")
            st.write(f"Región: {row['country']}")
            st.write(f"Descripción: {row['Estilo de vino']}")

        # Mostrar gráfico de distribución de puntuaciones
        st.write('Distribución de puntuaciones:')
        fig, ax = plt.subplots()
        recomendaciones.plot(kind='bar', x='wine_name', y='score', ax=ax, legend=False, color='skyblue', edgecolor='black')
        ax.set_ylabel('Puntuación', fontsize=12)
        ax.set_xlabel('Nombre del Vino', fontsize=12)
        ax.set_title('Puntuaciones de los Vinos Recomendados', fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.yticks(fontsize=10)
        ax.grid(True, linestyle='--', alpha=0.7)
        st.pyplot(fig)

        # Mostrar tabla con nombres y puntuaciones de los vinos recomendados
        st.write('Nombres y puntuaciones de los vinos recomendados:')
        st.table(recomendaciones[['wine_name', 'score']])
