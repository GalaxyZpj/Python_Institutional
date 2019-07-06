from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def getEmployee(self):
        pass
    @abstractmethod
    def putEmployee(self):
        pass
class Google(Employee):
    orgName = 'Google'
    numEmployee = int(input('Enter no. of employees working in Google: '))
    def getEmployee(self):
        print(f'\nOrganization: {Google.orgName}')
        self.__name = input('Enter Name: ')
        self.__sex = input('Enter Gender: ')
        self.__jobTitle = input('Enter Job Title: ')
        self.__dob = input('Enter Date of Birth: ')
    def putEmployee(self):
        print(Google.orgName, 'Employee:-')
        print(self.__name, self.__sex, self.__jobTitle, self.__dob)
        return (self.__name, self.__sex, self.__dob)
class Microsoft(Employee):
    orgName = 'Microsoft'
    numEmployee = int(input('Enter no. of employees working in Microsoft: '))
    def getEmployee(self):
        print(f'\nOrganization: {Microsoft.orgName}')
        self.__name = input('Enter Name: ')
        self.__sex = input('Enter Gender: ')
        self.__jobTitle = input('Enter Job Title: ')
        self.__dob = input('Enter Date of Birth: ')
    def putEmployee(self):
        print(Google.orgName, 'Employee:-')
        print(self.__name, self.__sex, self.__jobTitle, self.__dob)
        return (self.__name, self.__sex, self.__dob)
def similarity(a, b):
    if a.putEmployee() == b.putEmployee():
        print('\nThese Employees are equal to one another.')
    else:
        print('\nEmployees are not equal.')
    if a.orgName == b.orgName:
        print('They work in same organization.\n\n')
    else:
        print('They donot work in same organization.\n\n')
L = [Microsoft(), Google(), Google(), Microsoft()]
for x in L:
    x.getEmployee()
for i,x in enumerate(L):
    j = i+1
    while j < len(L):
        if x == L[j]: continue
        similarity(x, L[j])
        j += 1
