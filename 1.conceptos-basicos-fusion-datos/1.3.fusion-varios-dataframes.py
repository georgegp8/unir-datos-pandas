# ================================================
# Fusion de varios Dataframes
# ================================================

import pandas as pd

# Carga de los dataframes
cal = pd.read_csv('../cta_calendar.csv')
ridership = pd.read_csv('../cta_ridership.csv')
stations = pd.read_pickle('../stations.p')

# ------------------------------------------------
# Seccion 1: Total de usuarios en un mes
# ------------------------------------------------
# Tu objetivo es encontrar el numero total de viajes proporcionados a los
# pasajeros que pasan por la estacion Wilson cuando utilizan el sistema de
# transporte publico de Chicago en dias laborables de julio.
#
# Los DataFrames cal, ridership y stations se han cargado para ti.

# Instruccion 1: Fusiona las tablas ridership y cal empezando por la tabla
# ridership de la izquierda y guarda el resultado en ridership_cal.
ridership_cal = ridership.merge(cal, on=['year', 'month', 'day'])

# Instruccion 2: Amplia la fusion anterior a tres tablas fusionando tambien la
# tabla stations.
ridership_cal_stations = ridership.merge(cal, on=['year', 'month', 'day']) \
								  .merge(stations, on='station_id')

# Instruccion 3: Crea una variable llamada filter_criteria para seleccionar las
# filas adecuadas de la tabla combinada y poder sumar la columna rides.
filter_criteria = ((ridership_cal_stations['month'] == 7)
				   & (ridership_cal_stations['day_type'] == 'Weekday')
				   & (ridership_cal_stations['station_name'] == 'Wilson'))

print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

# ------------------------------------------------
# Seccion 2: Fusion de tres tablas
# ------------------------------------------------
# Para afianzar el concepto de fusion de tres DataFrame, fusionaras las tablas
# licenses y wards con la tabla zip_demo para analizar la renta media por codigo
# postal.
#
# Los DataFrames licenses, wards y zip_demo se han cargado para ti.

# Carga de los dataframes para la seccion 2
licenses = pd.read_csv('../licenses.csv')
wards = pd.read_csv('../Chicago_wards.csv')
zip_demo = pd.read_csv('../zip_demo.csv')

# Instruccion 1: Partiendo de licenses, fusiona con zip_demo en zip y luego con
# wards en ward. Guarda el resultado en licenses_zip_ward.
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
							.merge(wards, on='ward')

# Instruccion 2: Agrupa por alderman y calcula la mediana de income.
print(licenses_zip_ward.groupby('alderman').agg({'income': 'median'}))
