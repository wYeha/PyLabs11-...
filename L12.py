fname = input("Введите имя файла для отображения: ")
inf = open(fname, "r")

line=inf.readline().split()

for word in range(len(line)-1):
    if line[word]==line[word+1]:
        print("Word",line[word],"repeated")


inf.close()