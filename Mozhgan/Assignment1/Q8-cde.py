from time import time
import numpy as np
import statistics


def timeit(func):
    def inside_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.5f} seconds')
        return result

    return inside_func


@timeit
def time_taken_list(n):
    rand_nums = np.random.uniform(size=n)
    mid_nums = statistics.median(rand_nums)
#    print(rand_nums)
    print(mid_nums)


@timeit
def time_taken_tuple(n):
    rand_nums = np.random.uniform(size=n)
    median_num = statistics.median(tuple(rand_nums))
#    print(tuple(rand_nums))
    print(median_num)


time_taken_list(10000)
time_taken_tuple(10000)

time_taken_list(40000)
time_taken_tuple(40000)
