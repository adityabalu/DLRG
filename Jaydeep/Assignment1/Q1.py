def  strobogrammaticNumbers(n, len_num):
	edge_set = ['00', '11', '88', '69', '96']
	if n == 0: return ['']
	if n == 1: return ['1', '0', '8']
	center = strobogrammaticNumbers(n-2, len_num)	
	numbers = []
	for cent in center:
		if n != len_num:
			for edge in edge_set:
				left, right = edge[0], edge[1]
				numbers.append(left + cent + right)
		else:
			for edge in edge_set[1:]:
				left, right = edge[0], edge[1]
				numbers.append(left + cent + right)
	return numbers

if __name__ == '__main__':
	num = 5
	all_possible_numbers = strobogrammaticNumbers(num,num)
	print('Total possible strobogrammatic numbers of length {} = {}'.format(num, len(all_possible_numbers)))
	print('All possible strobogrammatic numbers: ' + '\n', all_possible_numbers)
