class Person:
    def __init__(self, fname, lname):
        self.firstName=fname
        self.lastName=lname

    def printname(self):
        print(self.firstName, self.lastName)
    
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x= Student("Mike","Olsen")
x.printname()