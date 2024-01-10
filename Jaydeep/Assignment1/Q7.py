import time

def timeit(func):
    def calculateTime(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start_time
        print('Total execution time = {:0.4f}'.format(total_time))
        return result
    return calculateTime

@timeit
def testFunction():
    pass

if __name__ == '__main__':
	testFunction()