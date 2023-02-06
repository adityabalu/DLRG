"""
A tetrahedral mesh can be represented as a graph with a set of nodes and a 
set  of  element  connectivity  (edge  connectivity  of  the  graph).  This is  a  python class 
which can store all the information of a mesh (i.e. the nodal locations, the edge 
connectivity). Also, it includes a method to read a mesh file in .dat format.
"""

class TetrahedralMesh:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
    

    def read_mesh_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            start = 0
            # find the line that starts with "/wb,node,start"
            for i, line in enumerate(lines):
                if line.startswith("/wb,node,start"):
                    start = i + 3
                    break
            # idx= int(lines[start].split('  ')[4])
            # parse the nodes
            self.nodes = []
            for i in range(start, len(lines)):
                if lines[i].startswith("-1"):
                    break
                else:
                    node = tuple(map(float, lines[i].split()))
                    self.nodes.append(node)
            
            start= start+ len(self.nodes)+6
            # parse the edges
            self.edges = []
            for i in range(start, len(lines)):
                if lines[i].startswith("-1"):
                    break
                else:
                    edge = tuple(map(int, lines[i].split()))
                    self.edges.append(edge)
        return self.nodes, self.edges

    

if __name__ == '__main__':
    mesh = TetrahedralMesh([], [])
    [nodes, edges] = mesh.read_mesh_file('mesh.dat')

    print(edges)
    # print(type(nodes))
    # print(len(nodes))