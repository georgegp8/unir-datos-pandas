# ================================================
# Conceptos Basicos de Fusion de Datos
# ================================================

# ------------------------------------------------
# Seccion 1: Clasificacion de uno a muchos
# ------------------------------------------------
# Entender la diferencia entre una relacion de uno a uno y una relacion de uno
# a muchos es una habilidad util. En este ejercicio, trabajaremos con un conjunto
# de tablas de un sitio web de comercio electronico. Las tablas hipoteticas son
# las siguientes:
# - Una tabla customer con informacion sobre cada cliente.
# - Una tabla cust_tax_info con los identificadores fiscales unicos de los clientes.
# - Una tabla orders con informacion sobre cada pedido.
# - Una tabla products con detalles sobre cada producto unico vendido.
# - Una tabla inventory con informacion sobre cuanto inventario total hay disponible
#   para vender de cada producto.

# Instrucciones:
# Selecciona el tipo de relacion mas adecuado para la relacion entre las distintas
# tablas: de uno a uno o bien de uno a muchos.

# Solucion:
# Uno a uno
uno_a_uno = [
	("customer", "cust_tax_info"),
	("products", "inventory"),
]

# Uno a muchos
uno_a_muchos = [
	("products", "orders"),
	("customers", "orders"),
]

# ------------------------------------------------
# Seccion 2: Fusion de uno a muchos
# ------------------------------------------------
# Una empresa puede tener uno o varios propietarios. En este ejercicio, seguiras
# adquiriendo experiencia con las uniones de uno a muchos fusionando una tabla de
# propietarios de empresas, llamada biz_owners, con la tabla licenses.
#
# Instrucciones:
# - Empezando por la tabla licenses de la izquierda, combinala con la tabla
#   biz_owners en la columna account y guarda el resultado en licenses_owners.
# - Agrupa licenses_owners por title y cuenta el numero de cuentas de cada titulo.
#   Guarda el resultado como counted_df.
# - Ordena counted_df por el numero de cuentas en orden descendente y guardalo como
#   sorted_df.
# - Utiliza el metodo .head() para imprimir las primeras filas de sorted_df.

import pandas as pd
from pathlib import Path

# Carga de los dataframes
licenses = pd.read_csv('../data/licenses.csv')
biz_owners = pd.read_csv('../data/business_owners.csv')

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account': 'count'})

# Sort the counted_df in descending order
sorted_df = counted_df.sort_values('account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())
