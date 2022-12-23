def inter_section(l1, l2):
    l3 = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                l3.append(l2[j])
    return tuple(l3)


list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]
print(inter_section(list1, list2))
