#Python Syntax:
#Ex.1
print ("Hello World")
#Ex.2
if 5 > 2:
    print("YES")
#Python comments:
#Ex.1
#This is a comment
#Ex.2
"""
This is a comment
written in 
more than just one line
"""
#Python variables:
#Ex.1
carname = "Volvo"
#Ex.2
x = 50
#Ex.3
x = 5
y = 10
print(x + y)
#Ex.4
x = 5
y = 10
z = x + y
print (z)
#Ex.5
x, y, z = "Orange", "Banana", "Cherry"
#Ex.6
x = y = z = "Orange"
#Ex.7
def myfunc():
    global x
    x = "fantastic"
#Python Data types:
#Ex.1
x = 5
print (type(x))
#int
#Ex.2
x = "Hello World"
print (type(x))
#str
#Ex.3
x = 20.5 
print (type(x))
#float
#Ex.4
x = ["apple", "banana", "cherry"]
print (type(x))
#list
#Ex.5
x = ("apple", "banana", "cherry")
print (type(x))
#tuple
#Ex.6
x = {"name" : "John", "age" : 36}
print (type(x))
#dict
#Ex.7
x = True
print (type(x))
#bool
#Python numbers:
#Ex.1
x = 5
x = float(x)
#Ex.2
x = 5.5 
x = int(x)
#Ex.3
x = 5
x = complex(x)
#Python strings
#Ex.1
x = "Hello World"
print (len(x))
#Ex.2
txt = "Hello World"
x = txt[0]
#Ex.3
txt = "Hello World"
x = txt[2:5]
#Ex.4
txt = " Hello World "
x = txt.strip()
#Ex.5
txt = "Hello World"
txt = txt.upper()
#Ex.6
txt = "Hello World"
txt = txt.lower()
#Ex.7
txt = "Hello World"
txt = txt.replace("H", "j")
#Ex.8
age = 36
txt = "My name is John, and I am {}"
print (txt.format(age))
