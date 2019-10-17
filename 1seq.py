print('Enter number of elements ')
a = int(input())
myList = []
for i in range(a):
    print('Enter new element of your list (only digit!!!!): ')
    num = int(input())
    myList.append(num)
print(myList)
myList.sort()
print(myList)