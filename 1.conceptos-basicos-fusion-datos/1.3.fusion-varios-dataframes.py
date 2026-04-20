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

# ------------------------------------------------
# Seccion 3: Fusion de uno a muchos con varias tablas
# ------------------------------------------------
# En esta seccion, uniras las tablas land_use, census y licenses para analizar
# como se relacionan poblacion, lotes vacantes y numero de cuentas.

# Carga de los dataframes para la seccion 3
land_use = pd.read_csv('../land_use.csv')
census = pd.read_csv('../Chicago_census.csv')
licenses = pd.read_csv('../licenses.csv')

# Instruccion 1: Fusiona land_use con census en ward. Luego fusiona con licenses
# en ward usando sufijos _cen para la tabla izquierda y _lic para la derecha.
land_cen_lic = land_use.merge(census, on='ward') \
					   .merge(licenses, on='ward', suffixes=('_cen', '_lic'))

# Instruccion 2: Agrupa land_cen_lic por ward, pop_2010 y vacant. Luego cuenta
# el numero de accounts. Guarda el resultado en pop_vac_lic.
pop_vac_lic = land_cen_lic.groupby(['ward', 'pop_2010', 'vacant'], as_index=False) \
						 .agg({'account': 'count'})

# Instruccion 3: Ordena pop_vac_lic por vacant (desc), account (asc) y pop_2010
# (asc). Guarda en sorted_pop_vac_lic e imprime las primeras filas.
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant', 'account', 'pop_2010'],
											 ascending=[False, True, True])
print(sorted_pop_vac_lic.head())
