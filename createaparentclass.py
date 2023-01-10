#Create a class named person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstName= fname
        self.lastName= lname

    def printname(self):
        print(self.firstName, self.lastName)

#use the person class to create an onject, and then execute the printname method:

x=Person("John", "Doe")
x.printname()