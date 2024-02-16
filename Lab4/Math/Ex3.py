import math

n = int(input("Number of sides: "))
l = int(input("The lenght of sides: "))
s = (n*l**2)/(4*float((math.tan(math.radians(180/n)))))
print(s)

