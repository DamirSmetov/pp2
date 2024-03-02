import re

x = open("row.txt ", "r")
y = x.read()
z = re.findall(r"[А-Я][а-я]+", y)
print(z)

x.close()