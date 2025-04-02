
import os
import pandas as pd
import mysql.connector

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from etl_proyecto_mundial.config import MYSQL_CONFIG
from etl.transformacion import df_city, df_country  # Importa los DataFrames transformados


# 🔹 1. Definir rutas de salida para CSV
ruta_base = os.path.dirname(__file__)  # Directorio actual
ruta_salida_city = os.path.join(ruta_base, "..", "datos_csv", "city.csv")
ruta_salida_country = os.path.join(ruta_base, "..", "datos_csv", "country.csv")

# 🔹 2. Guardar los archivos en formato CSV
df_city.to_csv(ruta_salida_city, index=False)
df_country.to_csv(ruta_salida_country, index=False)

print(f"\n✅ Datos guardados en CSV en:\n- {ruta_salida_city}\n- {ruta_salida_country}")