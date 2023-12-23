# EXAMEN FINAL - DENNIS A. ROMERO ROJAS
# Ejercicio - CASO 02: Roberto y Clara.

import pandas as pd
import os

# Ingresa la ruta correcta del archivo CSV
ruta_archivo = "./src/airbnb.csv"

# Lee el archivo CSV
df_airbnb = pd.read_csv(ruta_archivo)

# IDs de las casas de Roberto y Clara
id_roberto = 97503
id_clara = 90387

# Filtrar propiedades de Roberto y Clara por room_id
df_roberto = df_airbnb[df_airbnb['room_id'].isin([id_roberto])]
df_clara = df_airbnb[df_airbnb['room_id'].isin([id_clara])]

# Concatenar ambos dataframes
df_roberto_clara = pd.concat([df_roberto, df_clara])

# Mostrar el dataframe combinado en la terminal
print(df_roberto_clara)

# Guardar el dataframe en un archivo Excel (.xlsx en lugar de .xls)
nombre_archivo_excel = "roberto.xlsx"
ruta_completa_excel = os.path.abspath(nombre_archivo_excel)
df_roberto_clara.to_excel(nombre_archivo_excel, index=False, engine='openpyxl')

# Mostrar mensaje de generación del archivo con la ruta completa
print(f"Se ha generado el archivo Excel en la ruta: {ruta_completa_excel}")
