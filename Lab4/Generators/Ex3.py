def list_of_numbers(n):
    for i in range(0, n+1):
        if i % 3  == 0 and i%4 == 0:
            yield i
n = int(input())
for j in list_of_numbers(n):
    print(j, end=",")