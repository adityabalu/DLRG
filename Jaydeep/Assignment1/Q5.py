class tetMesh():
	def __init__(self, nodeList=None, elemList=None):
		self.nodeList = nodeList # Each element in this list is a list of 3 containing x,y,z co-ordinates
		self.elemList = elemList # Each element in this list is a list of the node indexes from nodeList forming the element

	def __str__(self):
		return 'There are {} nodes and {} elements'.format(len(self.nodeList), len(self.elemList))

if __name__ == '__main__':
	tetMesh1 = tetMesh()
	