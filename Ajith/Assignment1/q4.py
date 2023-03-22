def index(n):
	chapters = [y + ' ' + str(x+1) for x,y in enumerate(['chapter' for i in range(0, n)])]
	return chapters

print(index(3))
