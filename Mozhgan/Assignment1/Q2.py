a, b = input("please type two desired words: ").split()
c, d = input("please type two other desired words: ").split()
list1 = a, b
list2 = c, d

xy = zip(list1, list2)
final = []
for i in xy:
        final.append(" ".join(i))
        z = list(map(lambda x: x.lower(), final))
        print(z)

