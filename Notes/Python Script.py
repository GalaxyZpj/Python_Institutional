a = 10
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
print('{0:<10d}\n{1:>10d}\n{2:^10d}\n{3:10d}'.format(a, b, c, t))

#input
a = input('Enter number: ')
b = input('ENter number: ')
c = a + b
#c = a - b //not possible
#c = a * b //not possible
a = int(input('Enter number: ')) #same for float
b = int(input('Enter number: '))
c = a + b
#if
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
    print(i)
