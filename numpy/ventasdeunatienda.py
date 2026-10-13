import numpy as np

# Creamos un arreglo con las ventas
ventas = np.array([120000, 950000, 150000, 80000, 200000, 175000, 110000, 110000])

# Aumentamos las ventas en un 10 %
ventas = ventas * 1.10

# Mostramos las ventas actualizadas
print("Ventas con aumento del 10 %:")
print(ventas)

# Calculamos el total de las ventas
print("Total de las ventas:")
print(ventas.sum())