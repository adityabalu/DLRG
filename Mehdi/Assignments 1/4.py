n = 3
x = ['Chapter' for x in range (n+1)]
y1 = enumerate(x)
y = [(s+" "+str(r+1)) for r,s in y1]

print(list(y))