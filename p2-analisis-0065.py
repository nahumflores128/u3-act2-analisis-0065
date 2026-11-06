# importar librerias
import pandas as pd
import numpy as np
print("Analisis de datos alumnos Nahum Flores NC=0065")
inmuebles = {
    "Id_Casa": [101, 102, 103, 104, 105, 106],
    "Metros_Cuadrados": [65, 120, 85, 200, 150, 95],
    "Habitaciones": [2, 4, 3, 5, 4, 3],
    "Precio_Miles_USD": [150, 310, 210, 480, 390, 240]
}

df = pd.DataFrame(inmuebles)
print(df)
print("-+--++--+-+ AGRUPAR COLUMNAS -+-+-+-+-+-+-+-+")
agrupado = df.groupby('Metros_Cuadrados')
print(agrupado)
print("-+--++--+-+ POR AGREGACION -+-+-+-+-+-+-+-+")
# Habitaciones
print(agrupado['Habitaciones'].mean())
print("-+-+-+-+--+ muebles maximo -++-+--++-+-+--++")
# Precio_Miles_USD
print(agrupado['Precio_Miles_USD'].max())



