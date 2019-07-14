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

#Dictionary
"""d = {}
d = dict()
d = {'0751': 'Gwalior', '0123': 'Noida', '0731': 'Indore'}
print(d['0123'])
d['0123'] = 'Bhopal'
print(d['0123'])
print(d.get('075', 'Not found.'))
d = {1: 'one', 2: 'Two'}
for key in d.keys():
    print(key, d[key])
d = {'0751': 'Gwalior', '0123': 'Noida', '0731': 'Indore'}
v = d.values()
print(v)
for i in v:
    print(i)
v = d.items()
for i in v:
    print(i)

d = dict()
for i in range(3):
    id = input('Enter id: ')
    name = input('Enter Name: ')
    d.setdefault(id, name)
print(d)

d = {'100': 'Madhya Pradesh', '200': 'Bihar', '300': 'Haryana'}
i = {'400': 'Uttar Pradesh', '500': 'Uttrakhand'}
d.update(i)
print(d)

d = {'100': 'Ajay', '200': 'Vikas', '300': 'Peter'}
d.pop('200')

#String Method
k = '@@@@@'
m = 'Ravi Kumar'
k.join(m)


x = 'Gwalior'
y = list(x)
j = ''
j.join(y)"""

"""#Set
x = {5,6,7,8,3,4,5,6,7,8,1}
x.add(100)
y = [9,8,6,6,4,4,4]
x.update(y)
y = {100, 200, 300}
x.union(y)
y = {100, 200, 4,5,1,300}
x.intersection(y)
x.difference(y)
x.issuperset(y)
L = [3,5,6,7,7]
s = set(L)
L = [[10,20], [40,60], [50,80]]
D = dict(L)
#L = [[10,20,30], [40,60], [50,80]]     //not possible cause only 2 values needed to form a dictionary"""

#zip()
"""l1 = [1,2,3,4,5,6]
l2 = [10,20,30,40,50,60]
z = zip(l1, l2)
l3 = list(z)
z = zip(l1, l2)
a, b = zip(*z)
z = zip(l1, l2)
k = zip(*z)"""

#Creating a function
"""def sum(a, b):
    c = a+b
    return c
k = sum(100, 200)
print(k)"""

#Taking multiple arguments
"""def Call (*n):
    print(n)
Call(8, 2, 3)"""

#Returning multiple values
"""def Call(a, b):
    s1 = a+b
    s2 = a-b
    s3 = a*b
    return s1, s2, s3
k, m, j - Call(8, 5)
print(k, m, j)"""

#Lambda Expressions
"""c = lambda x, y: x+y
k = c(80, 90)
print(k)

#Single line statements
L = [i for i in range(2, 20, 2)]
c = lambda x, y: x if (x>y) else y"""

#Map Function:
"""l1 = [10,50,80,60,89,10]
l1 = [4,7,8,9]
k = [map(lambda x, y: x+y, l1, l2)]
print(k)"""

#Filter Function
"""l1 = [10,40,33,56,77,81,24,57,80]
k = [filter(lambda x:x%2 == 0, l1)]
print(k)
k = [filter(lambda x:(x >= 50 and x <= 90), l1)]
print(k)"""

#Reduce Function
"""from functools import reduce
print(reduce(lambda x, y:x+y, [100,200,30,50,70]))"""

#Class
"""class PNB:
    def OpenAccount(self):
        self.ano = input('Enter Account Number: ')
        self.name = input('Enter Name: ')
        self.balance = int(input('Enter Balance: '))

    def showAccount(self):
        print(self.ano, self.name, self.balance)"""

#Creating n number of objects
"""class Student:
    def getStudent(self):
        self.rollno = input('Enter roll no: ')
        self.name = input('Enter name: ')
        self.p = int(input('Enter Physics marks: '))
        self.c = int(input('Enter Chemistry marks: '))
        self.m = int(input('Enter Maths marks: '))
    def putStudent(self):
        print(self.rollno, self.name, self.p, self.c, self.m)
    def search(self, rollno):
        if rollno == self.rollno:
            self.putStudent()
            return True
        else: return False
L = list()
n = int(input('Enter no. of students: '))
for i in range(n):
    s = Student()
    s.getStudent()
    L.append(s)
rollno = input('Enter roll number to be searched: ')
for s in L:
    found = s.search(rollno)
    if found:
        break"""

#Static Members and Methods
"""class Bank:
    __bankbalance = 0       # static member
    def OpenAccount(self):
        self.__acno = input('Enter Account Number: ')
        self.__name = input('Enter Name: ')
        self.__balance = int(input('Enter Balance: '))
        Bank.__bankbalance += self.__balance

    def ShowAccount(self):
        print(self.__acno, self.__name, self.__balance)
    
    @classmethod
    def showBankBalance(cls):
        print('Bank Balance: ', cls.__bankbalance)

l = []
for i in range(3):
    c = Bank()
    c.OpenAccount()
    L.append(c)

for c in l:
    c.ShowAccount()
Bank.showBankBalance()"""

