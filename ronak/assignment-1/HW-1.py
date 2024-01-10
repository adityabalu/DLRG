
######################

# Run using VSCODE #

######################

#%%

#################
# Helper Function
#################

import warnings
warnings.filterwarnings("ignore")

from heapq import *
class MedianFinder(object):

    def __init__(self):
        self.heaps = [], []
        
    def addNum(self, num):
        left, right = self.heaps # min heap
        heappush(left, -heappushpop(right, num))
        if len(right) < len(left):
            heappush(right, -heappop(left))

    def findMedian(self):
        left, right = self.heaps
        if len(right) > len(left):
            return float(right[0])
        return (right[0] - left[0])/2.0  


#%%

######
# Q.1.
######
from dis import dis
import math
import itertools

rot_180 = { 
            0:0,
            1:1,
            6:9,
            8:8,
            9:6
          }

pos_first = [1,6,8,9]
pos_rest = [0,1,6,8,9]

def fill_rest(half_number):
    digits = len(half_number)
    other_half = []
    for l in range(digits-1,-1,-1):
        other_half.append(rot_180[half_number[l]])
    return other_half

def break_list(in_list):
    s = [str(i) for i in in_list]
    res = int("".join(s))
    return(res)

def list_to_num(in_list):
    list_of_nums = [break_list(elem) for elem in in_list]
    return list_of_nums


def gen_strobo(seq_length: int):
    if seq_length < 3:
        raise ValueError("Provide a parameter value >= 3")
    try:
        #If desired sequence lenth is even
        if seq_length%2 == 0:
            
            #We first manipulate the first half of a n digit number i.e. n/2
            to_gen = int(seq_length/2)

            #Generate list of lists so that we can apply itertools product
            LoL = [pos_first if t == 0 else pos_rest for t in range(to_gen)]

            #Key Step - We use iterlist to generate all possible combination of digits in the first half of the n digit number
            full_half_list = itertools.product(*LoL)

            #Convert these half numbers into digits
            in_list = [list(in_elem) for in_elem in full_half_list]

            #Use another method to convert first half to the second half of the number by rotating the digits by 180 degrees.
            received_list = [fill_rest(list(elem)) for elem in in_list]

            #We merge both the first half and the second half
            out_list = [in_list[j]+received_list[j] for j in range(len(in_list))]

            return list_to_num(out_list)

        else:
            to_gen = int((seq_length-1)/2)

            #Generate list of lists so that we can apply itertools product
            LoL = [pos_first if t == 0 else pos_rest for t in range(to_gen)]

            full_half_list = itertools.product(*LoL)
            in_list = [list(in_elem) for in_elem in full_half_list]
            received_list = [fill_rest(list(elem)) for elem in in_list]

            out_list = []
            for j in range(len(in_list)):
                #We need to append the middle digits for all combinations generated above.
                out_list.append(in_list[j]+[0]+received_list[j])
                out_list.append(in_list[j]+[1]+received_list[j])
                out_list.append(in_list[j]+[8]+received_list[j])

            return list_to_num(out_list)

    except Exception as e:
        print(str(e.with_traceback))
    


#Test the Method
got_list = gen_strobo(seq_length=4)
print("===========List of Strobogrammatic Numbers are ===============")
print(got_list)
print("==============================================================")





#%%
######
# Q.2.
######

def concat(strg_1: list, strg_2: list):

    #Zip together
    one_list = zip(strg_1,strg_2)

    #Apply the logic
    curated_list = [elem[0].lower() + ' ' + elem[1].lower() for elem in one_list]

    return curated_list

#Test the Method     
concat(['OnE','TWo'],['THree','FouR'])




#%%
######
# Q.3.
######

def convert_to_num(strg_1: list, strg_2: list):

    one_list = zip(strg_1,strg_2) #Size reduction by Zipping

    #Conversion to integer and multiplication
    audited_list = [int(elem[0])*int(elem[1]) for elem in one_list if (str(elem[0]).isnumeric() & str(elem[1]).isnumeric())]
    
    return audited_list

#Test the Method     
convert_to_num(['12', '13', 'Hello', '4', '6', '10]'],['2', '3', '4', 5, '[6', 12, 14])



# %%
######
# Q.4.
######

def list_chaps(num_chapters: int):
    return ['Chapter ' + str(elem) for elem in range(1,num_chapters+2)]

#Test the method
list_chaps(num_chapters=5)






