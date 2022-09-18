import numpy as np;
from numpy import random;
from statistics import median
from scipy.special import rel_entr
def timingMethods():
    def product1(a,b):
        p = [];
        for i, j in zip(a,b):
            p.append(i*j);
        return p;


    def product2(a,b):
        p = [i*j for i,j in zip(a,b)]
        return p;


    def product3(a,b):
        p = []
        for i in range(1000):
            p[i] = a[i]*b[i];
        return p;

    import time;
    def timeit(func):
        def subFunc(*args, **kwargs):
            begin = time.time()
            func(*args, **kwargs)
            end = time.time()
            print(end - begin)
        return subFunc
 
 

    @timeit
    def readMesh():
        with open(r'C:\Users\mozhd\Downloads\mesh.dat') as f:
            mesh = [line.split() for line in f] 
    readMesh();
    
    
    l1 =  random.uniform(0,1,1000)
    l2 = random.uniform(0,1,1000)
    l2 = tuple(l2)
 
    
    @timeit
    def med(l):
        print(median(l))
   
    med(l1)
    med(l2)
    
    dict = {'gauss':[], 'lognormvariate':[], 'normalvariate':[]}
    for i in range(1000):
        dict['gauss'].append(random.normal(0,1));
#        dict['normalvariate'].append(random.normalvariate(0,1)) 
#        dict['lognormvariate'].append(random.lognormvariate(0,1))
#    print(dict)
    # the answer for question f:
    # If you want to increase your sample size by n elements which data structure, can you easily add on to and why?
    # The answer will be list. Since size of the tuple is fixed, and we cannot add change the size of the tuple. 
    

    kl = np.zeros((3,3))
#    for key1 in dict.keys():
#        for key2 in dict.keys():
#            kl = sum(rel_entr(dict[key1], dict[key2]))
 #   print(kl)


if __name__ == '__main__':
    timingMethods()
