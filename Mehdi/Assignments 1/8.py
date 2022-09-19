from functools import wraps
import random
import time


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


randomlist_1 = []
randomlist_2 = []
for i in range(0,1000):
    #n = random.randint(1,30)
    n = random.random()
    m = random.random()
    randomlist_1.append(n)
    randomlist_2.append(m)

out = []

print('######################################## (a) ############################################')

#i:
@timeit
def product_calc_i(a, b):
    combined = list(zip(a, b))
    for s,r in combined:   
            out.append(s*r)
    return out
product_calc_i(randomlist_1, randomlist_2)

#ii:
@timeit
def product_calc_ii(a, b):
    for i in range (1000):   
            out.append(a[i]*b[i])
    return out
product_calc_ii(randomlist_1, randomlist_2)



#iii:
@timeit
def product_calc_iii(a, b):
    out = [a[x]*b[x] for x in range (1000)]
    return out
product_calc_iii(randomlist_1, randomlist_2)

print('\n######################################## (b) ############################################')
print ('This section has been done in Q6')
print ('We can accelerate the code by omitting unnecessary "for" loops.')

print('\n######################################## (c) ############################################')
@timeit
def norm_distr(): #Generate normal distribution
    result=[]
    for i in range (10000):
        count = 10
        values =  sum([random.randint(1, 100) for x in range(count)])
        result.append(round(values/count))
    return result
list = norm_distr()
print('\n######################################## (d) ############################################')
@timeit
def norm_distr(): #Generate normal distribution
    result=()
    for i in range (10000):
        count = 10
        values =  sum([random.randint(1, 100) for x in range(count)])
        result = result + (round(values/count),)
    return result
tuple = norm_distr()
print('\n######################################## (e) ############################################')
@timeit
def find_median(m): # because the index starts from 0 --> [med - 1]
    length = len(m)
    n = sorted(m)
    if (length % 2 == 0):
        median = (n[int(length/2) - 1] + n[int(length/2 + 1) - 1])/2
    else:
        median = n[int((length + 1)/2) - 1]
    return median

find_median(list)
find_median(tuple)

print('\n######################################## (f) ############################################')
print('I prefer to use the "list" structure because it can be extended by the "append" command.')


print('\n######################################## (g) ############################################')

my_dict = {"gauss":[],"lognormvariate":[],"normalvariate":[]};
@timeit
def dic_creator():
    for i in range (1000):
        my_dict["gauss"].append(random.gauss(100, 50))  
        my_dict["lognormvariate"].append(random.lognormvariate(0, 0.25))
        my_dict["normalvariate"].append(random.randint(1, 100))

dic_creator()

print('\n######################################## (h) ############################################')
@timeit
def l2_norm(list):
    max = len(list)
    norm = 0
    sum1 = sum([list[i] for i in range(max)])
    mean = sum1 / max
    for i in range (0, max):
        norm = norm + ((list[i] - mean)**2)
    return norm**1/2

print('KL-Divergence of gauss: ', l2_norm(my_dict["gauss"]), '\n')
print('KL-Divergence of lognormvariate: ', l2_norm(my_dict["lognormvariate"]), '\n')
print('KL-Divergence of normalvariate: ', l2_norm(my_dict["normalvariate"]), '\n')