#%%
######
# Q.5.
######
import numpy as np
class Mesh():

    def __init__(self, vertices: np.array, coords: np.array, adjacency_matrix: np.array) -> None:
        self.vertices = vertices
        self.coords = coords
        self.adjacency_matrix = adjacency_matrix

    def print_mesh_nodes(self):
        for node in range(len(self.vertices)):
            print('Node# {} is at Coords {}'.format(self.vertices[node], self.coords[node]))
    
    def print_edges(self):
        print('The following 1/0 matrix shows the edges in the mesh')
        print(self.adjacency_matrix)

    def add_nodes_and_edges(self, vertex: int, coord: np.array, edge_list: np.array):
        try:
            self.vertices = self.vertices.append(vertex) # Add Vertex
            self.coords = self.coords.append(coord) #Add the Coordinates

            #Prepare to add an additional row and column of connections to the adjacency matrix
            curr_size = len(self.vertices)
            updated_matrix = np.c_[self.adjacency_matrix, np.zeros(curr_size)]
            updated_matrix = np.vstack((updated_matrix, np.zeros(curr_size+1)))
            
            #Load connections from New Edge List
            for i in range(curr_size):
                updated_matrix[i, curr_size] = edge_list[i]
                updated_matrix[curr_size, i] = edge_list[i]
            
            #Every new edge is connected to itself
            updated_matrix[curr_size,curr_size] = 1

            #Save this new matrix back in the Mesh
            self.adjacency_matrix = updated_matrix

        except Exception as e: 
            print(str(e.with_traceback))



#%%
######
# Q.6.
######

'''

Objective is to create two files
(i) Mesh Nodes - Lines 5 to 54877
(ii) Mesh Elements - Lines 54884 - 128625

'''


def read_fem(fname):

  with open(fname) as file:
    lines = file.readlines()

  ####################
  # File Specific Info
  ####################        
  node_start = 4
  node_end = 4+54873
  mesh_start = 4+54873+6
  mesh_end = len(lines) - 3

  #Collect Nodes
  mesh_nodes_LoL = []
  for idx in range(node_start,node_end):
    each_line_node = [lines[idx].split()]
    mesh_nodes_LoL.append(each_line_node)

  #Collect Mesh Elements
  mesh_connectivity_LoL = []
  for idx in range(mesh_start,len(lines)-2,2):
    each_line_mesh = [lines[idx].split()[10:19]]
    mesh_connectivity_LoL.append(each_line_mesh)

  print('============= AUDIT REPORT ==================\n')
  print('Number of Mesh Nodes {} \n'.format(len(mesh_nodes_LoL)))
  print('Number of Mesh Elements {} \n'.format(len(mesh_connectivity_LoL)))
  print('============= AUDIT REPORT ENDS =============\n')

  return mesh_nodes_LoL, mesh_connectivity_LoL

        
collected_nodes, collected_mesh = read_fem('/home/ronak/Downloads/DL- Reading-Group/dlrg/mesh.dat')



#%%
######
# Q.7.
######
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('Execution time: {} seconds'.format(end_time - start_time))
        return result
    return wrapper


@timeit
def test_func(): #To add the first 100 million positive integers
    sum_x = 0
    for i in range(100000000):
        sum_x += i


#Test the Code
test_func()



#%%
######
# Q.8.
######

from scipy.special import rel_entr
import random

#a

list_1 = [random.randint(1,10000) for j in range(1000)]
list_2 = [random.randint(1,10000) for j in range(1000)]


#(i)

@timeit
def prod_list1(L1: list, L2: list):
  one_list = zip(L1,L2)
  final_result = []
  for elem in one_list:
    final_result.append(elem[0]*elem[1])
  return final_result

prod_list1(list_1,list_2)



#(ii)

@timeit
def prod_list2(L1: list, L2: list):
  list_len = len(L1)
  final_result = []
  for h in range(list_len):
    final_result.append(L1[h]*L2[h])
  return final_result


prod_list2(list_1,list_2)



#(iii)

@timeit
def prod_list3(L1: list, L2: list):
  list_len = len(L1)
  return [L1[h]*L2[h] for h in range(list_len)]

prod_list3(list_1,list_2)


