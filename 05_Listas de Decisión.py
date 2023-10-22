######################################################
#################   K-DL  ###########################
#####################################################
import random

class DecisionListNode(object):
    def __init__(self, point=None, label=None, left=None, right=None):
        self.point = point
        self.label = label
        self.left = left
        self.right = right

class DecisionList(object):
    def __init__(self):
        self.root = None

    def add(self, point, label):
        if not self.root:
            self.root = DecisionListNode(point=point, label=label)
        else:
            self._add(self.root, point, label)

    def _add(self, node, point, label):
        if point[0] < node.point[0]:
            if node.left:
                self._add(node.left, point, label)
            else:
                node.left = DecisionListNode(point=point, label=label)
        else:
            if node.right:
                self._add(node.right, point, label)
            else:
                node.right = DecisionListNode(point=point, label=label)

    def classify(self, point):
        if not self.root:
            return None
        return self._classify(self.root, point)

    def _classify(self, node, point):
        if point[0] < node.point[0]:
            if node.left:
                return self._classify(node.left, point)
            else:
                return node.label
        else:
            if node.right:
                return self._classify(node.right, point)
            else:
                return node.label

def random_points(count, dimensions):
    """Genera puntos aleatorios."""
    return [[random.randint(0, 100) for _ in range(dimensions)] for _ in range(count)]


######################################################
################# K-DT ###########################
#####################################################

import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

def kdt_algorithm(data, k, distance_function):
    """
    Funcion que implementa el algoritmo K-DT.
    :param data: lista de puntos de datos
    :param k: entero que indica el numero de clusters
    :param distance_function: funcion que calcula la distancia entre dos puntos
    :return: lista de clusters
    """
    clusters = []
    centroids = data[random.sample(range(0, len(data)), k)]
    old_centroids = centroids

    while old_centroids != centroids:
        old_centroids = centroids
        clusters = []

        for centroid in centroids:
            cluster = []

            for point in data:
                if distance_function(point, centroid) < distance_function(point, old_centroids[old_centroids.index(centroid)]):
                    cluster.append(point)

            clusters.append(cluster)

        centroids = []

        for cluster in clusters:
            centroids.append(np.mean(cluster, axis=0))

    return clusters

def distance_function(point1, point2):
    """
    Funcion que calcula la distancia euclidiana entre dos puntos.
    :param point1: punto 1
    :param point2: punto 2
    :return: distancia entre point1 y point2
    """
    return np.sqrt(np.sum((point1 - point2) ** 2))

def main():
    # Puntos de datos
    data = [[1, 1], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4]]

    # Visualizacion de los puntos de datos
    plt.scatter(data[:, 0], data[:, 1])
    plt.title('Puntos de datos')
    plt.show()

    # Aplicar el algoritmo