# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 10:30:00 2021

@author: Andrés Díaz
"""

import pandas as pd

"""
Tomando como base la información suministrada de casos de Covid-19 en
Colombia.
Realice las líneas de código en Python que den respuesta a las siguientes
preguntas:
"""

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

data['Nombre municipio'].replace(
    'puerto colombia', 'PUERTO COLOMBIA', inplace=True)

data['Nombre departamento'].replace('Tolima', 'TOLIMA', inplace=True)
data['Nombre departamento'].replace('Caldas', 'CALDAS', inplace=True)

data['Ubicación del caso'].replace('casa', 'Casa', inplace=True)
data['Ubicación del caso'].replace('CASA', 'Casa', inplace=True)

data.Sexo.replace('f', 'F', inplace=True)
data.Sexo.replace('m', 'M', inplace=True)

# 1. Número de casos de Contagiados en el País.

print(f'Número de casos de contagiados en el país: {data.shape[0]}')

# 2. Número de Municipios Afectados

numero_municipios_afectados = len(data['Nombre municipio'].value_counts())
print(f'Número de municipios afectados: {numero_municipios_afectados}')

# 3. Liste los municipios afectados (sin repetirlos)

nombre_municipios = data['Nombre municipio'].unique()
count = 0
print('Lista de municipios afectados (sin repeticiones)')
for municipio in nombre_municipios:
    count += 1
    print(f'#{count}. {municipio}')


# 4. Número de personas que se encuentran en atención en casa

data['Ubicación del caso'].value_counts()
casos_casa = data[data['Ubicación del caso'] == 'Casa'].shape[0]
print(f'Número de personas con atención en casa: {casos_casa}')


# 5.Número de personas que se encuentran recuperados

data['Recuperado'].value_counts()
personas_recuperadas = data[data['Recuperado'] == 'Recuperado'].shape[0]
print(f'Número de personas recuperadas: {personas_recuperadas}')

# 6. Número de personas que ha fallecido

personas_fallecidas = data[data.Estado == 'Fallecido'].shape[0]
print(f'Número de personas fallecidas: {personas_fallecidas}')

# 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,
# Relacionado)

print('Listar de mayor a menor por tipo de caso (Importado, en estudio,'
      'Relacionado)')
data["Tipo de contagio"].value_counts()
