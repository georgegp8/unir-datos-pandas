import json

notebook = {
    "cells": [
        # Título principal
        {
            "cell_type": "markdown",
            "id": "main_title",
            "metadata": {},
            "source": [
                "# Conceptos Basicos de Fusion de Datos - Parte 1\n",
                "\n",
                "Aprenderás los conceptos fundamentales de fusión de datos usando pandas."
            ]
        },
        # Setup
        {
            "cell_type": "code",
            "execution_count": None,
            "id": "setup_imports",
            "metadata": {},
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "\n",
                "# Carga de los dataframes\n",
                "taxi_owners = pd.read_csv('../taxi_owners.csv')\n",
                "taxi_veh = pd.read_csv('../taxi_vehicles.csv')\n",
                "wards = pd.read_csv('../Chicago_wards.csv')\n",
                "census = pd.read_csv('../Chicago_census.csv')\n",
                "\n",
                "# Copias alteradas para comparar fusiones internas\n",
                "wards_altered = wards.copy()\n",
                "census_altered = census.copy()\n",
                "wards_altered.loc[0, 'ward'] = -1\n",
                "census_altered.loc[0, 'ward'] = -1"
            ]
        },
        # Sección 1
        {
            "cell_type": "markdown",
            "id": "section1_title",
            "metadata": {},
            "source": [
                "## Sección 1: ¿Qué columna elegiremos para fusionar?\n",
                "\n",
                "Chicago proporciona una lista de propietarios de taxis y vehículos con licencia para operar en la ciudad, por seguridad pública. Tu objetivo es unir dos tablas. Una tabla se llama `taxi_owners` y contiene información sobre los propietarios de las empresas de taxis, mientras que la otra se llama `taxi_veh` e incluye información sobre cada vehículo de taxi."
            ]
        },
        {
            "cell_type": "markdown",
            "id": "section1_instr",
            "metadata": {},
            "source": [
                "### Instrucciones 1/1\n",
                "Elige la columna correcta para fusionar ambas tablas.\n",
                "\n",
                "Respuestas posibles:\n",
                "- on='rid'\n",
                "- on='vid'\n",
                "- on='year'\n",
                "- on='zip'\n",
                "\n",
                "Respuesta correcta: on='vid'"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "id": "section1_code",
            "metadata": {},
            "outputs": [],
            "source": [
                "taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid')\n",
                "\n",
                "print(taxi_own_veh.columns)"
            ]
        },
        # Sección 2
        {
            "cell_type": "markdown",
            "id": "section2_title",
            "metadata": {},
            "source": [
                "## Sección 2: Tu Primera Unión Interna\n",
                "\n",
                "Te han encargado que averigües cuáles son los tipos de combustible más utilizados en los taxis de Chicago. Para completar el análisis, tienes que fusionar las tablas `taxi_owners` y `taxi_veh`."
            ]
        },
        {
            "cell_type": "markdown",
            "id": "section2_instr1",
            "metadata": {},
            "source": [
                "### Instrucciones 1/3\n",
                "Fusiona `taxi_owners` con `taxi_veh` en la columna `vid`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "id": "section2_code1",
            "metadata": {},
            "outputs": [],
            "source": [
                "taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid')\n",
                "\n",
                "print(taxi_own_veh.columns)"
            ]
        },
        {
            "cell_type": "markdown",
            "id": "section2_instr2",
            "metadata": {},
            "source": [
                "### Instrucciones 2/3\n",
                "Establece los sufijos `_own` y `_veh` para las columnas solapadas."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "id": "section2_code2",
            "metadata": {},
            "outputs": [],
            "source": [
                "taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own', '_veh'))\n",
                "\n",
                "print(taxi_own_veh.columns)"
            ]
        },
        {
            "cell_type": "markdown",
            "id": "section2_instr3",
            "metadata": {},
            "source": [
                "### Instrucciones 3/3\n",
                "Selecciona la columna `fuel_type` e imprime `.value_counts()` para encontrar los tipos de combustible más utilizados."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "id": "section2_code3",
            "metadata": {},
            "outputs": [],
            "source": [
                "print(taxi_own_veh['fuel_type'].value_counts())"
            ]
        },
        # Sección 3
        {
            "cell_type": "markdown",
            "id": "section3_title",
            "metadata": {},
            "source": [
                "## Sección 3: Uniones internas y número de filas devueltas\n",
                "\n",
                "Todas las fusiones que has estudiado hasta ahora se llaman uniones internas. Es necesario comprender que las uniones internas solo devuelven las filas con valores coincidentes en ambas tablas. Para este ejercicio, las tablas `wards` y `census` empiezan con 50 filas."
            ]
        },
        {
            "cell_type": "markdown",
            "id": "section3_instr1",
            "metadata": {},
            "source": [
                "### Instrucciones 1/3\n",
                "Fusiona `wards` y `census` en la columna `ward` y guarda el resultado en `wards_census`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "id": "section3_code1",
            "metadata": {},
            "outputs": [],
            "source": [
                "wards_census = wards.merge(census, on='ward')\n",
                "print('wards_census table shape:', wards_census.shape)"
            ]
        },
        {
            "cell_type": "markdown",
            "id": "section3_instr2",
            "metadata": {},
            "source": [
                "### Instrucciones 2/3\n",
                "Fusiona `wards_altered` y `census` en la columna `ward` y observa la diferencia en las filas devueltas."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "id": "section3_code2",
            "metadata": {},
            "outputs": [],
            "source": [
                "print(wards_altered[['ward']].head())\n",
                "wards_altered_census = wards_altered.merge(census, on='ward')\n",
                "print('wards_altered_census table shape:', wards_altered_census.shape)"
            ]
        },
        {
            "cell_type": "markdown",
            "id": "section3_instr3",
            "metadata": {},
            "source": [
                "### Instrucciones 3/3\n",
                "Fusiona `wards` y `census_altered` en la columna `ward` y observa la diferencia en las filas devueltas."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "id": "section3_code3",
            "metadata": {},
            "outputs": [],
            "source": [
                "print(census_altered[['ward']].head())\n",
                "wards_census_altered = wards.merge(census_altered, on='ward')\n",
                "print('wards_census_altered table shape:', wards_census_altered.shape)"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Write the notebook
with open(r'c:/Users/George/Downloads/unir-datos-pandas/1.conceptos-basicos-fusion-datos/1.1.union-interna.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Notebook creado exitosamente: 1.1.union-interna.ipynb")
