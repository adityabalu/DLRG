class tetMesh():
	def __init__(self, filename='mesh.dat'):
		self.nodeList = None # Each element in this list is a list of 3 containing x,y,z co-ordinates
		self.elemList = None # Each element in this list is a list of the node indexes from nodeList forming the element
		self.filename = filename
	def __str__(self):
		return 'There are {} nodes and {} elements'.format(len(self.nodeList), len(self.elemList))

	def readdat(self, filename):
	    self.nodeList = []
	    self.elemList = []
	    #NumNodesPerElem = 0
	    with open(self.filename,'r') as f:
	        nstart = False
	        estart = False
	        linebreak = False
	        NumNodesPerElem = 0
	        for idx, line in enumerate(f):
	            if nstart == True and estart == False:
	                if len(line.strip().split()) == 4:
	                    assert int(line.strip().split()[0]) == (idx - n_start_idx + 1)
	                    point = []
	                    for coord in line.strip().split()[1:]:
	                        point.append(float(coord))
	                    self.nodeList.append(point)
	                    continue
	                try:
	                    if int(line.strip().split(',')[0]) == -1:
	                            nstart = False
	                except ValueError as e:
	                    pass
	            if nstart == False and estart == True:
	                if len(line.strip().split()) == 19 and linebreak == False:
	                    assert int(line.strip().split()[10]) == len(self.elemList) + 1
	                    NumNodesPerElem = int(line.strip().split()[8])
	                    Elem = []
	                    for nodeId in (line.strip().split()[11:]):
	                        Elem.append(int(nodeId) - 1)
	                    linebreak = True
	                    continue
	                if len(line.strip().split()) == NumNodesPerElem - 8 and linebreak == True:
	                    for nodeId in (line.strip().split()):
	                        Elem.append(int(nodeId) - 1)
	                    self.elemList.append(Elem)
	                    linebreak = False
	                    continue
	                try:
	                    if int(line.strip().split(',')[0]) == -1:
	                            estart = False
	                except ValueError as e:
	                    pass
	                pass # Need to write the parser for elements
	            if nstart == False and estart == False:
	                if line.startswith('nblock'):
	                    NumNodes = int(line.strip().split(',')[-1])
	                    n_start_idx = idx + 2
	                    nstart = True
	                if line.startswith('eblock'):
	                    e_start_idx = idx + 2
	                    estart = True
	    return self.nodeList, self.elemList

if __name__ == '__main__':
	filename = 'mesh.dat'
	tetMesh1 = tetMesh(filename)
	mesh = tetMesh1.readdat(filename)
	print(tetMesh1)
	