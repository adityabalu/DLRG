# Just part c (X + Y[: , np.newaxis]) produce an error!

import numpy as np

X = np.random.rand(10, 3)
Y = np.random.rand(3)
print(X[np.newaxis, :].shape)
print(Y[:, np.newaxis].shape)
"""
print(X + Y)
print(X[np.newaxis, :] + Y)
print(X + Y[:, np.newaxis])
print(X[:, np.newaxis] + Y)
print(X + Y[np.newaxis, :])
print(X[:, np.newaxis, :] + Y)
"""