"""class Hero:
    __s = 0
    __p = 0
    __c = 0
    def getbike(self):
        self.id = int(input('Enter ID: '))
        self.name = input('Enter name: ')
        if self.name == 'splender':
            Hero.__s += 1
        elif self.name == 'cd deluxe':
            Hero.__c += 1
        elif self.name == 'passion':
            Hero.__p += 1
    def putbike(self):
        print(self.id, self.name)
    
    @classmethod
    def production(cls):
        print('Total Production: ', cls.__s + cls.__p + cls.__c)"""

#Object as an Argument
"""class TwoNum:
    def getTwoNum(self):
        self.__x = int(input('Enter '))
        self.__y = int(input('Enter '))
    def putTwoNum(self):
        print(self.__x, seld.__y)
    def Add(self, A):
        R = TwoNum()
        R.__x = self.__x + A.__x
        R.__y = self.__y + A.__y
        return R
T1 = TwoNum()
T1.getTwoNum()
T2 = TwoNum()
T2.getTwoNum()
T3 = T1.Add(T2)
T1.putTwoNum()
T2.putTwoNum()
T3.putTwoNum()"""

#Constructor & Destructor
"""class Car:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    def getCar(self):
        self.__name = input("Enter Name: ")
        self.__price = int(input('Enter Price: '))
    def showCar(self):
        print(self.__name, ':', self.__price)
    def __del__(self):
        print('Destroyed Car', self.__name)
c = Car('Honda City', 1400000)
c.showCar()
del c
c.getCar()
c.showCar()
"""

#AlienGame
"""class Alien:
    points = 0
    def __init__(self, name, point):
        self.name = name
        self.point = point
        print(f'Alien {self.name} Created.')
    @classmethod
    def showPoint(cls):
        print('Points: ',Alien.points)
    def __del__(self):
        print(self.name, 'Destroyed.')
        Alien.points += self.point
a = Alien('Pranav', 5)
b = Alien('Harsh', 10)
del a
del b
Alien.showPoint()"""

#Inheritance
"""class Student:
    def getStudent(self):
        self.__rollno = input('Enter Roll Number: ')
        self.__name = input('Enter Name: ')
    def putStudent(self):
        print(self.__rollno, self.__name)
class Bsc(Student):
    def getBsc(self):
        self.getStudent()
        self._p = int(input('Enter Physics: '))
        self._c = int(input('Enter Chemistry: '))
        self._m = int(input('Enter Math: '))
    def putBsc(self):
        self.putStudent()
        print(self._p, self._c, self._m)       
# s = Bsc()
# s.getBsc()
# s.putBsc()
class Result(Bsc):
    def getResult(self):
        self.getBsc()
        self.__total = self._p + self._c + self._m
    def putResult(self):
        self.putBsc()
        print('Total: ', self.__total)
s = Result()
s.getResult()
s.putResult()"""
#Multiple Inheritance
"""class ProductionOne:
    def getProductionOne(self):
        self._one = int(input('Enter Production One: '))
    def showProductionOne(self):
        print('Production One: ', self._one)
class ProductionTwo:
    def getProductionTwo(self):
        self._two = int(input('Enter Production Two: '))
    def showProductionTwo(self):
        print('Production Two: ', self._two)
class TotalProduction(ProductionOne, ProductionTwo):
    def totalProduction(self):
        self.getProductionOne()
        self.getProductionTwo()
        self.__total = self._one + self._two
    def showTotalProduction(self):
        self.showProductionOne()
        self.showProductionTwo()
        print('Total Production: ', self.__total)
t = TotalProduction()
t.totalProduction()
t.showTotalProduction()"""
# MultiLevel Inheritance
"""class Employee:
    def getEmployee(self):
        self.__id = input('Enter ID: ')
        self.__name = input('Enter Name: ')
        self.__salary = int(input('Enter Salary: '))
        return self.__salary
class Perks(Employee):
    def returnTotal(self):
        s = self.getEmployee()
        self.__da = s * 0.5
        self.__hra = s * 0.16
        self.__pf = s * 0.05
        return self.__da + self.__hra - self.__pf
class NetSalary(Perks):
    def netShow(self):
        print('Net Salary: ', self.returnTotal())
e = NetSalary()
e.netShow()"""
#Abstraction
"""from abc import ABC, abstractmethod
class Student(ABC):
    @abstractmethod
    def Get(self):
        pass
    def Put(self):
        pass
class Bsc(Student):
    def Get(self):
        self.__rollno = input('Enter Roll Number: ')
        self.__name = input('Enter Name: ')
        self.__p = int(input('Enter Physics: '))
        self.__c = int(input('Enter Chemistry: '))
        self.__m = int(input('Enter Math: '))
    def Put(self):
        print(self.__p, self.__c, self.__m)   
class Ba(Student):
    def Get(self):
        self.__rollno = input('Enter Roll Number: ')
        self.__name = input('Enter Name: ')
        self.__h = int(input('Enter History: '))
        self.__g = int(input('Enter Geography: '))
        self.__e = int(input('Enter Economics: '))
    def Put(self):
        print(self.__h, self.__g, self.__e)     
L = [Bsc(), Bsc(), Ba(), Ba()]
for student in L:
    student.Get()
    student.Put()"""

