# importamos la libreria numpy
import numpy as np

# lista con las notas de los estudiantes
notas = np.array(
    [
        [7.5, 8.0, 6.5],
        [9.0, 5.5, 8.5],
    ]
)
# Calculamos las estadísticas solicitadas usando funciones de NumPy
promedio = np.mean(notas)
maximo = np.max(notas)
minimo = np.min(notas)
desviacion = np.std(notas)

# Mostramos los resultados en consola de forma clara
print("estadisticas de las notas del grupo:")
print(f"Notas originales: {notas}")
print(f"Promedio: {promedio:.2f}")
print(f"Nota maxima: {maximo}")
print(f"Nota minima: {minimo}")
print(f"Desviacion estandar: {desviacion:.2f}")
