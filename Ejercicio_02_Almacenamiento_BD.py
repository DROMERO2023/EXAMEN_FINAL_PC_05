# EXAMEN FINAL - DENNIS A. ROMERO ROJAS
# Ejercicio 02 - ALMACENAMIENTO SOBRE BASE DE DATOS

import matplotlib.pyplot as plt
import pandas as pd
import xlsxwriter
import sqlite3
import os

DB = 'candidates.db'
TABLE_NAME = 'candidate'

def almacenar_pandas_to_sql(df: pd.DataFrame, database_name: str, table_name: str) -> None:
    """Procesamiento datos candidatos para almacenarlos sobre db """

    # rename columns
    column_rename = {c: c.replace(' ', '') for c in df.columns}
    df.rename(column_rename, axis='columns', inplace=True)

    # Almaceno sobre db
    with sqlite3.connect(database_name) as conn:
        df.to_sql(table_name, conn, index=False, if_exists='replace')

    sql_table_schema = f'{database_name}.{table_name}'
    cantidad_registros = df.shape[0]
    print(f'Se almacenaron {cantidad_registros} sobre tabla sql {sql_table_schema}')

# read csv
path = './src/candidates.csv'
df = pd.read_csv(path, sep=';')
df.shape
df.head(2)
almacenar_pandas_to_sql(df, DB, TABLE_NAME)