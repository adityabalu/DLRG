from functools import wraps
import time
import random

#timeit_wrapper function
def timeit(meth):
    @wraps(meth)
    def timeit_wrapper(*args, **kwargs):
        start = time.time()
        result = meth(*args, **kwargs)
        # print(result)  #display results 
        end = time.time()
        total_time = end - start
        print(f'{meth.__name__} method executes in {(total_time*1000):.8f} ms\n')
    return timeit_wrapper

class Calculator:

    @timeit
    def get_time_zip(self, list1, list2):
        
        for x,y in zip (list1, list2):
            result_zip.append(x*y)
        return result_zip
    @timeit
    def get_time_for(self, list1, list2):

        for i in range (len(list1)):
            result_for.append(list1[i]*list2[i])
        return result_for
    @timeit
    def get_time_list(self, list1, list2):
        
        result_list = [list1[i]*list2[i] for i in range(len(list1))]
        return result_list


#inputs
list1 = random.sample(range(1, 1100), 1000) # n=1000 numbers in [1,1100]
list2 = random.sample(range(1, 1100), 1000)

if __name__ == '__main__':
    result_zip=[]
    result_for=[]
    calc = Calculator()
    calc.get_time_zip(list1, list2)
    calc.get_time_for(list1, list2)
    calc.get_time_list(list1, list2)

# sample output:
# get_time_zip method executes in 0.12803078 ms

# get_time_for method executes in 0.14305115 ms

# get_time_list method executes in 0.11086464 ms