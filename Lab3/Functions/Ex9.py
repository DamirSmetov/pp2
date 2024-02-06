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