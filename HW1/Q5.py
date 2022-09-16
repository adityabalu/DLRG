class mesh:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNode(self,i,j):
        n = [i,j]
        self.nodes.append(n);
    
    def findNode(self,i,j):
        for c,n in enumerate(self.nodes):
            if n[0] == i and n[1] == j:
                return c;

    def addEdges(self,i1,j1,i2,j2):
        n1 = self.findNode(i1,j1);
        n2 = self.findNode(i2,j2);
        self.edges.append([n1,n2])

    
    def printMesh(self):
        for e in self.edges:
            print(self.nodes[e[0]],"---",self.nodes[e[1]])
    

if __name__ == '__main__':
    m = mesh();
    m.addNode(1,2)
#    print(m.nodes)
    m.addNode(3,4)
 #   print(m.nodes)
    m.addEdges(1,2,3,4)

    m.printMesh()