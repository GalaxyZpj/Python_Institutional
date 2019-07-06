class Student:
    def getStudent(self):
        self.__rollno = input('Enter Roll Number: ')
        self.__name = input('Enter Name: ')
        self.__aggregatePercentage = int(input('Enter Aggregate Percentage: '))
        self.__highSecondaryPercentage = int(input('Enter High Secondary Percentage: '))
        self.__highSchoolPercentage = int(input('Enter High School Percentage: '))
        self.__backlog = input('Backlog(Yes/No): ')
        self.__age = int(input('Enter Age: '))
    def putStudent(self):
        print(f'\nName: {self.__name}\nRollNo: {self.__rollno}\nAge: {self.__age}\n')
    def search(self, agg, sec, sch, back):
        if self.__aggregatePercentage >= agg and self.__highSecondaryPercentage >= sec and self.__highSchoolPercentage and self.__backlog == back:
            return True
        return False
record = [Student(),Student(),Student(),]
for x in record:
    x.getStudent()
agg = int(input('Enter Required Aggregate Percentage: '))
sec = int(input('Enter Required High Secondary Percentage: '))
sch = int(input('Enter Required High School Percentage: '))
back = input('Backlogs Accepted(Yes/No): ')
for x in record:
    if x.search(agg, sec, sch, back):
        x.putStudent()
