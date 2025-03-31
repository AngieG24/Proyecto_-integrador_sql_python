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


# -----------------------------------------------------------------------------------------------------------------
# 🔹 Completar los valores nulos en la columna 'District' con datos verificados externamente.
# Se utiliza un diccionario con las correcciones y la función map() para asignar los valores correspondientes.

# Obtener el DataFrame de city
df_city = dataframes.get("city")  

# Verificar si se cargó correctamente antes de modificarlo
if df_city is not None:
# Definir los valores correctos para los distritos

    def corregir_distritos(df):

        distritos_corregidos = {
            3285: "Taiwan Province",
            3293: "Kaohsiung",
            3294: "Taoyuan",
            3563: "Zulia"
        }
    # Reemplazar los valores nulos en la columna "District"
        df.loc[df_city["ID"].isin(distritos_corregidos.keys()), "District"] = df_city["ID"].map(distritos_corregidos)

    df_city = corregir_distritos(df_city)

    # Guardar el CSV transformado
    ruta_salida = os.path.join(os.path.dirname(__file__), "..", "datos_csv", "city.csv")
    df_city.to_csv(ruta_salida, index=False)
    print(f"\n✅ Archivo actualizado y guardado en: {ruta_salida}")

