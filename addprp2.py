class Person:
    def __init__(self, fname, lname):
        self.firstName= fname
        self.lastName= lname
    
    def printname(self):
        print(self.firstName, self.lastName)

class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname,lname)
        self.graduationyear= year

x=Student("Mike","Olsen", 2019)
print(x.graduationyear)