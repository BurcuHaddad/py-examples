import json

x={
    "name":"John",
    "age":30,
    "married": True,
    "divorced": False,
    "pets": None,
    "children":("Ann","Billy"),
    "cars":[
        {"model": "BMW 230", "mpg":27.5},
        {"model":"Ford Edge", "mpg":24.1}
    ]
}
print(json.dumps(x,indent=4,separators=(". ", "= ")))