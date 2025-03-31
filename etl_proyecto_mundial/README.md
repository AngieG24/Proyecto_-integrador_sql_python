## Proyecto ETL - Análisis de Datos Mundiales

Descripción

Este proyecto implementa un proceso ETL (Extracción, Transformación y Carga) utilizando Python y MySQL sobre la base de datos World. El objetivo es extraer datos relevantes, transformarlos mediante limpieza y enriquecimiento, y almacenarlos para su posterior análisis en herramientas de visualización y exploración de datos.

Tecnologías Utilizadas

Python: Lenguaje principal para la automatización del proceso ETL.

MySQL: Base de datos relacional utilizada como fuente de datos.

pandas: Para manipular y transformar los datos.

mysql-connector-python: Para la conexión entre Python y MySQL.

Jupyter Notebook: Para exploración de datos y análisis visual.

Git & GitHub: Para control de versiones y colaboración.

Estructura del Proyecto

ETL_Proyecto_Mundial/
│-- .git/                 # Carpeta del repositorio Git
│-- datos_csv/            # Almacenamiento de archivos CSV extraídos
│-- etl/                  # Código fuente del proceso ETL
│   │-- __init__.py       # Archivo para tratar el módulo como un paquete
│   │-- extraccion.py     # Módulo de extracción de datos desde MySQL
│   │-- transformacion.py # Módulo de transformación y limpieza de datos
│   │-- carga.py          # Módulo de carga de datos transformados
│-- notebooks/            # Análisis exploratorio y visualizaciones
│-- .gitignore            # Archivos y carpetas excluidos del repositorio
│-- config.py             # Configuración de conexión a la base de datos (IGNORADO en Git)
│-- main.py               # Orquestador del proceso ETL
│-- README.md             # Documentación del proyecto

Configuración y Uso

Clonar el repositorio:

git clone git@github.com:AngieG24/etl-proyecto-mundial.git
cd etl-proyecto-mundial

Crear y activar un entorno virtual (opcional pero recomendado):

python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate  # En Windows

Instalar dependencias:

pip install -r requirements.txt

Configurar la conexión a MySQL:

Crear un archivo config.py basado en config_example.py.

Agregar las credenciales correctas de la base de datos.

Ejecutar el proceso ETL:

python main.py

Próximos Pasos

Optimizar las consultas SQL para mejorar el rendimiento.

Agregar visualizaciones avanzadas con Seaborn y Matplotlib.

Automatizar el proceso con un scheduler (Airflow o Cron).

📌 Desarrollado por: AngieG24  🚀


