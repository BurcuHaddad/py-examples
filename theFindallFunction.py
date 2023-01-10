import re
#return a list containing every occurence of "ai":

txt="The rain in Spain"
x=re.findall("ai",txt)
print(x)