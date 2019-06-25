class India:
    def getCity(self):
        self.__statename = input('Enter State: ')
        self.__cityname = input('Enter city: ')
    def putCity(self):
        print(f'State: {self.__statename} City: {self.__cityname}')
    @staticmethod
    def searchCityByState(l)