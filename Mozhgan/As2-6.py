import numpy as np

X = np.array([5, 9, 77, 0, 74, 55, 81, 79, 90])
Y = np.array([5, 1, 46, 2, 10, 29, 55, 4, 90])

a = np.where(X > Y)
print(a)
print(X[a], a)

b = np.where(X == Y)
print(b)
print(X[b], b)
