# ================================================
# Conceptos Basicos de Fusion de Datos - Parte 1
# ================================================

import pandas as pd

# Carga de los dataframes
taxi_owners = pd.read_csv('../taxi_owners.csv')
taxi_veh = pd.read_csv('../taxi_vehicles.csv')
wards = pd.read_csv('../Chicago_wards.csv')
census = pd.read_csv('../Chicago_census.csv')

# Copias alteradas para comparar fusiones internas
wards_altered = wards.copy()
census_altered = census.copy()
wards_altered.loc[0, 'ward'] = -1
census_altered.loc[0, 'ward'] = -1

# ------------------------------------------------
# Sección 1: ¿Qué columna elegiremos para fusionar?
# ------------------------------------------------
# Chicago proporciona una lista de propietarios de taxis y vehículos con licencia
# para operar en la ciudad, por seguridad pública. Tu objetivo es unir dos tablas.
# Una tabla se llama `taxi_owners` y contiene información sobre los propietarios de
# las empresas de taxis, mientras que la otra se llama `taxi_veh` e incluye
# información sobre cada vehículo de taxi.

# Instrucción 1: Elige la columna correcta para fusionar ambas tablas.
# Respuestas posibles:
# - on='rid'
# - on='vid'
# - on='year'
# - on='zip'
# Respuesta correcta: on='vid'
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid')

# Código de verificación de la respuesta
print(taxi_own_veh.columns)

# ------------------------------------------------
# Sección 2: Tu Primera Unión Interna
# ------------------------------------------------
# Te han encargado que averigües cuáles son los tipos de combustible más utilizados 
# en los taxis de Chicago. Para completar el análisis, tienes que fusionar las tablas 
# `taxi_owners` y `taxi_veh`.

# Instrucción 1: Fusiona `taxi_owners` con `taxi_veh` en la columna `vid`.
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid')

# Código de verificación para la instrucción 1
print(taxi_own_veh.columns)

# Instrucción 2: Establece los sufijos `_own` y `_veh` para las columnas solapadas.
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own', '_veh'))

# Código de verificación para las instrucciones 1 y 2
print(taxi_own_veh.columns)

# Instrucción 3: Selecciona la columna `fuel_type` e imprime `.value_counts()` 
# para encontrar los tipos de combustible más utilizados.
print(taxi_own_veh['fuel_type'].value_counts())

# ------------------------------------------------
# Sección 3: Uniones internas y numero de filas devueltas
# ------------------------------------------------
# Todas las fusiones que has estudiado hasta ahora se llaman uniones internas.
# Es necesario comprender que las uniones internas solo devuelven las filas con
# valores coincidentes en ambas tablas. Para este ejercicio, las tablas `wards`
# y `census` empiezan con 50 filas.

# Instrucción 1: Fusiona `wards` y `census` en la columna `ward` y guarda
# el resultado en `wards_census`.
wards_census = wards.merge(census, on='ward')
print('wards_census table shape:', wards_census.shape)

# Instrucción 2: Fusiona `wards_altered` y `census` en la columna `ward`
# y observa la diferencia en las filas devueltas.
print(wards_altered[['ward']].head())
wards_altered_census = wards_altered.merge(census, on='ward')
print('wards_altered_census table shape:', wards_altered_census.shape)

# Instrucción 3: Fusiona `wards` y `census_altered` en la columna `ward`
# y observa la diferencia en las filas devueltas.
print(census_altered[['ward']].head())
wards_census_altered = wards.merge(census_altered, on='ward')
print('wards_census_altered table shape:', wards_census_altered.shape)
