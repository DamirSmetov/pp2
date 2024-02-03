#Functions
#Ex1

def calculate_factorial(n):
    if n == 1:
        return 1
    return n * calculate_factorial(n-1)
a = int(input())
print(calculate_factorial(a))
#Ex2

def reverse_string (s):
    print(s[::-1])
s = input()
reverse_string(s)

#Ex3
def get_max(a, b, c):
    print(max(a, b, c))
b = int(input())
c = int(input())
d = int(input())
get_max(b, c, d)
#Ex4
def is_even(n):
    if n % 2 == 0:
        print ("True")
    else:
        print ("False")
number = int(input())
is_even(number)

#Ex5 

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

#Ex6
def find_common_elements(l1, l2):
    l3 = [x for x in l1 if x in l2]
    return l3
l1 = [4, 5, 6, 7]
l2 = [3, 5, 6, 7 , 8 ]
l = find_common_elements(l1, l2)
print (l)

#Ex7

def word_frequency(s):
    l = s.split()
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)
s = input()
word_frequency(s)


#Ex8
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1 
    return fibonacci(n-1) + fibonacci(n-2)
n = int(input())
print (fibonacci(n))

#Ex9
def calculate_running_average(*n):
    l = []
    average = 0
    for i in range(1, len(n)+1):
        average = 0
        for j in range(i):
            average += n[j]
        average = average/i
        l.append(average)
    return l

print(calculate_running_average(10, 20, 30, 40, 50))

    
    
    