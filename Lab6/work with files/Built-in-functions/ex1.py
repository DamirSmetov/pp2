res = 1

def mult(x):
    global res
    res *= x
    return res
    
    

list1 = [1, 2, 3]
a = map(lambda x : x * 2, list1)
b = map(mult, list1)
c = list(b)
print(list(a))
print(c[-1])