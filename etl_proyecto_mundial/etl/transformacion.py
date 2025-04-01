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

"🎯 REPORTE DE DATAFRAMES CON NULOS(ANTES DE LA LIMPIEZA)"

# Obtener el DataFrame
df_city = dataframes.get("city")
df_country = dataframes.get("country")  

ruta_log = os.path.join(os.path.dirname(__file__), "..", "log_auditoria.txt")

# Verificar si el archivo de log existe
reporte_existente = os.path.exists(ruta_log)

with open(ruta_log, "a", encoding="utf-8") as log:  # "a" para agregar sin sobrescribir
    if not reporte_existente:
        log.write("📋 REGISTRO DE AUDITORÍA DE DATOS\n")
        log.write("=" * 80 + "\n")

    # 🔹 Reporte de ciudades sin distrito
    df_ciudades_sin_distrito = df_city[df_city["District"].isna()][["ID", "Name", "CountryCode"]]
    if not df_ciudades_sin_distrito.empty:
        log.write("\n🏙️ CIUDADES SIN DISTRITO ANTES DE LA LIMPIEZA\n")
        log.write("-" * 80 + "\n")
        log.write(df_ciudades_sin_distrito.to_string(index=False))
        log.write("\n" + "-" * 80 + "\n")

    # 🔹 Reporte de países sin Independencia registrada
    df_paises_sin_indep = df_country[df_country["IndepYear"].isna()][["Code", "Name", "Region"]]
    if not df_paises_sin_indep.empty:
        log.write("\n🌎 PAÍSES SIN AÑO DE INDEPENDENCIA REGISTRADO\n")
        log.write("-" * 80 + "\n")
        log.write(df_paises_sin_indep.to_string(index=False))
        log.write("\n" + "-" * 80 + "\n")

    # 🔹 Reporte de países sin GNPOld registrada
    df_paises__sin_gnpold = df_country[df_country["GNPOld"].isna()][["Code", "Name", "GNP"]]
    if not df_paises__sin_gnpold.empty:
        log.write("\n🌎 PAÍSES SIN PRODUCTO NACIONAL BRUTO DE PERIODO ANTERIOR (GNPOld) REGISTRADO\n")
        log.write("-" * 80 + "\n")
        log.write(df_paises_sin_indep.to_string(index=False))
        log.write("\n" + "-" * 80 + "\n")    

    # 🔹 Reporte de países sin el nombre del Jefe de Estado
    df_paises_sin_jefeestado = df_country[df_country["HeadOfState"].isna()][["Code", "Name", "GovernmentForm"]]
    if not df_paises_sin_jefeestado.empty:
        log.write("\n🌎 PAÍSES SIN JEFE DE ESTADO REGISTRADO\n")
        log.write("-" * 80 + "\n")
        log.write(df_paises_sin_indep.to_string(index=False))
        log.write("\n" + "-" * 80 + "\n")

print(f"\n✅ Reporte actualizado en: {ruta_log}")

# ----------------------------------------------------------------------------------------------------------------------
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

    # Guardar el CSV transformado
    ruta_salida_city = os.path.join(os.path.dirname(__file__), "..", "datos_csv", "city.csv")
    df_city.to_csv(ruta_salida_city, index=False)
    print(f"\n✅ Limpieza de datos df CITY: Archivo actualizado y guardado en: {ruta_salida_city}")


"📌 Dataframe COUNTRY"

# Conversión de tipos de datos para mantener coherencia y facilitar análisis

# Cambio de tipo de dato para la columna 'IndepYear' a Int64
if 'IndepYear' in df_country.columns:
    df_country['IndepYear'] = df_country['IndepYear'].astype('Int64')

# cambio de tipo de dato para la columna Capital, que muy posiblemente corresponde al ID de la ciudad capital.
if 'Capital' in df_country.columns:
    df_country['Capital'] = df_country['Capital'].astype('Int64')

# Redondear  a un decimal la columna 'LifeExpectancy'
df_country['LifeExpectancy'] = df_country['LifeExpectancy'].round(1)

# Transformación y enriquecimiento de datos

# Crear columna EsIndependizado ✅ "Sí" → País con año de independencia registrado. ❌ "No aplica" → País sin independencia registrada.
df_country.insert(df_country.columns.get_loc("IndepYear") + 1, "EsIndependizado", 
                np.where(df_country["IndepYear"].isna(), "No aplica", "Sí"))

# Llenar valores nulos de GNPOld con la mediana de GNP
df_country['GNPOld'] = df_country['GNPOld'].fillna(df_country['GNP'].median())

# 🔹 Completar los valores nulos en la columna 'HeadOfState' con datos verificados externamente.

# Verificar si se cargó correctamente antes de modificarlo
if df_country is not None:
    def jefes_estado_2002(df):
        jefes_estado_corregidos = {
            'AND': 'Coprincipe episcopal - Joan-Enric Vives i Sicília y Coprincipe francés -Jacques Chirac',
            'SMR': '1er semestre - Giuseppe Arzilli y Gian Carlo Venturini y 2do semestre - Roberto Giorgetti y Giovanni Lonfernini'
        }
        # Reemplazar los valores nulos en la columna "HeadOfState"
        df.loc[df["Code"].isin(jefes_estado_corregidos.keys()), "HeadOfState"] = df["Code"].map(jefes_estado_corregidos)
        return df
    # Aplicar la función
    df_country = jefes_estado_2002 (df_country)

# 🔹 Completar el campo Code2 con "NA" para mantener la coherencia del dataset

# Verificar si 'Code2' existe en el DataFrame
if "Code2" in df_country.columns:
    # Llenar solo los valores nulos para Namibia con su código correcto
    df_country.loc[df_country["Code"] == "NAM", "Code2"] = "NA"

# Guardar el CSV transformado
ruta_salida_country = os.path.join(os.path.dirname(__file__), "..", "datos_csv", "country.csv")
df_country.to_csv(ruta_salida_country, index=False)
print(f"\n✅ Limpieza de datos df COUNTRY: Archivo actualizado y guardado en: {ruta_salida_country}")