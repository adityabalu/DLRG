def listmultiply1(list1, list2):
	zipped = zip(list1, list2)
	zipped = [(int(x),int(y)) for x,y in zipped if str(x).isdigit() and str(y).isdigit()]
	result = [(x*y) for x, y in zipped]
	return result

ls1 = listmultiply1(['12', '13', 'Hello', '4', '6', '10]'], ['2', '3', '4', 5, '[6', 12, 14])
print(ls1)
