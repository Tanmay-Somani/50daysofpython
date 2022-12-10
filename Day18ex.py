def add_reverse(l1, l2):
    if len(l1) == len(l2):
        l3 = l2
        for i in range(len(l1)):
            l3[i] = l1[i]+l2[i]
        l3 = l3[::-1]
        return l3
    else:
        return "The lists are of different lengths"


l1 = [10, 12, 34]
l2 = [12, 56, 78]
print(add_reverse(l1, l2))
