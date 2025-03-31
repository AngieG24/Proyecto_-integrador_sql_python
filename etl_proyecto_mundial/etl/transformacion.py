import os
import pandas as pd

def cargar_csv(nombre_archivo):
    """
    Carga un archivo CSV desde la carpeta datos_csv y lo devuelve como DataFrame.
    """
    ruta_csv = os.path.join(os.path.dirname(__file__), "..", "datos_csv", nombre_archivo)
    
    if os.path.exists(ruta_csv):
        df = pd.read_csv(ruta_csv)
        print(f"\n✅ Cargado: {nombre_archivo} ({df.shape[0]} filas, {df.shape[1]} columnas)")
        return df
    else:
        print(f"\n❌ Error: No se encontró {nombre_archivo}")
        return None

# Cargar todas las tablas de una sola vez
archivos_csv = ["city.csv", "country.csv", "countrylanguage.csv"]  # Lista de los nombres de los archivos

dataframes = {archivo.split(".")[0]: cargar_csv(archivo) for archivo in archivos_csv}


# Función para generar reporte de calidad de datos
def generar_reporte_calidad(dataframes, ruta_salida):
    """
    Genera un reporte de calidad de datos con valores nulos y porcentajes por DataFrame.
    """
    reportes = []

    for nombre, df in dataframes.items():
        if df is not None:
            df_reporte = pd.DataFrame({
                "Tabla": nombre,  # Nombre del DataFrame
                "Columna": df.columns,
                "Valores Nulos": df.isnull().sum(),
                "Porcentaje Nulos (%)": (df.isnull().mean() * 100).round(2)
            })
            reportes.append(df_reporte)
    
    # Unir todos los reportes en un solo DataFrame
    df_reporte_final = pd.concat(reportes, ignore_index=True)

    # Guardar el reporte como CSV
    df_reporte_final.to_csv(ruta_salida, index=False)
    print(f"\n📊 ✅ Reporte de calidad de datos guardado en: {ruta_salida}")

# 📂 Ruta donde se guardará el reporte
ruta_reporte = os.path.join(os.path.dirname(__file__), "..", "datos_csv", "reporte_calidad.csv")

# Generar el reporte de calidad antes de aplicar transformaciones
generar_reporte_calidad(dataframes, ruta_reporte)