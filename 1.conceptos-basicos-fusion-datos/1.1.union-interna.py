# =================================================================
# Conceptos Básicos de Fusión de Datos: Unión Interna
# Ejercicios: Fusionando DataFrames con Pandas
# =================================================================

# ------------------------------------------------
# Sección 1: Fusión de DataFrames de Taxis
# ------------------------------------------------
# Chicago proporciona una lista de propietarios de taxis y vehículos con licencia 
# para operar en la ciudad, por seguridad pública. Tu objetivo es unir dos tablas. 
# Una tabla se llama `taxi_owners` y contiene información sobre los propietarios 
# de las empresas de taxis, mientras que la otra se llama `taxi_veh` e incluye 
# información sobre cada vehículo de taxi. Se han cargado las tablas `taxi_owners` y
# `taxi_veh` para que las explores.

# Instrucciones:
# - Fusiona los DataFrames `taxi_owners` y `taxi_veh` en la columna `vid`.
# - Imprime las primeras 5 filas del DataFrame resultante.
# - Imprime el número de filas y columnas del DataFrame resultante.

# Importar pandas
import pandas as pd

# Carga de los dataframes
taxi_owners = pd.read_csv('../taxi_owners.csv')
taxi_veh = pd.read_csv('../taxi_vehicles.csv')

# Inspección de los dataframes
print("Contenido de taxi_owners:")
print(taxi_owners.head())
print("\nContenido de taxi_veh:")
print(taxi_veh.head())

# Unión de los dataframes en la columna 'vid'
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid')

# Imprimir las 5 primeras filas de la unión
print("\nDataFrame fusionado (primeras 5 filas):")
print(taxi_own_veh.head())

# Imprimir el número de filas y columnas
print("\nDimensiones del DataFrame fusionado:")
print(taxi_own_veh.shape)

# ------------------------------------------------
# Pregunta del Ejercicio
# ------------------------------------------------
#
# ¿Qué columna elegiremos para fusionar?
#
# Respuestas posibles:
#   - on='rid'
#   - on='vid'  <- Correcta
#   - on='year'
#   - on='zip'