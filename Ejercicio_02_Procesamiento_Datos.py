# EXAMEN FINAL - DENNIS A. ROMERO ROJAS
# Ejercicio 02 - PROCESAMIENTO DE DATOS

import sqlite3
import os
import pandas as pd
import matplotlib.pyplot as plt

DB = 'candidates.db'  # Asegúrate de que DB tenga el valor correcto según tu configuración
TABLE_NAME = 'candidate'

# 1. Lectura de datos
with sqlite3.connect(DB) as conn:
    df = pd.read_sql_query(f'select * from {TABLE_NAME}', conn)
df.head(2)

# 2. Filtrado de datos
listado_paises = ['United States of America', 'Brazil', 'Colombia', 'Ecuador']

# Asegúrate de que el nombre de la columna sea 'TechnicalInterviewScore'
filterDf = df[df['Country'].isin(listado_paises) & (df['CodeChallengeScore'] >= 7) & (df['TechnicalInterviewScore'] >= 7)]

# Funciones de generación de gráficos y reportes...
def genero_grafico_circular(df: pd.DataFrame, country: str) -> None:
    """Funcion que se encarga de crear el gráfico en pie"""
    tec = df.groupby('Technology')['Technology'].count()
    tec.plot.pie(figsize=(11, 7))

    plt.savefig(f"./reportes/images/{country}/pie_chart.png", dpi=300, bbox_inches='tight')
    plt.close()
    print('Se genero gráfico circular ...')

def genero_grafico_barras(df: pd.DataFrame, country: str) -> None:
    """Funcion que se encarga de crear el gráfico de barras"""
    senority_group = df.groupby('Seniority')['Seniority'].count()
    senority_group.plot.bar()

    plt.savefig(f"./reportes/images/{country}/bar_chart.png", dpi=300, bbox_inches='tight')
    plt.close()
    print('Se genero gráfico barras ...')

# genero carpetas necesarias
if not os.path.isdir('./reportes'):
    os.mkdir('reportes')
    os.mkdir('./reportes/images')

# Procesamiento y generación de reportes...
for country in listado_paises:
    # creo subcarpetas
    if not os.path.isdir(f'./reportes/images/{country}'):
        os.mkdir(f'./reportes/images/{country}')

    # filtro df
    countryDf = filterDf[filterDf['Country'] == country]

    # genero gráficos
    genero_grafico_circular(countryDf, country)
    genero_grafico_barras(countryDf, country)

    # Genero reporte Excel por pais
    with pd.ExcelWriter(f"./reportes/{country}.xlsx", engine="xlsxwriter") as excelBook:
        sheet_name = f"Report-{country}"
        countryDf.to_excel(excelBook, index=False, sheet_name=sheet_name)

        # posiciono sobre hoja de excel
        excel_sheet = excelBook.sheets[sheet_name]

        # almaceno imagen
        image_pie_path = f"./reportes/images/{country}/pie_chart.png"
        image_bar_path = f"./reportes/images/{country}/bar_chart.png"

        excel_sheet.insert_image(1, countryDf.shape[1]+2, image_pie_path)  # 1 y df.shape +2 -> establecen posicion de imagen en libro
        excel_sheet.insert_image(countryDf.shape[0]+2, countryDf.shape[1]+2, image_bar_path)

        # Guardo cambios sobre excel
        # excelBook.close()

        print(f'Se generó reporte para el país {country}')

print('Se finalizó la generación de reportes')
