import time
import random
import statistics

from Q6 import readdat

def timeit(func):
    def calculateTime(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start_time
        print('Total execution time = {:0.5f}'.format(total_time))
        return result
    return calculateTime

@timeit
def _8a1(list1, list2):
	products = []
	for l1, l2 in zip(list1, list2):
		products.append(l1*l2)
	return products

@timeit
def _8a2(list1, list2):
	products = []
	for i in range(len(list1)):
		products.append(list1[i]*list2[i])
	return products

@timeit
def _8a3(list1, list2):
	products = [l1*l2 for l1, l2 in zip(list1, list2)]
	return products

@timeit
def _8c(n=10000):
	numbers = [random.uniform(0,1) for _ in range(n)]
	return numbers

@timeit
def _8d(n=10000):
	numbers = tuple(random.uniform(0,1) for _ in range(n))
	return numbers


@timeit
def _8e(data):
	n = len(data)
	data = sorted(data)
	if n%2 != 0:
		return data[n//2 - 1]
	else:
		return (data[n//2 - 1] + data[n//2]) / 2
	
@timeit
def  _8g(n=1000):
	random_numbers = {}
	keys = ['gauss', 'lognormvariate', 'normalvariate']
	random_numbers['gauss'] , random_numbers['lognormvariate'], random_numbers['normalvariate'] = [],[],[]  
	for i in range(n):
		random_numbers['gauss'].append(random.gauss(0,1))
		random_numbers['lognormvariate'].append(random.lognormvariate(0,1))
		random_numbers['normalvariate'].append(random.normalvariate(0,1))
	return random_numbers		

@timeit
def _8h(mean1, mean2):
	return (mean1 - mean2)**2

if __name__ == '__main__':
	# Q8a
	list1 = [i for i in range(1000)]
	list2 = [i for i in range(1000)]
	_8a1(list1, list2)
	_8a2(list1, list2)
	_8a3(list1, list2)
	
	#Q8b
	readdat = timeit(readdat)
	readdat('mesh.dat')
	
	#Q8c
	random_list = _8c(10000)
	#Q8d
	random_tuple = _8d(10000)
	
	#Q8e
	print('Median of List: ', _8e(random_list))
	print('Median of tuple: ', _8e(random_tuple))

	#Q8f

	# To increase the sample size by n elements, the easiest way is to add to the list. As list creation already allocates more memory as they are mutable

	#Q8g
	random_numbers = _8g(1000)
	
	#Q8h
	gauss_mean = statistics.mean(random_numbers['gauss'])
	lognormvariate_mean = statistics.mean(random_numbers['lognormvariate'])  
	normalvariate_mean = statistics.mean(random_numbers['normalvariate']) 
	print(gauss_mean)
	print(lognormvariate_mean)
	print(normalvariate_mean)
	
	print('KL diverhence between gauss and lognormvariate = ', _8h(gauss_mean, lognormvariate_mean))
	print('KL diverhence between gauss and normalvariate = ', _8h(gauss_mean, normalvariate_mean))
	print('KL diverhence between lognormvariate and normalvariate = ', _8h(lognormvariate_mean, normalvariate_mean))
	
	