#8b
#%%
@timeit
def read_fem(fname):

  with open(fname) as file:
    lines = file.readlines()

  ####################
  # File Specific Info
  ####################        
  node_start = 4
  node_end = 4+54873
  mesh_start = 4+54873+6
  mesh_end = len(lines) - 3

  #Collect Nodes
  mesh_nodes_LoL = []
  for idx in range(node_start,node_end):
    each_line_node = [lines[idx].split()]
    mesh_nodes_LoL.append(each_line_node)

  #Collect Mesh Elements
  mesh_connectivity_LoL = []
  for idx in range(mesh_start,len(lines)-2,2):
    each_line_mesh = [lines[idx].split()[10:19]]
    mesh_connectivity_LoL.append(each_line_mesh)

  print('============= AUDIT REPORT ==================\n')
  print('Number of Mesh Nodes {} \n'.format(len(mesh_nodes_LoL)))
  print('Number of Mesh Elements {} \n'.format(len(mesh_connectivity_LoL)))
  print('============= AUDIT REPORT ENDS =============\n')

  return mesh_nodes_LoL, mesh_connectivity_LoL

        
collected_nodes, collected_mesh = read_fem('/home/ronak/Downloads/DL- Reading-Group/dlrg/mesh.dat')

#%%

#8c
@timeit
def samp_randuni(samp_length = 10000):
  return [np.random.uniform(-1,1) for t in range(samp_length)]
  
ds1 = samp_randuni(10000)

#%%
 
#8d
@timeit
def samp_randuni2(samp_length = 10000):
  return tuple(np.random.uniform(-1,1) for t in range(samp_length))

ds2 = samp_randuni2()

#%%

#8e

@timeit
def medianFinder(dset):
    obj = MedianFinder()
    for t in range(len(dset)):
        obj.addNum(dset[t])
    #Return Medians from
    return obj.findMedian()

print(medianFinder(ds1))
print(medianFinder(ds2))

#%%

#8f
'''
Both lists and dictionaries are good candidates, but adding to a list is easier as we don't need to create keys.
But Dictionaries have better lookup speed while retrieving data. Hence, if we need frequent lookups, dictionary might be a better choice.
'''

#%%
#8g

@timeit
def gen_samples(stype: str):
    if stype == 'gauss':
        return np.array([random.gauss(0,1) for r in range(1000)])
    elif stype == 'lognorm':
        return np.array([random.lognormvariate(0,1) for r in range(1000)])
    else:
        return np.array([random.normalvariate(0,1) for r in range(1000)])

dists = {
        'gauss': gen_samples('gauss'),
        'lognormalvariate' : gen_samples('lognorm'),
        'normalvariate' : gen_samples('normvar')
}

#%%

#8h

import matplotlib.pyplot as plt
from scipy.stats import norm
import sklearn.metrics

@timeit
def kl_divergence(p, q):
  return sklearn.metrics.mutual_info_score(p,q)

print(kl_divergence(dists['gauss'],dists['lognormalvariate']))
print(kl_divergence(dists['gauss'],dists['normalvariate']))
print(kl_divergence(dists['lognormalvariate'],dists['normalvariate']))


#%%
#################
# Q.9,10,11,12
#################

#Q9/10/11/12

class Robot:
  def __init__(self) -> None:
    self.position = np.array([[0],[0]]) #Column Vector
    self.direction = np.array([[1],[0]]) #Column Vector
    self.time = 0.0
    self.speed = 0.5

  def __repr__(self):
        return f'Robot(position = {self.position}, direction = {self.direction}, time = {self.time}, speed = {self.speed})'

  def wait(self,time):
    self.time = self.time + time

  def move_forward(self,time):
    self.position = self.position + self.direction * self.speed * time
    self.time = self.time + time

  def rotate_right(self):
    rot_matrix_right = np.array([[0,1],[-1,0]])
    self.direction = rot_matrix_right@self.direction

  def rotate_left(self):
    rot_matrix_left = np.array([[0,-1],[1,0]])
    self.direction = rot_matrix_left@self.direction

  def move_square(self,side_length):
    for k in range(4):
      self.move_forward(side_length)
      print('Robot state is as follows: \n')
      print(self.__repr__())
      self.rotate_left()
      print('\n Robot now being rotated to the left by 90 degrees. \n')

    print('===========Final State of the Robot is as follows: ================ \n')
    print(self.__repr__())
    print('\n ===================================================================')

#Instantiate the Robot
myRobot = Robot()
# Executing the motion of the Robot along a square trajectory
myRobot.move_square(20)


