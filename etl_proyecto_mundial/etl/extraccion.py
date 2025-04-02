"""
Script de extracción de datos desde MySQL a archivos CSV.
Autor: Angie
Fecha: marzo 2025
Descripción: Este script se conecta a la base de datos 'world', extrae todas las tablas relevantes
y guarda sus datos como archivos CSV para análisis posterior.
"""
import sys
import mysql.connector  
import pandas as pd
import os
from etl_proyecto_mundial.config import MYSQL_CONFIG

# Agregar la carpeta raíz al sys.path para evitar problemas de importación
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

""" Extrae los datos de todas las tablas de la base de datos 'world'y los guarda en archivos CSV en la carpeta 'datos_csv'."""

# Definir la carpeta donde se guardarán los CSV
ruta_carpeta_csv = os.path.join(os.path.dirname(__file__), "..", "datos_csv")
os.makedirs(ruta_carpeta_csv, exist_ok=True)  # Crear carpeta si no existe

def extraer_datos():
   
    try:
        # Conectar a MySQL
        conexion = mysql.connector.connect(**MYSQL_CONFIG)
        
        if conexion.is_connected():
            print("✅ Conexión exitosa a MySQL")
            
            # Crear un cursor
            cursor = conexion.cursor()
            
            # Obtener los nombres de todas las tablas de la base de datos
            cursor.execute("SHOW TABLES;")
            tablas = [tabla[0] for tabla in cursor.fetchall()]
            
            # Extraer los datos de cada tabla y guardarlos en CSV
            for tabla in tablas:
                query = f"SELECT * FROM {tabla};"
                df = pd.read_sql(query, conexion)
                
                # Guardar en la carpeta 'datos_cvs' con el nombre de la tabla
                ruta_csv = os.path.join(ruta_carpeta_csv, f"{tabla}.csv")
                df.to_csv(ruta_csv, index=False, encoding='utf-8')
                
                # Mostrar cantidad de registros exportados
                print(f"📁 {tabla}.csv exportado con {len(df)} registros en '{ruta_csv}'")

    except mysql.connector.Error as error:
        print(f"❌ Error al conectar a MySQL: {error}")

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()
            print("🔌 Conexión cerrada")

# Prueba del script de extracción
if __name__ == "__main__":
    extraer_datos()