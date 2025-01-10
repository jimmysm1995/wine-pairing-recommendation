# 🍷 Proyecto de Recomendación de Maridajes para Vinos

¡Bienvenido/a a este proyecto! 🎉 Aquí encontrarás una aplicación que utiliza **inteligencia artificial** 🤖 para recomendar el mejor maridaje 🍽 según el vino 🍇 que elijas o ingreses.

## 📂 Estructura del Proyecto

El proyecto está dividido en varios archivos que cumplen diferentes funciones:

1. **`scraping.ipynb`**: 📡 Realiza _web scraping_ para obtener datos de vinos y los guarda en un archivo CSV.
2. **`preprocessing.ipynb`**: 🛠️ Prepara y limpia los datos para entrenar el modelo, generando un CSV limpio y listo para usar.
3. **`train_model.ipynb`**: 🎓 Entrena el modelo de IA y lo guarda en un archivo `.pkl`.
4. **`app.py`**: 💻 Código de la aplicación construida con Streamlit para interactuar con el modelo y recomendar maridajes.

## 🚀 Cómo Usar el Proyecto

### 1️⃣ Requisitos Previos
Asegúrate de tener instalados los siguientes paquetes en tu entorno Python:

```bash
pip install streamlit pandas scikit-learn joblib
```

### 2️⃣ Ejecutar la Aplicación
Inicia la aplicación con el siguiente comando:
```bash
streamlit run app.py
```

### 3️⃣ Interactuar con la Aplicación
- 🕵️ Buscar un vino: Escribe el nombre de un vino y descubre con qué alimentos marida mejor.
- ✍️ Ingresar un vino nuevo: Proporciona las características de un vino para obtener recomendaciones personalizadas.

## 📊 Funciones de la Aplicación
### 🔍 Buscar un Vino
1. Ingresa el nombre del vino que deseas buscar.
2. Selecciona el vino en los resultados.
3. Presiona "Recomendar Maridaje" y obtén una lista de alimentos sugeridos 🍖 🐟 🥗.

### 🆕 Ingresar un Vino Nuevo
Completa un formulario con:
- Nombre del vino
- Año, precio 💰, y puntuación ⭐
- Grado de alcohol 🍷 y tipo de vino
- País de origen 🌍 y sabor principal 🏵️

Obtendrás una recomendación de maridaje instantánea.

## 🧠 Entrenamiento del Modelo
El modelo de IA:
- Toma datos históricos de vinos y sus maridajes ideales.
- Utiliza un clasificador para predecir los mejores alimentos según características como:
  - Tipo de vino (blanco o tinto) 🍾
  - Precio y calidad 💵
  - Sabor y país de origen 🌎

## Archivos Importantes:
- 📄 `vivino.csv`: Datos en bruto obtenidos mediante scraping.
- 📄 `vivino_clean.csv`: Datos limpios y listos para usar en el modelo.
- 🗃️ `modelo_maridaje.pkl`: Modelo de IA entrenado.

## 📸 Capturas de Pantalla
✨ Por agregar (puedes subir capturas de la interfaz aquí).

## 📃 Licencia
Este proyecto está bajo la licencia MIT. ¡Siéntete libre de usarlo y mejorarlo! 😄
