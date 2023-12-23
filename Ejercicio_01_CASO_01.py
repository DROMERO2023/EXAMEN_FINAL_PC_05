# EXAMEN FINAL - DENNIS A. ROMERO ROJAS
# Ejercicio - CASO 01: ALICIA - Busqueda de Alojamiento en Airbnb.

import pandas as pd

# Ingresa la ruta correcta del archivo CSV
ruta_archivo = "./src/airbnb.csv"

# Configurar para mostrar todas las columnas
pd.set_option('display.max_columns', None)

# Lee el archivo CSV
df_airbnb = pd.read_csv(ruta_archivo)

# Condiciones del problema
condition = ((df_airbnb['reviews'] > 10) & (df_airbnb['overall_satisfaction'] > 4) & (df_airbnb['accommodates'] >= 4) & (df_airbnb['bedrooms'] >= 2))

# Aplicar condiciones
df_filtered = df_airbnb[condition]

# Ordenamiento
df_ordered = df_filtered.sort_values(['overall_satisfaction', 'reviews'], ascending=[False, False])

# Top 3
df_top3 = df_ordered.head(3)

# Mostrar el resultado con todas las columnas
print(df_top3)
