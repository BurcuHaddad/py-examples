import re
#replace the first two occurences all white-space with the digit 9:

txt="The rain in Spain"
x=re.sub("\s", "9", txt, 2)
print(x)