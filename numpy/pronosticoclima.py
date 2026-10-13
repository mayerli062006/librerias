import numpy as np

# Creamos un arreglo con temperaturas en Celsius
celsius = np.array([18, 22, 25, 19, 30])

# Convertimos las temperaturas a Fahrenheit
fahrenheit = celsius * 9 / 5 + 32

# Mostramos las temperaturas en Celsius
print("Temperaturas en Celsius:")
print(celsius)

# Mostramos las temperaturas en Fahrenheit
print("Temperaturas en Fahrenheit:")
print(fahrenheit)