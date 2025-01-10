# 🍷 Wine Pairing Recommendation Project

## 🌍 Chose Your Language / Elige tu idioma:
- [English](#english-)
- [Español](#español-)

---

## English GB
Welcome! 🎉 This project features an application that uses **artificial intelligence** 🤖 to recommend the best food pairing 🍽 based on the wine 🍇 you choose or enter.

## 📂 Project Structure

The project is divided into several files, each with a specific purpose:

1. **`scraping.ipynb`**: 📡 Performs web scraping to gather wine data and saves it into a CSV file.
2. **`preprocessing.ipynb`**: 🛠️ Prepares and cleans the data for model training, generating a clean, ready-to-use CSV file.
3. **`train_model.ipynb`**: 🎓 Trains the AI model and saves it in a `.pkl` file.
4. **`app.py`**: 💻 The Streamlit application code that interacts with the model to recommend pairings.

## 🚀 How to Use the Project

### 1️⃣ Prerequisites

Make sure you have the following packages installed in your Python environment:

```bash
pip install streamlit pandas scikit-learn joblib
```

### 2️⃣ Running the Application
#### 🖥️Option 1: Run with Python
1. Start the application with the following command:
    ```bash
    streamlit run app.py
    ```
2. Open your browser at `http://localhost:8501/`.

#### 🐳 Option 2: Run with Docker
1. Launch Docker Desktop 🐳.
2. Open the terminal and navigate to the project directory.
3. Run the following command:
    ```bash
    docker-compose up --build
    ```
4. Open your browser at `http://localhost:8502/`.

### 3️⃣ Interacting with the Application
- 🕵️ Search for a wine: Enter the name of a wine and discover its best food pairings.
- ✍️ Add a new wine: Provide the characteristics of a wine to get personalized recommendations.

## 📊 Application Features
### 🔍 Search for a Wine
1. Enter the name of the wine you want to search for.
2. Select the wine from the results.
3. Press "Recommend Pairing" to get a list of suggested foods 🍖 🐟 🥗.

### 🆕 Add a New Wine
Fill out a form with:
- Wine name
- Year, price 💰, and rating ⭐
- Alcohol content 🍷 and wine type
- Country of origin 🌍 and main flavor 🏵️

You'll get an instant pairing recommendation.

## 🧠 Model Training
The AI model:
- Uses historical data of wines and their ideal pairings.
- Employs a classifier to predict the best food options based on characteristics like:
  - Wine type (red or white) 🍾
  - Price and quality 💵
  - Flavor and country of origin 🌎

## Key Files:
- 📄 **`vivino.csv`**: Raw data obtained through scraping.
- 📄 **`vivino_clean.csv`**: Cleaned data ready for model training.
- 🗃️ **`modelo_maridaje.pkl`**: Trained AI model file.

## 📸 Screenshots
✨ To be added (you can upload UI screenshots here).

## 📃 License
This project is licensed under the MIT license. Feel free to use and improve it! 😄

## 👨‍💻 Credits
This project was created by:
- **David Moreno Cerezo**
- **Jose Sanchez**
- **Jesús Ruiz Toledo**

Enjoy the perfect pairing between technology and gastronomy. 🍷🍴

---

## Español ES

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
#### 🖥️ Opción 1: Ejecutar con Python
1. Inicia la aplicación con el siguiente comando:
    ```bash
    streamlit run app.py
    ```
2. Busca en el navegador `http://localhost:8501/`.

#### 🐳 Opción 2: Ejecutar con Docker
1. Inicia el programa Docker Desktop 🐳.
2. Abre la terminal y sitúate en el directorio del proyecto.
3. Ejecuta el siguiente comando:
    ```bash
    docker-compose up --build
    ```
4. Abre tu navegador en `http://localhost:8502/`.

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
- 📄 **`vivino.csv`**: Datos en bruto obtenidos mediante scraping.
- 📄 **`vivino_clean.csv`**: Datos limpios y listos para usar en el modelo.
- 🗃️ **`modelo_maridaje.pkl`**: Modelo de IA entrenado.

## 📸 Capturas de Pantalla
✨ Por agregar (puedes subir capturas de la interfaz aquí).

## 📃 Licencia
Este proyecto está bajo la licencia MIT. ¡Siéntete libre de usarlo y mejorarlo! 😄

## 👨‍💻 Créditos
Este proyecto fue creado por:
- **David Moreno Cerezo**
- **Jose Sanchez**
- **Jesús Ruiz Toledo** 

Disfruta del maridaje perfecto entre tecnología y gastronomía. 🍷🍴
