class Person:
    def __init__(self, fname, lname):
        self.firstName= fname
        self.lastName= lname
    
    def printname(self):
        print(self.firstName, self.lastName)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear= year

    def welcome(self):
        print("Welcome", self.firstName, self.lastName, "to the class of", self.graduationyear)

x=Student("Mike", "Olsen", 2019)
x.welcome()