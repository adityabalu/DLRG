# class exe_time:

#     def extime(self, method):
#         self.method= method
#get time to run q4 

from functools import wraps
import time
from q4 import chapter_num 
obj =chapter_num()
method= obj.chp_num

#timeit_wrapper function
def timeit(meth):
    @wraps(meth)
    def timeit_wrapper(*args, **kwargs):
        start = time.time()
        result = meth(*args, **kwargs)
        print(result)  #display results 
        end = time.time()
        total_time = end - start
        print(f'\n method executes in {total_time:.8f} seconds')
    return timeit_wrapper

class Calculator:
    @timeit
    def get_time(self, num):

        result= method(num)
        return result


if __name__ == '__main__':
    calc = Calculator()
    calc.get_time(5)

# sample output:

# ['Chapter 1', 'Chapter 2', 'Chapter 3', 'Chapter 4', 'Chapter 5', 'Chapter 6']

#  method executes in 0.00005817 seconds
