#  Copyright (c) 2021. Oskar "Bocian" Możdżeń
#  All rights reserved.

import numpy as np
import matplotlib.pyplot as plt
from Perceptron import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs

def accuracy(y_true, y_pred):
    acc = np.sum(y_true == y_pred) / len(y_true)
    return acc

X, y = make_blobs(n_samples=150, n_features=2, centers=2, cluster_std=1.05, random_state=424)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=481)

p = Perceptron()
p.fit(X_train, y_train)
predictions = p.predict(X_test)

print("Perceptron classification accuracy", accuracy(y_test, predictions))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.scatter(X_train[:, 0], X_train[:, 1], marker='o', c=y_train)

x0_1 = np.amin(X_train[:, 0])
x0_2 = np.amax(X_train[:, 0])

x1_1 = (-p.weights[0] * x0_1 - p.bias) / p.weights[1]
x1_2 = (-p.weights[0] * x0_2 - p.bias) / p.weights[1]

ax.plot([x0_1, x0_2], [x1_1, x1_2], 'k')

ymin = np.amin(X_train[:, 1])
ymax = np.amax(X_train[:, 1])
ax.set_ylim([ymin - 3, ymax + 3])

plt.show()
