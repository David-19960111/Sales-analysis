import pandas as pd 
from faker import Faker
import random 

faker = Faker()

num_rows = 5236
data = {
    "Fecha" : [faker.date_between(start_date = '-1y', end_date = 'today') for _ in range(num_rows)],
    "Producto" : [random.choice(["Laptop", "Smartphone", "Camiseta", "Zapatos", "Auriculares"]) for _ in range(num_rows)],
    "Precio": [round(random.uniform(10, 500), 2) for _ in range(num_rows)],
    "Cantidad": [random.randint(1, 5) for _ in range(num_rows)],
    "Ciudad": [random.choice(["Buenos Aires", "Cordoba", "Tucuman", "Rio Negro", "San Luis", "Santa Fe", "Tierra del Fuego", "Salta", "Jujuy", "Neuquen"]) for _ in range(num_rows)],
    "Metodo de pago": [random.choice(["Tarjeta de crédito", "Efectivo", "Transferencia"]) for _ in range(num_rows)]
}

df = pd.DataFrame(data)

df.to_csv("datos_ventas.csv", index=False)

print("Archivo 'datos_ventas.csv' creado con éxito.")