import re

#split the string at every white-sapce character:

txt="The rain in Spain"
x=re.split("\s",txt)
print(x)