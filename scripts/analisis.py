import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px

df = pd.read_csv("C:/Users/User/OneDrive/Escritorio/Analisis de Ventas/datos/datos_ventas.csv")
df["Fecha"] = pd.to_datetime(df["Fecha"])
df["Mes"] = df["Fecha"].dt.month_name()
df["Dia"] = df["Fecha"].dt.day_name()

#Exploratory Data Analysis

##Cantidad de productos

fig = px.histogram(df, x="Producto", hover_data=df.columns, title="Productos")
fig.show()

## Uso frecuente de metodo de pago

fig = px.histogram(df, x="Metodo de pago", hover_data=df.columns, title="Metodos de pagos")
fig.show()

## Ventas totales por producto

ventas_por_producto = df.groupby('Producto')['Cantidad'].sum().sort_values(ascending=False)
ventas_por_producto_df = ventas_por_producto.reset_index()

fig = px.bar(ventas_por_producto_df, x='Producto', y='Cantidad',
             title='Ventas Totales por producto', labels= {'Cantidad':'Ventas', 'Producto':'Producto'})
fig.show()

## Ingresos por ciudad

ingresos_por_ciudad = df.groupby('Ciudad')['Precio'].sum().sort_values(ascending=False)
ingresos_por_ciudad_df = ingresos_por_ciudad.reset_index()

fig = px.bar(ingresos_por_ciudad_df, x='Ciudad', y='Precio',
             title='Ingresos Totales por Ciudad', labels= {'Precio':'Ingresos', 'Ciudad':'Ciudad'})
fig.show()

## Ventas totales por ciudad

ventas_por_ciudad = df.groupby('Ciudad')['Cantidad'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
ventas_por_ciudad.plot(kind='bar')
plt.title('Ventas Totales por Ciudad')
plt.ylabel('Cantidad Vendida')
plt.xticks(rotation=45)
plt.show()

## Precio Promedio por producto 

precios_por_producto = df.groupby('Producto')['Precio'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
precios_por_producto.head(10).plot(kind='bar')
plt.title('Precio Promedio por Producto')
plt.ylabel('Precio Promedio')
plt.xticks(rotation=45)
plt.show()

## Ventas totales por Mes

precios_por_producto = df.groupby('Mes')['Cantidad'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
precios_por_producto.head(10).plot(kind='bar')
plt.title('Ventas Totales por Mes')
plt.ylabel('Cantidad de Ventas')
plt.xticks(rotation=45)
plt.show()

## Ventas por dia de semana

ventas_por_dia = df.groupby('Dia')['Cantidad'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
ventas_por_dia.plot(kind='bar')
plt.title('Ventas por Día de la Semana')
plt.xlabel('Día')
plt.ylabel('Cantidad Vendida')
plt.xticks(rotation=45)
plt.show()

##Ingresos totales por dia

ingresos_por_dia = df.groupby('Dia')['Precio'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
ingresos_por_dia.plot(kind='bar')
plt.title('Ingresos Totales por Dia')
plt.xlabel('Día')
plt.ylabel('Ingresos')
plt.xticks(rotation=45)
plt.show()