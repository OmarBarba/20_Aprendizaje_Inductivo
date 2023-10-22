import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo (tamaño de la casa y precio)
tamanio_casas = np.array([1400, 1600, 1700, 1875, 1100])
precio_casas = np.array([245000, 312000, 279000, 308000, 199000])

# Modelo de regresión lineal
def regresion_lineal(x, y):
    n = len(x)
    pendiente = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x))**2)
    interseccion = (np.sum(y) - pendiente * np.sum(x)) / n
    return pendiente, interseccion

pendiente, interseccion = regresion_lineal(tamanio_casas, precio_casas)

# Realizar una predicción para una casa de 1500 pies cuadrados
tamanio_prediccion = 1500
precio_prediccion = pendiente * tamanio_prediccion + interseccion

# Mostrar la explicación de la predicción
print(f"Predicción: El precio de una casa de {tamanio_prediccion} pies cuadrados es aproximadamente ${precio_prediccion:.2f}.")
print(f"Factor de Influencia: Por cada pie cuadrado adicional, el precio aumenta en ${pendiente:.2f}.")

# Graficar los datos y la línea de regresión
plt.scatter(tamanio_casas, precio_casas, label='Datos de entrenamiento')
plt.plot(tamanio_casas, pendiente * tamanio_casas + interseccion, color='red', label='Línea de Regresión')
plt.xlabel('Tamaño de la Casa (pies cuadrados)')
plt.ylabel('Precio de la Casa')
plt.legend()
plt.show()
