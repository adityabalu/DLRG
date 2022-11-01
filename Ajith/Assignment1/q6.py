from q7 import timeit

@timeit
def readMesh(filename):
    """
    returns two seperate lists containing nodes and elements
    """
    with open(filename) as f:
        lines = f.readlines()

    nodes = numNodes(lines)

    node_list = lines[5:(nodes+5)]
    ele_list = lines[(nodes+12):-3]

    return numArray(node_list), numArray(ele_list)

def numNodes(lines):

    return int(lines[2].split(',')[3])

def numArray(num_list):

    return [[float(ele) for ele in line.split()] for line in num_list]


print(readMesh('mesh.dat'))