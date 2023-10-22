# Datos de entrenamiento: (Color, Sabor, Clase)
datos_entrenamiento = [
    ("rojo", "dulce", "manzana"),
    ("naranja", "dulce", "naranja"),
    ("rojo", "dulce", "manzana"),
    ("verde", "amargo", "manzana"),
    ("naranja", "dulce", "naranja"),
]

# Espacio de Versiones: Conjunto de todas las hipótesis consistentes con los datos
espacio_de_versiones = set()

for muestra in datos_entrenamiento:
    color, sabor, clase = muestra
    hipotesis = (color, sabor)
    espacio_de_versiones.add(hipotesis)

print("Espacio de Versiones (hipótesis consistentes):", espacio_de_versiones)
