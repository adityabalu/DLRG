n = int(input("Please type the number of Chapters: "))
chapter_list = []

for i in range(n+1):
    chapter_list.append("Chapter")
    y = list(enumerate(chapter_list, start=1))
z = [(i[1] + " " + str(i[0])) for i in y]
print(z)