import json

#a python object (dict):
x={"name":"John","age":30, "city":"NY"}

#convert into JSON:
y=json.dumps(x)

#the result is a JSON string:
print(y)