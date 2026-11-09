# importar librerias
import pandas as pd
import numpy as np
print("Analisis de datos alumnos Nahum Flores NC=0065")
inmuebles = {
    "Id_Casa": [101, 102, 103, 104, 105, 106],
    "Metros_Cuadrados": [95, 120, 85, 200, 150, 95],
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

print("Nahum-+-+-+-++-+ segunda parte -+-+-+-+-+-+0065")
print("Agregaciones multiples ")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> minimo")
resultado_agregado = agrupado['Habitaciones'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)

print("Agrupacion por varias columnas")
print("Agrega columna al dataframe")
print("columna team --> equipp")
df['equipo'] = ['A','B','A','B','A','B']

agrupado_multiple = df.groupby(['Metros_Cuadrados', 'equipo'])['Habitaciones'].mean()
print(agrupado_multiple)


