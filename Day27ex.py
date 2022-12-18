
def difference(a, b):
    return [x for x in a if x not in b] + [x for x in b if x not in a]


list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
print(difference(list1, list2))
