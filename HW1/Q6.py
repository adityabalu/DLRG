import numpy as np;
if __name__ == '__main__':
    with open(r'C:\Users\mozhd\Downloads\mesh.dat') as f:
        mesh = [line.split() for line in f] 
    print(len(mesh))
    print(mesh[4])