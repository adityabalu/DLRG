import numpy as np


x, y = np.mgrid[:10, :5]
z = x + y
print("Dimentions of x, y, z : ", np.ndim(x), np.ndim(y), np.ndim(z))
print("Shape of x, y, z : ", np.shape(x), np.shape(y), np.shape(z))

x1, y1 = np.ogrid[:10, :5]
z1 = x1 + y1
print("Dimentions of x1, y1, z1 : ", np.ndim(x1), np.ndim(y1), np.ndim(z1))
print("Shape of x1, y1, z1 : ", np.shape(x1), np.shape(y1), np.shape(z1))

