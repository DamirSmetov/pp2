l = [1, 2, 3, 4, 5]

with open ("1.txt", "wt") as file:
    for i in l:
        file.write(str(i) + "\n")
    