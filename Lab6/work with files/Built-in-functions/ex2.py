c = 0
l = 0
def letters(s):
    global c
    global l
    if s.isupper() == True:
        c += 1
    else:
        l += 1
    return c, l
s = "aaAAAcx"
result = map(letters, s)
l2 = list(result)
print(f"Capital letters: {l2[-1][0]}, Lowercase letters: {l2[-1][1]}")
        