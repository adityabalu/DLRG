class Mesh: # creating mesh matrix
    def __init__(self, n, d, e, t): #(number of nodes, dimension, number of elements, element group capacity)
        self.nodal = [[0] * d for _ in range(n)]
        self.conn = [[0] * t for _ in range(e)]

    def assign_node(self, n, a, value): # assign node coordinates
        self.nodal[n][a] = value

    def assign_conn(self, e, a, value): # assign elenment number for connections
        self.conn[e][a] = value

    def retrieve_node(self, n, a): # reading node information
        return self.nodal[n][a]

    def retrieve_element(self, e, a): # reading element connectivity information
        return self.conn[e][a]

    
# Test Class   
    
m = Mesh(6, 3, 11, 4) # creating mesh matrix (ex: nodes=6 , three dimension, elements=11, connectivity=4)
print('\nTest Class:' + '\nCreating mesh matrix (ex: nodes=6 , three dimension, elements=11, connectivity=4)')
print('\nNodes matrix:')
print(m.nodal) # print node matrix
print('\nElements matrix:')
print(m.conn) # print element connectivity matrix

