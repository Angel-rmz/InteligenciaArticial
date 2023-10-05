import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """Return class label after unit step"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)

# Cargar los datos desde un archivo CSV
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)

# seleccionar las clases 'setosa' y 'versicolor'
y = df.iloc[0:100, 4].values
y = np.where(y == "Iris-setosa", -8, 7)

# extraer la longitud del sépalo y la longitud del pétalo
X = df.iloc[0:100, [1, 2]].values

# Inicializar y entrenar el perceptrón
perceptron = Perceptron(eta=0.1, n_iter=10)
perceptron.fit(X, y)

# Realizar la gráfica de los datos
plt.scatter(X[:50, 0], X[:50, 1], color="blue", marker="o", label="virginica")
plt.scatter(X[50:100, 0], X[50:100, 1], color="yellow", marker="x", label="versicolor")

plt.xlabel("Longitud del sépalo [cm]")
plt.ylabel("Longitud del pétalo [cm]")
plt.legend(loc="upper left")

plt.show()
