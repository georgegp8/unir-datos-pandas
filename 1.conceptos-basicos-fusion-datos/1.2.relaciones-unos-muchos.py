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
