myL_01 = input('Введите значения элементов списка через чё угодно: ').replace(';', ',').replace('/', ',').split(',')
myL_02 = input('Введите значения элементов списка через чё угодно: ').replace(';', ',').replace('/', ',').split(',')
print(myL_01)
print(myL_02)
for i in myL_02:
    while i in myL_01:
        myL_01.remove(i)
print(myL_01)

myL01 = input('Введите значения элементов списка через чё угодно: ').replace(';', ',').replace('/', ',').split(',')
myL02 = input('Введите значения элементов списка через чё угодно: ').replace(';', ',').replace('/', ',').split(',')
print(myL01)
print(myL02)
i = 0
j = 0
while j < len(myL02):
    while i < len(myL01):
        if myL01[i] == myL02[j]:
            myL01.remove(myL01[i])
            i = i + 0
        else:
            i = i + 1
    j = j + 1
    i = 0
print(myL01)