s = input()
s1 = reversed(list(s))
s2 = ""
for i in s1:
    s2 += i
if s2 == s:
    print("Yes")
else:
    print("No")
    
    