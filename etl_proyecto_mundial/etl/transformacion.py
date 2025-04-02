import os
import pandas as pd
import numpy as np

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

# ---------------------------------------------------------------------------------------------------------------------
"Elementos clave de la Transformación en mi ETL "

"1️⃣ Limpieza de datos"
"2️⃣ Estandarización y normalización"
"3️⃣ Enriquecimiento de datos"
"4️⃣ Creación de nuevas columnas o cálculos derivados"
# ---------------------------------------------------------------------------------------------------------------------
# Obtener el DataFrame
df_city = dataframes.get("city")
df_country = dataframes.get("country")  

"📌 Dataframe CITY"

# 🔹 Completar los valores nulos en la columna 'District' con datos verificados externamente.
# Se utiliza un diccionario con las correcciones y la función map() para asignar los valores correspondientes.

# Verificar si se cargó correctamente antes de modificarlo
if df_city is not None:
    def corregir_distritos(df):
        distritos_corregidos = {
            3285: "Taiwan Province",
            3293: "Kaohsiung",
            3294: "Taoyuan",
            3563: "Zulia"
        }
        # Reemplazar los valores nulos en la columna "District"
        df.loc[df["ID"].isin(distritos_corregidos.keys()), "District"] = df["ID"].map(distritos_corregidos)
        return df

    # Aplicar la función
    df_city = corregir_distritos(df_city)


"📌 Dataframe COUNTRY"

# Conversión de tipos de datos para mantener coherencia y facilitar análisis

# Cambio de tipo de dato para la columna 'IndepYear' a Int64
if 'IndepYear' in df_country.columns:
    df_country['IndepYear'] = df_country['IndepYear'].astype('Int64')

# cambio de tipo de dato para la columna Capital, que muy posiblemente corresponde al ID de la ciudad capital.
if 'Capital' in df_country.columns:
    df_country['Capital'] = df_country['Capital'].astype('Int64')

# Transformación y enriquecimiento de datos

# Crear columna EsIndependizado ✅ "Sí" → País con año de independencia registrado. ❌ "No aplica" → País sin independencia registrada.
df_country.insert(df_country.columns.get_loc("IndepYear") + 1, "EsIndependizado", 
                np.where(df_country["IndepYear"].isna(), "No aplica", "Sí"))

# Llenar valores nulos de GNPOld con la mediana de GNP
df_country['GNPOld'] = df_country['GNPOld'].fillna(df_country['GNP'].median())


# 🔹 Completar los valores nulos en la columna 'HeadOfState' con datos verificados externamente.

if df_country is not None:
    def jefes_estado_2002(df):
        jefes_estado_corregidos = {
            'AND': 'Coprincipe episcopal - Joan-Enric Vives i Sicília y Coprincipe francés -Jacques Chirac',
            'SMR': '1er semestre - Giuseppe Arzilli y Gian Carlo Venturini y 2do semestre - Roberto Giorgetti y Giovanni Lonfernini',
            'ATA': 'No aplica'
        }
        # Reemplazar los valores nulos en la columna "HeadOfState"
        df.loc[df["Code"].isin(jefes_estado_corregidos.keys()), "HeadOfState"] = df["Code"].map(jefes_estado_corregidos)
        return df
    # Aplicar la función
    df_country = jefes_estado_2002 (df_country)

# 🔹 Completar el campo Code2 que según busqueda exteRna "NA" corresponde al Código 2 correcto para mantener la coherencia del dataset.

def corregir_code2(df):
    if "Code2" in df.columns:
        # Convertir explícitamente los valores nulos a np.nan para evitar inconsistencias
        df["Code2"] = df["Code2"].replace("", np.nan)
        df.loc[(df["Name"] == "Namibia") & (df["Code2"].isna()), "Code2"] = "NA"
    return df

# Aplicar la función al DataFrame
df_country = corregir_code2(df_country)

