class Person:
    def __init__(self, fname, lname):
        self.firstName=fname
        self.lastName=lname

    def printname(self):
        print(self.firstName, self.lastName)
    
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x= Student("Mike","Olsen")
x.printname()

#the child class still inherited __init__() function from the parent