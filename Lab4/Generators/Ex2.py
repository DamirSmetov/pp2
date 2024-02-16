def list_of_numbers(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i
n = int(input())
for j in list_of_numbers(n):
    print(j, end=",")