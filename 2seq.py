myList = input('Введите значения элементов списка через чё угодно: ').replace(';', ',').replace('/', ',').split(',')
print(myList)
myList.sort()
temp = []
for i in myList:
    count_entries = myList.count(i)
    if count_entries == 1:
        temp.append(i)
print(temp)