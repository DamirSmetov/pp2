def squares_of_numbers(n):
    i = 1
    while i**2<n:
        yield i**2
        i+=1
        
        
n = int(input())
for j in squares_of_numbers(n):
    print(j)
    