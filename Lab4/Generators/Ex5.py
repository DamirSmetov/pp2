def list_of_numbers(n):
    for i in range(n, -1, -1):
            yield i
n = int(input())
for j in list_of_numbers(n):
    print(j, end=",")