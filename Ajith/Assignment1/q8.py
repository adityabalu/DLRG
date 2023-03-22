from q7 import timeit
import random



#######################################################################################
print("\n\na")

list1 = [1e5, 1e5, 1e5]
list2 = [1e5, 1e5, 1e5]


print("For loops with zip iterator")
@timeit
def zippFor(list1, list2):
	zipped = zip(list1, list2)
	result = []
	for x,y in zipped:
		result.append(x*y)

zippFor(list1, list2)

print("For loops with indexing")
@timeit
def onlyFor(list1, list2):
	result = []
	for i in range(0, len(list1)):
		result.append(list1[i]*list2[i])

onlyFor(list1, list2)

print("List comprehension")
@timeit
def lstComp(list1, list2):
	result = [list1[i]*list2[i] for i in range(0, len(list1))]
lstComp(list1, list2)



#########################################################################################
print("\n\nc")
@timeit
def randList():
	return [random.uniform(0, 1) for i in range(0, 10000)]



#######################################################################################
print("\n\nd")
@timeit
def randTupl():
	return tuple(random.uniform(0, 1) for i in range(0, 10000))



#########################################################################################
print("\n\ne")
def median(lst):
	length = len(lst)
	middle = int(length/2)
	median_index = 0
	if length%2 == 0:
		median = (lst[middle-1] + lst[middle+1])/2
	else:
		median_index = middle+1
	return median_index

lst = [random.uniform(0, 1) for i in range(0, 10000)]
tupl = tuple(random.uniform(0, 1) for i in range(0, 10000))
lst_median_index = median(lst)
tupl_median_index = median(tupl)

print("List indexing")
@timeit
def getListMedian(median_index, lst):
	return lst[median_index]
getListMedian(lst_median_index, lst)

print("Tuple indexing")
@timeit
def getTuplMedian(median_index, tupl):
	return tupl[median_index]
getTuplMedian(tupl_median_index, tupl)



##########################################################################################
print("\n\ng")
@timeit
def dictionary():
	Dict = {'gauss': [], 'lognormvariate': [], 'normalvariate': []}
	mu = 20
	sigma = 5
	for i in range(0, 1000):
		Dict['gauss'] = random.gauss(mu, sigma)
		Dict['lognormvariate'] = random.lognormvariate(mu, sigma)
		Dict['normalvariate'] = random.normalvariate(mu, sigma)
dictionary()

