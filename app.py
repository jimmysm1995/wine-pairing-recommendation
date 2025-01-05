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
    0: 'Ternera',
    1: 'Ternera lechal',
    2: 'Aves',
    3: 'Pasta',
    4: 'Marisco',
    5: 'Aperitivos y tentempiés',
    6: 'Pescado blanco',
    7: 'Carne adobada',
    8: 'Cordero',
    9: 'Carne de caza',
    10: 'Cerdo',
    11: 'Vegetariana',
    12: 'Carne de caza',
    13: 'Queso azul',
    14: 'Pescado azul',
    15: 'Comida picante',
    16: 'Queso tierno y cremoso',
    17: 'Pescado azul',
    18: 'Champiñones',
    19: 'Queso curado',
    20: 'Queso de leche de cabra',
    21: 'Aperitivo'
}

# Diccionario que mapea los números a los nombres de los tipos de vino
wine_type_mapping = {
    1: 'Blanco',
    2: 'Tinto'
}

# Diccionario para relacionar la calidad del precio con un número
price_quality_mapping = {
    1: 'Relación calidad-precio no disponible',
    2: 'Mejor relación calidad-precio en otros vinos',
    3: 'Relación calidad-precio razonable',
    4: 'Buena relación calidad-precio',
    5: 'Excelente relación calidad-precio',
    6: '¡Increíble relación calidad-precio!'
}

# Diccionario para asociar países a grupos
country_mapping = {
    'italia': 1,
    'francia': 2,
    'españa': 3
}

# Función que mapea los demás países a 0 (otros países)
def map_country_to_group(country_name):
    country_name = country_name.lower()
    return country_mapping.get(country_name, 0)  # Si no es Italia, Francia o España, se asigna 0

# Función para recomendar maridaje usando el modelo
def recomendar_maridaje(vino, data=None):
    # Si se pasa el nombre del vino
    if isinstance(vino, str): 
        vino_data = data[data['wine_name'] == vino]
        if vino_data.empty:
            return "No se encontró el vino seleccionado."
    # Si se pasa un DataFrame de datos del vino
    elif isinstance(vino, pd.DataFrame):
        vino_data = vino
    else:
        return "El dataframe del tipo de vino no es correcto"

    # Usar el modelo para predecir el maridaje
    features = vino_data[['year', 'price', 'score', 'wine_type', 'price_quality', 'country_grouped']]
    maridaje_predicho = model.predict(features)

    # Convertir los valores predichos a nombres de alimentos
    maridaje_nombres = [food_mapping[i] for i, val in enumerate(maridaje_predicho[0]) if val == 1]

    return maridaje_nombres


# Título de la aplicación
st.title('Recomendación de Maridaje de Vinos')

# Opción para elegir entre buscar un vino o ingresar un vino nuevo
opcion = st.selectbox('Selecciona una opción', ['Buscar vino', 'Ingresar un vino nuevo'])

if opcion == 'Buscar vino':
    # Buscador de vinos
    busqueda_vino = st.text_input('Buscar vino:')

    # Filtrar los vinos según la búsqueda
    vinos_filtrados = data[data['wine_name'].str.contains(busqueda_vino, case=False, na=False)]

    # Ordenar los vinos alfabéticamente
    vinos_ordenados = sorted(vinos_filtrados['wine_name'].unique())

    if vinos_ordenados:
            # Selección del vino
            vino_seleccionado = st.selectbox('Selecciona el vino:', vinos_ordenados)

            if st.button('Recomendar Maridaje'):
                maridaje = recomendar_maridaje(vino_seleccionado, data)  # Se pasa el nombre del vino y el DataFrame
                if maridaje:
                    st.write(f"Maridaje recomendado para {vino_seleccionado}: {', '.join(maridaje)}")
                else:
                    st.write(f"No se encontró el vino '{vino_seleccionado}' o no se pudo recomendar un maridaje.")

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
    else:
        st.write('No se encontraron vinos que coincidan con tu búsqueda.')

elif opcion == 'Ingresar un vino nuevo':
    # Formulario para ingresar un nuevo vino
    st.subheader("Ingresar datos de un nuevo vino")
    with st.form(key='nuevo_vino_form'):
        bodega = st.text_input('Bodega')
        wine_name = st.text_input('Nombre del vino')
        year = st.number_input('Año', min_value=1700, max_value=2025, step=1)
        price = st.number_input('Precio', min_value=0.0, step=0.01)
        score = st.number_input('Puntuación', min_value=1.0, max_value=5.0, step=0.1)
        wine_type = st.selectbox('Tipo de vino', options=[1, 2], format_func=lambda x: wine_type_mapping[x])
        price_quality = st.selectbox('Calidad del precio', options=[1, 2, 3, 4, 5, 6], format_func=lambda x: price_quality_mapping[x])  # Ajusta las opciones según sea necesario
        country_name  = st.text_input('País')

         # Asignar el número del país
        country_grouped = map_country_to_group(country_name)

        # Botón para enviar el formulario
        submit_button = st.form_submit_button(label='Recomendar Maridaje')

    # Si el formulario fue enviado
    if submit_button:
        # Crear un DataFrame con los datos del vino ingresado
        nuevo_vino = pd.DataFrame({
            'year': [year],
            'price': [price],
            'score': [score],
            'wine_type': [wine_type],
            'price_quality': [price_quality],
            'country_grouped': [country_grouped]  # Aquí asignamos el grupo de país
        })

        # Recomendar maridaje
        maridaje = recomendar_maridaje(nuevo_vino)
        if maridaje:
            st.write(f"Maridaje recomendado para el vino '{wine_name}': {', '.join(maridaje)}")
        else:
            st.write(f"No se pudo recomendar un maridaje para el vino '{wine_name}'.")