from functools import wraps
import time

print('\n######################################## Runtime ############################################')

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def line_numbers(file_path, word_list): # searching in file

    with open(file_path, 'r') as f:
        results = {word:[] for word in word_list}
        for num, line in enumerate(f, start=1):
            for word in word_list:
                if word in line:
                    results[word].append(num)
                    temp = num
    return temp

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
    

with open('mesh.dat', 'r') as d: # open mesh file
    content = d.readlines()


# counting nodes
node_counter = content[2].split(",")
nodes = int(node_counter[3])

# counting element
start = ['Element Group 1']
end = ['Done writing mesh elements']
element_start_line = line_numbers("mesh.dat", start) + 2 
element_end_line = line_numbers("mesh.dat", end) - 3
elements = int((element_end_line - element_start_line + 1) / 2) # all elements


# creating mesh matrix
m = Mesh((nodes + 1), 3, (elements + 1), 8)

# writing node coordinates
@timeit
def read_nodes():
    for x in range(1, nodes):
        line = content[x + 3].split()
        m.assign_node((x), 0, line[1])
        m.assign_node((x), 1, line[2])
        m.assign_node((x), 2, line[3])

read_nodes()


# writing elements information
@timeit
def read_element():
    for i in range(0, elements):
        c = 2*i + element_start_line
        line = content[c].split()
        for j in range (0, 8):
            m.assign_conn(i + 1, j, line[j + 11])
read_element()

print('\nTest:')
print('\nNode 33201:', m.nodal[33201][:])
print('Element 5712:', m.conn[5712][:])

