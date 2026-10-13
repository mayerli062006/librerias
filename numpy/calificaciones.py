import numpy as np

# Creamos una matriz con las notas de los estudiantes
notas = np.array([
    [3.5, 4.0, 2.2, 5.0],
    [4.4, 5.0, 3.0, 3.0],
    [5.0, 3.8, 4.6, 4.0]
])

# Calculamos el promedio de cada estudiante
print("Promedio de cada estudiante:")
print(notas.mean(axis=1))

# Calculamos el promedio de cada materia
print("Promedio de cada materia:")
print(notas.mean(axis=0))

# Mostramos el tamaño de la matriz
print("Tamano de la matriz:")
print(notas.shape)

# Mostramos las notas del primer estudiante
print("Notas del primer estudiante:")
print(notas[0])

# Mostramos las notas de la segunda materia
print("Notas de la segunda materia:")
print(notas[:, 1])