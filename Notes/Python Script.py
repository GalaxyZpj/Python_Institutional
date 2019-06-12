"""a = 10
b = 30
c = a + b
print('%d, %d, %d'%(a, b, c))
print('%d, %f, %d'%(a, b, c))
print('%r, %r, %r'%(a, b, c))
print('Sum of %r and %r is %r'%(a, b, c))
#.format()
print("{}, {}, {}".format(a, b, c))
print("Sum of {} and {} is {}".format(a, b, c))
print("{0}, {1}, {2}, {0}".format(a, b, c)) #using index
print("{0:d}, {1:f}, {2}, {0}".format(a, b, c)) #conversions while printing
#Right allignment by spaces
a = 1000
b = 10
c = 100
t = a + b + c
print('{0:10d}\n{1:10d}\n{2:10d}\n{3:10d}'.format(a, b, c, t))
#Allignment
print('{0:<10d}\n{1:>10d}\n{2:^10d}\n{3:10d}'.format(a, b, c, t))"""

#input
"""a = input('Enter number: ')
b = input('ENter number: ')
c = a + b
#c = a - b //not possible
#c = a * b //not possible
a = int(input('Enter number: ')) #same for float
b = int(input('Enter number: '))
c = a + b"""
"""#if
amt = float(input('Enter Amount: '))
qty = float(input('Enter Quantity'))
tamt = amt * qty
print('Amount: ', tamt)
if(tamt >= 100000):
    dis = tamt * 20/100
elif(tamt >= 20000 and tamt <= 99999):
    dis = tamt * 10/100
else:
    dis = tamt * 5/100
print('Discount Amount: ', dis)
netamt = tamt - dis
print('Net Amount: ', netamt)

#while
n = int(input('Enter number'))
i = 1
while i <= 10:
    t = n * i
    print(n, 'x', i, ' = ', t)
    i += 1

#nested while
i = 1
while(i <= 5):
    j = 1
    while(j <= 5):
        print(j, end='')
        j = j+1
    i = i+1
    print()

#for
for i in range(1, 11):
    print(i)"""

#Strings
"""x = 'Gwalior'
x[0]
x[2:5]
x[0:]
x[2:]
x[:4]
x[0::2]
x[5:2:-1]       #will start from
x[::-1]     #reverse
x + ' ' : 'city'
x * 3
x > 'agra'
x.capitalize()
x = 'Agra'
x.casefold()

x = 'Jaipur'
x.startwith('Jai')
x.startwith('ai', 1)
x.endswith('pur')

x.center(15, '*')
x.ljust(10, '*')
x = '252'
x.ljust(10, '0')

s = 'the man the machine'
s.find('a')
i = s.find('a')
s = s.find('a', i+1)
i = s.find('the')
i = s.find('the', i+1)
i = s.find('ach')
i = s.index('ac')
i = s.index('act')      #will give error

x = 'GGGGwalior'
print(x.lstrip('G'))

x = 'the man the machine'
x.replace('the', 'that')
print(x.replace('the', 'that', 1))

x = 'Gwalior, Bhopal, Indore'
j = x.split(",")
j = x.split(",", 1)
x.rsplit(",", 1)
x = "this is test program"
k = x.partition("is")
#print(k)
x = 'Gwalior,Indore,Bhopal,Indore'
k = x.partition(",")
#print(k)
x = "this is test program"
j = x.title()
x = "4567"
x.zfill(10)"""

#Tuple
"""t = ()      //tuple declaration
t = tuple()     //declaration using a constructor
t = (65, 78, 90, 22, 33)
t = (78, 90.6, 'Bhopal', 'Indore', (90, 87, 88))
print(t[0])
print(t[3][1])
t1 = (10, 20, 30)
t2 = (1, 2, 3)
t3 = t1 + t2
print(t3)
print(t3*3)
print(t1>t2)        #True
t1 = (10, 20, 30, 40)
t2 = (1000, 1)
print(t1 > t2)      #False
t = tuple()
t += (78,)
t += (77,)
t += (79,)
print(t)        #, will be absent in the end of tuple
"""
#Lists
"""L = [30, 80, 67, 54]
print(L)
L = ['Ajay', 'Gwalior', 9.6, 67]
L[0] = 'Noida'
print(L)
L[2:]
L[::-1]
del L[0]
del L[1:]
#del L[49:30:-1]     #will delete elements in reverse
L = [[1,2,3],[5,6,7,8],[6,8,9]]
L = [1, 2, 3]
print(L[1][2])
L.append(90)
L.insert(3, "Gwalior")
L.insert(3, (1,3,4,5))
L.remove(1)
L.index(3)
L.sort()"""
