from time import time


def timeit(func):
    def inside_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.5f} seconds')
        return result

    return inside_func


@timeit
def time_taken(n):
    for i in range(n):
        for j in range(10000):
            i * j


time_taken(5)
time_taken(50)
time_taken(500)
time_taken(5000)
