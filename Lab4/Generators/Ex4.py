def list_of_numbers(a, b):
    for i in range(a, b+1):
            yield i**2
a = int(input())
b = int(input())
for j in list_of_numbers(a,b):
    print(j, end=",")