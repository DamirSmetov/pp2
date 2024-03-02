import re

s = "BarcelonaIsTheBest"
x = re.findall("[A-Z][a-z]*", s)
print(x)