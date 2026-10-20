import pandas as pd

# Creamos un diccionario con los datos del inventario
inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3],
}

# Convertimos el diccionario en una tabla
df = pd.DataFrame(inventario)

# Mostramos los primeros productos
print("Primeros productos del inventario:")
print(df.head())

# Mostramos el tamaño de la tabla
print("Tamaño de la tabla:")
print(df.shape)

# Mostramos los nombres de las columnas
print("Columnas del inventario:")
print(df.columns)

# Mostramos un resumen de los datos
print("Descripción del inventario:")
print(df.describe())
