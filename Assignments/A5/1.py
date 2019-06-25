class Product:
    def getProduct(self):
        self.__id = int(input('Enter ID: '))
        self.__name = input('Enter Name: ')
        self.__rate = input('Enter Rate: ')
        self.__stock = input('Enter Stock: ')
    def showProducts(self):
        print(self.__id, self.__name, self.__rate, self.__stock)
    @staticmethod
    def search_id(l, id):
        found = False
        for x in l:
            if x.__id == id:
                found = True
                return L.index(x)
        if not found:
            return -1
L = []
for _ in range(int(input('Enter number of elements: '))):
    s = Product()
    s.getProduct()
    L.append(s)
print('Object Index: ',Product.search_id(L, 4))

