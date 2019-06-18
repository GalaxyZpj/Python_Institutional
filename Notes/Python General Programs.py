#Enter n number of elements in a tuple
"""t = ()
n = int(input('Enter no. of elements: '))
i = 0
while i < n:
    v = int(input())
    t += tuple(v)
    i = i+1
print(t)



for i in t:
    t += (int(input())
    if index+1 is n: break


s = ['Pranav', 'Khushi', 'Shreyansh']
for x in s:
    x = x.lower()
    print(x[0])
    break"""

#Sum of elements of list l1 and l2 into l3
"""n = int(input('Enter no. of elements: '))
l1 = []
l2 = []
l3 = []
print('List 1:-')
for x in range(n):
    l1.append(int(input('Enter Element: ')))
print('List 2:-')
for x in range(n):
    l2.append(int(input('Enter Element: ')))

for a, b in zip(l1, l2):
    l3.append(a+b)
print(f'L3: {l3}')"""

#Give no. of different types of datatype in the list
"""l = ['Gwalior', 'Bhopal', 77.6, 82, 97.9]
i_int = 0
i_str = 0
i_float = 0
i_list = 0
i_tuple = 0
for x in l:
    if isinstance(x, int):
        i_int += 1
    elif isinstance(x, str):
        i_str += 1
    elif isinstance(x, float):
        i_float += 1
    elif isinstance(x, list):
        i_list += 1
    elif isinstance(x, tuple):
        i_tuple += 1
print(f'int: {i_int}\tstr: {i_str}\tfloat: {i_float}\tlist: {i_list}\ttuple: {i_tuple}')"""

#Matrix
"""r = int(input('Enter no. of rows: '))
c = int(input('Enter no. of columns: '))
M = []
i = 0
j = 0
for row in range(r):
    L = []
    for col in range(c):
        L.append(int(input('')))
    M.append(L)
#Printing a Matrix
for row in M:
    for col in row:
        print(col, end = " ")
    print()
#Another Method of printing List "C style"
for i in range(len(M)):
    for j in range(len(L[i])):
        print(L[i][j], end = " ")
    print()"""

#Find Name accross marks >= 60
"""P = [60, 70, 85, 29, 44, 66]
N = ['Ajay', 'Harry', 'Vikas', 'Ankit', 'Vijay', 'Mohan']
print('Studens with score above 60:-')
for x,y in zip(P,N):
    if x >= 60:
        print(y)"""

#Creating a Dictionary from 2 lists
"""l1 = ['Pranav', 'Shreyansh', 'Harsh']
l2 = [12345, 67890, 22222]
d = {}
for x, y in zip(l1, l2):
    d[y] = x
print(d)"""
"""l1 = [1,2,3,4,5,6]
l2 = [10,20,30,40,50,60]
z = zip(l1, l2)
a = zip(*z)"""

#Calculate simple interest of given amounts
l = [7000,5000,45000,89000]
r = 7.5
t = 1
c = lambda: [amt*r*t/100 for amt in l]
print(c())
