def filter_prime(l1):
    result = []
    for i in l1:
        divisors = 0
        for j in range(1, i+1):
            if i % j == 0:
                divisors += 1
        if divisors ==2:
            result.append(i)
    return result
    
l  = [1, 3, 5, 2, 7, 8, 11]
print(filter_prime(l))