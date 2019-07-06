class India:
    def getCity(self):
        self.__City = input('Enter City: ')
    def putCity(self):
        print(self.__City)
    def searchCity(self, pattern, status):
        if status == 's':
            if self.__City.startswith(pattern):
                return True
        elif status == 'e':
            if self.__City.endswith(pattern):
                return True
        return False
l = [India(),India(),India(),India(),India(),India()]
for x in l:
    x.getCity()
p = input('Enter pattern: ')
s = input('s/e: ')
for x in l:
    if x.searchCity(p, s):
        x.putCity()


