import re

txt="The rain in Spain"
x=re.search("\s", txt)

print("the first white-space character is located in position:", x.start())