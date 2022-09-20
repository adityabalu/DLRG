def Product(list1, list2):
	products = []
	
	for l1, l2 in zip(list1, list2):
		if not isinstance(l1, int):
			if l1.isdigit():
				l1 = int(l1)
		if not isinstance(l2, int):
			if l2.isdigit():
				l2 = int(l2)

		if isinstance(l1, int) and isinstance(l2, int):
			products.append(int(l1) * int(l2))

	return products

if __name__ == '__main__':
	list1 = [ '12', '13', 'Hello', '4', '6', '10]']
	list2 =  ['2', '3', '4', 5, '[6', 12, 14]
	products = Product(list1, list2)

	print('Possible products: ' + '\n', products)
