import re
#search for an upper case "S" character in the beginning of a word, and print the word:

txt="the rain in Spain"
x=re.search(r"\bS\w+", txt)
print(x.group())