from time import time
import random
from scipy.special import rel_entr


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
    dict_my = {}
    key_list = ["gauss", "lognormvariate", "normalvariate"]
    nums_g = []
    nums_l = []
    nums_n = []
    mu = 100
    sigma = 50
    for i in range(n):
        temp_g = random.gauss(mu, sigma)
        nums_g.append(temp_g)
        temp_l = random.lognormvariate(mu, sigma)
        nums_l.append(temp_l)
        temp_n = random.normalvariate(mu, sigma)
        nums_n.append(temp_n)
    dict_my["gauss"] = nums_g
    dict_my["lognormvariate"] = nums_l
    dict_my["normalvariate"] = nums_n
    print(dict_my)
    print(sum(rel_entr(nums_g, nums_l)))
    print(sum(rel_entr(nums_g, nums_n)))
    print(sum(rel_entr(nums_l, nums_n)))


time_taken(1000)
