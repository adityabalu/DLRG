def Chapters(n):
	return ['Chapter {}'.format(i) for i in range(1, n+2)]

if __name__ == '__main__':
	n = 5
	chapter_list = Chapters(n)
	print('Chapter List: ' + '\n', chapter_list)