"""from abc import ABC, abstractmethod
class Shapes(ABC):
    @abstractmethod
    def getDimentions(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Triangle(Shapes):
    def getDimentions(self):
        self.height = int(input('Enter Height: '))
        self.base = int(input('Enter Base: '))
    def area(self):
        print('Area of the triangle is:', 0.5*self.height*self.base)
class Rectangle(Shapes):
    def getDimentions(self):
        self.length = int(input('Enter Length: '))
        self.breadth = int(input('Enter Breadth: '))
    def area(self):
        print('Area of the rectangle is:', self.length*self.breadth)
r = Rectangle()
r.getDimentions()
r.area()
t = Triangle()
t.getDimentions()
t.area()"""

#Exception Handling

"""try:
    v = int(input("Enter Any Value: "))
    print(v)
except Exception as e:
    print('Invalid Input.', e)"""

"""while True:
    try:
        v1 = int(input('Enter Any Value: '))
        print(v1)
        break
    except ValueError as e:
        print('Invalid Input', e)"""

# File Handling
"""f = open('/Users/pranavjain/Github/Python_Institutional/Notes/File Handling/1.txt', 'w')    #create a file in write mode
f.write('LG')
f.write('Samsung')
f.close()"""

"""f = open('/Users/pranavjain/Github/Python_Institutional/Notes/File Handling/1.txt', 'a')    #create a file in write mode
while True:
    name = input('Enter Name: ')
    if name == '': break
    f.write(name)
    f.write('\n')
f.close()"""

"""f = open('/Users/pranavjain/Github/Python_Institutional/Notes/File Handling/1.txt', 'r')
data = f.read()
print(data)
f.close()"""

"""from time import sleep as s
f = open('/Users/pranavjain/Github/Python_Institutional/Notes/File Handling/1.txt', 'r')
while True:
    data = f.read(1)
    if data == '': break
    print(data)
    s(0.5)
f.close()

f = open('/Users/pranavjain/Github/Python_Institutional/Notes/File Handling/students.txt', 'a')
while True:
    record = input('Enter Roll Number, Name and P, C, M Marks: ')
    if record == '': break
    f.write(record)
f.close()"""


# Threading
import threading
import random
from time import sleep
# Printer
"""class Printer(threading.Thread):
    def run(self):
        lock.acquire()
        print(self.getName())
        sleep(0.5)
        lock.release()
lock = threading.Lock()
u1 = Printer()
u2 = Printer()
u3 = Printer()
u1.setName('Hello')
u2.setName('Hi')
u3.setName('Bye')
u1.start()
u2.start()
u3.start()
"""
# Spell Checker
"""
class SpellChecker(threading.Thread):
    def init(self):
        self.list = ['tool', 'setup', 'utilities']
        self.x = ''
    def run(self):
            while True:
                if self.x in self.list: 
                    print('OK')
                    
                else: 
                    print('Not Found')
word = SpellChecker()
word.init()
word.start()
while True:
    word.x = input('Enter word: ')
"""
# MatchStick Game
class Dice(threading.Thread):
    dice = [1]*10
    def init(self):
        self.inp = 'random'
    def run(self):
        while True:
            self.turn = random.choice(range(0, 10))
            if self.inp != 'random':
                Dice.dice[self.turn] = 0
                self.inp = 'random'
x = Dice()
x.init()
x.setDaemon(True)
print(Dice.dice)
x.start()
winner = 0
while True:
    print(':: Player 1 ::')
    x.inp = input('Press ENTER to ROLL: ')
    winner = 1
    print('\n', Dice.dice, '\n')
    if all(x==0 for x in Dice.dice): break
    print(':: Player 2 ::')
    x.inp = input('Press ENTER to ROLL: ')
    winner = 2
    print('\n', Dice.dice, '\n')
    if all(x==0 for x in Dice.dice): break
print(f"\n\nPlayer {winner} wins!\n\n")
