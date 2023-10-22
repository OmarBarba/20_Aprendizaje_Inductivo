
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Cargar el conjunto de datos Iris
iris = load_iris()
X, y = iris.data, iris.target

# Crear un clasificador de árbol de decisión
clf = DecisionTreeClassifier()

# Entrenar el clasificador
clf.fit(X, y)

# Realizar una predicción
nueva_instancia = [[5.1, 3.5, 1.4, 0.2]]
prediccion = clf.predict(nueva_instancia)
print("Clase predicha:", iris.target_names[prediccion])
