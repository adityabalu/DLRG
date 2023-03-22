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
def time_taken_i(n):
    list1 = [i for i in range(n)]
    list2 = [i for i in range(n)]
    re_list = [list(zip(list1, list2))[i][0] * list(zip(list1, list2))[i][1] for i in range(len(list1))]
    print(re_list)


@timeit
def time_taken_ii(n):
    l1 = [i for i in range(n)]
    l2 = [i for i in range(n)]
    res_list = []
    for i in range(0, len(l1)):
        res_list.append(l1[i] * l2[i])
    print(res_list)


@timeit
def time_taken_iii(n):
    li1 = [i for i in range(n)]
    li2 = [i for i in range(n)]
    result_list = [li1[i] * li2[i] for i in range(len(li1))]
    print(result_list)


time_taken_i(1000)
time_taken_ii(1000)
time_taken_iii(1000)
