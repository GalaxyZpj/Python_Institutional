"""class Bank:
    def create(self):
        self.__accno = input('Enter account no: ')
        self.__name = input('Enter Name: ')
        self.__balance = 0
        return self.__accno
    def display(self):
        print(f'{self.__accno}: {self.__name}')
    def search_name(self, ss):
        found = True
        for i in range(len(self.__name)):
            if self.__name[i: i+len(ss)] == ss: return found
        if not found:
            return False
    def deposit(self):
        self.__balance += int(input('Enter Amount: '))
        print('Amount added to your Account.')
    def withdrawal(self):
        amount = int(input('Enter Amount: '))
        if self.__balance > amount:
            self.__balance -= amount
            print(f'{amount} deducted form your account.')
        else: print('Not enough Balance.')
D = {}
for i in range(int(input('Enter no. of customers: '))):
    s = Bank()
    D.setdefault(s.create(), s)
while True:
    print('\n::: Menu :::')
    print('1. Display All')
    print('2. Search By Account Number')
    print('3. Search by Name/Surname')
    print('4. Deposit')
    print('5. Withdraw')
    print('6. Exit')
    c = int(input('Enter your choice: '))
    if c == 1:
        for x in D.values():
            x.display()
    elif c == 2:
        r = D.get(input('Enter Account Number: '), 'Not Found')
        if isinstance(r, Bank): r.display()
        else: print(r)
    elif c == 3:
        ss = input('Enter the string: ')
        i = 0
        for x in D.values():
            if x.search_name(ss):
                x.display()
                i += 1
        if i == 0:
            print('Record not found.')
    elif c == 4:
        r = D.get(input('Enter Account Number: '), 'Not Found')
        if isinstance(r, Bank): r.deposit()
        else: print(r)
    elif c == 5:
        r = D.get(input('Enter Account Number: '), 'Not Found')
        if isinstance(r, Bank): r.withdrawal()
        else: print(r)
    elif c == 6:
        break
    else:
        print('Invalid Choice.')"""

class Product:
    def getProduct(self):
        self.id = input('Enter id: ')
        self.name = input('Enter name: ')
        self.price = int(input('Enter price: '))
        self.stock = int(input('Enter stock available: '))
        return self.id
    def putProduct(self):
        print(self.id, self.name, self.price, self.stock)
    def search_price(self, min, max):
        if self.price > min and self.price < max:
            return True
        else: return False
    def sale(self):
        q = int(input('Enter Quantity: '))
        if q >= self.stock:
            print('Not enough Stock.')
        else:
            self.stock -= (self.price * q)
            print('Item added to cart.')
    def purchase(self):
        pass
D = {}
for x in range(int(input('Enter number of Products: '))):
    x = Product()
    D.setdefault(x.getProduct(), x)
while True:
    print('\n::: Menu :::')
    print('1. Display all Products')
    print('2. Search by Price')
    print('3. Sale')
    print('4. Purchase')
    print('5. Exit')
    c = int(input('Enter your choice: '))
    if c == 1:
        for x in D.values():
            x.putProduct()
    elif c == 2:
        min, max = (int(x) for x in input('Enter Min and Max price seperated by a space: ').split())
        found = False
        for x in D.values():
            if x.search_price(min, max):
                x.putProduct()
                found = True
                break
        if not found:
            print('No Product found within the given range.')
    elif c == 3:
        s = input('Enter Product Name: ')
        found = False
        for x in D.values():
            if s == x.name:
                x.sale()
                found = True
        if not found:
            print('Product not found.')
    elif c == 4:
        pass
    elif c == 5:
        break
    else:
        print('Invalid Choice.')

