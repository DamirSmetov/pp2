import re

x = open("row.txt ", "r")
y = x.read()
z = re.split("\s", y)
for i in z:
    k = re.search(r"а.+б$", i)
    if k == None:
        continue
    else:
        print(i,"matches")

x.close()