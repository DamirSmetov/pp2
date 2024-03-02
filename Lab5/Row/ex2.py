import re


x = open("row.txt ", "r")
y = x.read()
z = re.split("\s", y)
for i in z:
    k = re.search(r"аб{2,3}", i)
    if k == None:
        print(i, "does not match")
    else:
        print(i,"matches")

x.close()