import re

x = open("row.txt ", "r")
y = x.read()
z = re.sub("[ ,.]", ":", y)
print(z)

x.close()