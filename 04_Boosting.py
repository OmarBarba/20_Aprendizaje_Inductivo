from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X, y = iris.data, iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear un clasificador de AdaBoost
clf = AdaBoostClassifier(n_estimators=50)

# Entrenar el clasificador
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
predicciones = clf.predict(X_test)

# Calcular la precisión
precision = accuracy_score(y_test, predicciones)
print("Precisión:", precision)
