#the try block will generate a nameerror, because x is not defined:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")