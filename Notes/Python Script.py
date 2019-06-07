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
