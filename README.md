## Introducción 🚀


Este proyecto ETL (Extracción, Transformación y Carga) tiene como objetivo procesar los datos de la base de datos "world" de MySQL y analizarlos en Python. La implementación se realizó en Visual Studio Code (VS Code) para el desarrollo del código y Jupyter Notebook para la exploración visual de
los datos.

## Tecnologías Utilizadas

- Python: Lenguaje principal para la automatización del proceso ETL.
- MySQL: Base de datos relacional utilizada como fuente de datos.
- Numpy: Para trabajar con grandes conjuntos de datos de manera eficiente. Operaciones
- matemáticas y estadísticas de alto rendimiento.
- Pandas: Para manipular y transformar los datos.
- Seaborn (as sns): Es una librería basada en Matplotlib que facilita la creación de gráficos estadísticos atractivos y con estilo, proporcionando funciones más sencillas y poderosas para visualización de datos.
- Matplotlib (as plt): Es una librería de gráficos en 2D para Python que permite crear una amplia variedad de gráficos estáticos, animados e interactivos, como líneas, barras, dispersión, etc.
- Folium: Es una librería para crear mapas interactivos utilizando Leaflet.js y permite visualizar datos geoespaciales de manera interactiva sobre mapas.
- mysql-connector-python: Para la conexión entre Python y MySQL.
- SQLAlchemy y PyMySQL: para Consultas SQL
- Jupyter Notebook: Para exploración de datos y análisis visual.
- Git & GitHub: Para control de versiones y colaboración.


##Estructura del Proyecto 📂

El proyecto está estructurado en los siguientes archivos y carpetas: 
├── etl_proyecto_mundial/
│ ├── etl/
│ │ ├──
extraccion.py
#### 📥 Módulo de extracción de datos desde MySQL
│ │ ├──
transformacion.py
####  🔄Procesamiento y limpieza de datos
│ │ ├──
carga.py
####  📤 Exportación a CSV
│ ├──
config.py
####  📌Configuración de conexión a MySQL
│ ├──
main.py
#### ▶️ Script principal de ejecución
│ ├── datos_csv/ # 📁 Carpeta donde se guardan los archivos CSV
│ ├── world/ # Carpeta con las tablas de la base de datos world
│ ├── Exploración.ipynb # 📊Notebook para análisis exploratorio
│ ├──
README.md
#### Documentación general del proyecto


## Conclusión 🎯

Este proyecto demuestra cómo estructurar un proceso ETL de manera modular y profesional, asegurando la reutilización del código y facilitando su mantenimiento.
✅ La separación de la conexión en
config.py
permite automatizar la conexión y mejorar la seguridad del proyecto.
✅ La organización en módulos mejora la escalabilidad y facilidad de mantenimiento del código.
