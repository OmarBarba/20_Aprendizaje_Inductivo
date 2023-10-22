import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo (horas de estudio y calificaciones)
horas_de_estudio = np.array([1, 2, 3, 4, 5])
calificaciones = np.array([2, 4, 7, 9, 11])

# Función para calcular la regresión lineal
def regresion_lineal(x, y):
    n = len(x)
    suma_x = np.sum(x)
    suma_y = np.sum(y)
    suma_x2 = np.sum(x**2)
    suma_xy = np.sum(x * y)

    pendiente = (n * suma_xy - suma_x * suma_y) / (n * suma_x2 - suma_x**2)
    interseccion = (suma_y - pendiente * suma_x) / n

    return pendiente, interseccion

# Calcular la pendiente e intersección de la mejor hipótesis (modelo)
pendiente, interseccion = regresion_lineal(horas_de_estudio, calificaciones)

# Graficar los datos y la mejor hipótesis
plt.scatter(horas_de_estudio, calificaciones, label='Datos de entrenamiento')
plt.plot(horas_de_estudio, pendiente * horas_de_estudio + interseccion, color='red', label='Mejor Hipótesis')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificaciones')
plt.legend()
plt.show()

print(f"La mejor hipótesis actual (modelo de regresión): Calificación = {pendiente:.2f} * Horas de Estudio + {interseccion:.2f}")
