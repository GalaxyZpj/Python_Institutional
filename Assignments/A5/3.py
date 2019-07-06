class India:
    def getCity(self):
        self.__state = input('Enter State: ')
        self.__city = input('Enter city: ')
    def putCity(self):
        print(self.__city)
    def searchState(self, state):
        if state == self.__state:
            return True
        return False
l = [India(),India(),India(),India(),India()]
for x in l:
    x.getCity()
s = input('Enter State: ')
for x in l:
    if x.searchState(s):
        x.putCity()