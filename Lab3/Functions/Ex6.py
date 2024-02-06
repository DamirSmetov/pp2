def find_common_elements(l1, l2):
    l3 = [x for x in l1 if x in l2]
    return l3
l1 = [4, 5, 6, 7]
l2 = [3, 5, 6, 7 , 8 ]
l = find_common_elements(l1, l2)
print (l)