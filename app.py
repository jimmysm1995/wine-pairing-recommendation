import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo de maridaje
@st.cache_resource
def load_model():
    model = joblib.load('modelo_maridaje.pkl')
    return model

model = load_model()

# Cargar los datos de vinos
@st.cache_data
def load_data():
    data = pd.read_csv('data/vivino_clean.csv')
    # Eliminar los vinos que tengan como año -1
    data = data[data['year'] != -1]
    return data

data = load_data()

# Renombrar las columnas para que coincidan con las características usadas para entrenar el modelo
data.columns = [
    'bodega', 'wine_name', 'year', 'price', 'score', 'country', 'wine_type', 
    'pairing', 'pictures', 'price_quality', 'wine_style', 'country_grouped'
]

# Renombrar la columna 'pictures' a 'image'
data = data.rename(columns={'pictures': 'image'})

# Actualizar las URLs en la columna 'image' para que comiencen con 'https:'
data['image'] = data['image'].apply(lambda x: f"https:{x}" if x.startswith('//') else x)

# Diccionario que mapea los números a los nombres de los alimentos
food_mapping = {
    0: 'Carne',
    1: 'Pescado',
    2: 'Pollo',
    3: 'Pasta',
    4: 'Queso',
    5: 'Ensalada',
    6: 'Postre',
    7: 'Mariscos',
    8: 'Verduras',
    9: 'Sopa',
    10: 'Pizza',
    11: 'Hamburguesa',
    12: 'Sushi',
    13: 'Tacos',
    14: 'Paella',
    15: 'Curry',
    16: 'Barbacoa',
    17: 'Tapas',
    18: 'Risotto',
    19: 'Empanadas',
    20: 'Ceviche',
    21: 'Guiso'
}

# Diccionario que mapea los números a los nombres de los tipos de vino
wine_type_mapping = {
    1: 'Blanco',
    2: 'Tinto'
}

# Título de la aplicación
st.title('Recomendación de Maridaje de Vinos')

# Buscador de vinos
busqueda_vino = st.text_input('Buscar vino:')

# Filtrar los vinos según la búsqueda
vinos_filtrados = data[data['wine_name'].str.contains(busqueda_vino, case=False, na=False)]

# Ordenar los vinos alfabéticamente
vinos_ordenados = sorted(vinos_filtrados['wine_name'].unique())

# Selección del vino
vino_seleccionado = st.selectbox('Selecciona el vino:', vinos_ordenados)

# Función para recomendar maridaje usando el modelo
def recomendar_maridaje(vino):
    vino_data = data[data['wine_name'] == vino]
    if vino_data.empty:
        return "No se encontró el vino seleccionado."
    else:
        # Usar el modelo para predecir el maridaje
        features = vino_data[['year', 'price', 'score', 'wine_type', 'price_quality', 'country_grouped']]
        maridaje_predicho = model.predict(features)
        # Convertir los valores predichos a nombres de alimentos
        maridaje_nombres = [food_mapping[i] for i, val in enumerate(maridaje_predicho[0]) if val == 1]
        return maridaje_nombres

if st.button('Recomendar Maridaje'):
    maridaje = recomendar_maridaje(vino_seleccionado)
    st.write(f"Maridaje recomendado para {vino_seleccionado}: {', '.join(maridaje)}")

# Mostrar detalles del vino seleccionado
vino_data = data[data['wine_name'] == vino_seleccionado]
if not vino_data.empty:
    st.subheader('Detalles del Vino Seleccionado')
    st.write(f"Bodega: {vino_data.iloc[0]['bodega']}")
    st.write(f"Año: {vino_data.iloc[0]['year']}")
    st.write(f"Precio: {vino_data.iloc[0]['price']}")
    st.write(f"Puntuación: {vino_data.iloc[0]['score']}")
    st.write(f"País: {vino_data.iloc[0]['country']}")
    st.write(f"Tipo de Vino: {wine_type_mapping[vino_data.iloc[0]['wine_type']]}")
    st.write(f"Estilo de Vino: {vino_data.iloc[0]['wine_style']}")
    if vino_data.iloc[0]['image']:
        st.image(vino_data.iloc[0]['image'], width=80)