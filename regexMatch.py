import re
#the search() function returns a match object:

txt="The rain in Spain"
x=re.search("ai", txt)
print(x)