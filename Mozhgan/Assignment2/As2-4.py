import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

dist_cities = []
city_locs = np.array([[0, 0], [10, 15], [25, 10], [40, 50], [12, 5], [25, 25], [50, 50], [6, 50], [10, 18], [12, 18]])
for i in range(len(city_locs)):
    # city_code = f"{i}"
    dist = []
    for j in range(len(city_locs)):
        dist.append(np.linalg.norm(city_locs[i] - city_locs[j]))
    dist_cities.append(dist)
y=np.array([np.array(dist_cities) for xi in dist_cities])
# np.shape(y)
arr_city_dists = y[0, :]
print(arr_city_dists)

ax = plt.subplot()
im = ax.imshow(arr_city_dists)

# create an Axes on the right side of ax. The width of cax will be 5%
# of ax and the padding between cax and ax will be fixed at 0.05 inch.
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)

plt.colorbar(im, cax=cax)

plt.show()

