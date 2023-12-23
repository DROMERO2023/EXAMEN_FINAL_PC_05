# EXAMEN FINAL - DENNIS A. ROMERO ROJAS
# Ejercicio - CASO 03: CLARA

import pandas as pd

# Ingresa la ruta correcta del archivo CSV
ruta_archivo = "./src/airbnb.csv"

# Lee el archivo CSV
df_airbnb = pd.read_csv(ruta_archivo)

# Condiciones del problema
condition_diana = (df_airbnb['accommodates'] >= 1) & (df_airbnb['price'] <= 50) & (df_airbnb['room_type'] == 'Shared room')

# Aplicar condiciones
df_filtered_diana = df_airbnb[condition_diana]

# Ordenamiento para habitaciones compartidas por precio y puntuación
df_ordered_diana = df_filtered_diana.sort_values(['price', 'overall_satisfaction'], ascending=[True, False])

# Top 10 propiedades más baratas para Diana
df_top10_diana = df_ordered_diana.head(10)

# Mostrar el resultado
print(df_top10_diana)
