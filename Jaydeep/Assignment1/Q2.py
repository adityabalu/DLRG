def concatenateStringsLowercase(list1, list2):
	concatenated_list = []
	if len(list1) != len(list2):
		raise Exception("Length of both list must be same")
	else:	
		for l1, l2 in zip(list1, list2):
			concatenated_list.append(l1.lower() + ' ' + l2.lower())
		return concatenated_list

if __name__ == '__main__':
	list1 = ['HellO', 'BYe']
	list2 =  ['woRlD', 'WOrld']
	concatenated_list = concatenateStringsLowercase(list1, list2)

	print('Concatenated list with all lower case and space between it: ' + '\n', concatenated_list)
