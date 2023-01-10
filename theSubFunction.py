import re
#replace all white-space with the digit 9:

txt="The rain in Spain"
x=re.sub("\s", "9", txt)
print(x)