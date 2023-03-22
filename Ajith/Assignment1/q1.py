def appendNum(n, length):
	
	if n==0:
		return ['']
	elif n==1:
		return ['0', '1', '8']

	middle = appendNum(n-2, length)
	strobo = []

	for num in middle:
		if n!=length:
			strobo.append('0'+num+'0')
		strobo.append('1'+num+'1')
		strobo.append('6'+num+'9')
		strobo.append('8'+num+'8')
		strobo.append('9'+num+'6')
	return strobo

def strobogrammatic(n):

	return appendNum(n, n)


print(strobogrammatic(3))