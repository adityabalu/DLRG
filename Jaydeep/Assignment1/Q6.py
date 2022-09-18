def readdat(filename):
    nodeList = []
    elementList = []
    #NumNodesPerElem = 0
    with open(filename,'r') as f:
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
                    nodeList.append(point)
                    continue
                try:
                    if int(line.strip().split(',')[0]) == -1:
                            nstart = False
                except ValueError as e:
                    pass
            if nstart == False and estart == True:
                if len(line.strip().split()) == 19 and linebreak == False:
                    assert int(line.strip().split()[10]) == len(elementList) + 1
                    NumNodesPerElem = int(line.strip().split()[8])
                    Elem = []
                    for nodeId in (line.strip().split()[11:]):
                        Elem.append(int(nodeId) - 1)
                    linebreak = True
                    continue
                if len(line.strip().split()) == NumNodesPerElem - 8 and linebreak == True:
                    for nodeId in (line.strip().split()):
                        Elem.append(int(nodeId) - 1)
                    elementList.append(Elem)
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
    return nodeList, elementList

if __name__ == '__main__':
    file = 'mesh.dat'
    nodes, elements = readdat(file)
    print(len(nodes), len(elements))