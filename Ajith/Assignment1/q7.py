import time

def timeit(function):

	def calculate_time(*args, **kwargs):

		start = time.time()

		function(*args, **kwargs)

		end = time.time()

		print(end-start)

	return calculate_time