"""class Matrix:
    def getMatrix(self, row, col):
        self.row = row
        self.col = col
        self.matrix = []
        for x in range(row):
                self.matrix.append([int(x) for x in input().split()])
    def putMatrix(self):
        for x in self.matrix:
            for y in x:
                print(y, end = ' ')
            print()
    def __add__(self, o):
        R = Matrix()
        R.matrix = []
        for x in range(self.row):
            l = []
            for y in range(self.col):
                l.append(self.matrix[x][y] + o.matrix[x][y])
            R.matrix.append(l)
        return R
m1 = Matrix()
m2 = Matrix()
print('Enter row and col seperated by space: ', end = '')
row, col = [int(x) for x in input().split()]
print('Input Matrix 1:')
m1.getMatrix(row, col)
print('Input Matrix 2:')
m2.getMatrix(row, col)
m3 = m1 + m2
print('Matrix SUM:')
m3.putMatrix()"""

"""class Patient:
    __billAmount = 0
    __pBusiness = 0
    __pService = 0
    __pBPL = 0
    __BusinessRevenue = 0
    __ServiceRevenue = 0
    __BPLRevenue = 0
    def getDetails(self):
        self.id = input('Enter ID: ')
        self.category = input('Enter Category: ')
        self.name = input('Enter Name: ')
        if self.category == 'Service':
            Patient.__pService += 1
            Patient.__ServiceRevenue += 100 - (100*0.2)
        elif self.category == 'Business':
            Patient.__pBusiness += 1
            Patient.__BusinessRevenue += 100
        elif self.category == 'BPL':
            Patient.__pBPL += 1
    @classmethod
    def summary(cls):
        print(f'\n\nPatients:\nBusiness Class: {cls.__pBusiness}\nAmount Generated: {cls.__BusinessRevenue}\n\nService Class: {cls.__pService}\nAmount Generated: {cls.__ServiceRevenue}\n\nBPL: {cls.__pBPL}\nAmount Generated: {cls.__BPLRevenue}\n\n')
        print('Total Revenue: ', cls.__pBusiness*100 + cls.__pService*(100 - (100*0.2)))
while True:
    print('::: Hospital :::')
    p = Patient()
    p.getDetails()
    if int(input('More Paitients?(1/0): ')) == 0: break
Patient.summary()"""