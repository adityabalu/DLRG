import numpy as np
from numpy import savetxt


class Tetra:

    def save_tets(self, nodes):
        self.save = savetxt('data.csv', nodes, delimiter=',')
        return self.save


node = np.array([
    [0, 1, 2, 6],
    [0, 5, 1, 6],
    [0, 4, 5, 6],
    [0, 7, 4, 6],
    [0, 3, 7, 6],
    [0, 2, 3, 6]], dtype=np.int)

TETRA = Tetra()  # object of Tetra class
print(TETRA.save_tets(node))
