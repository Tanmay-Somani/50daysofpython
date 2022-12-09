def sum_list(listx):
    nest_lx = []
    sum = 0
    for i in range(len(listx)):
        popped = listx.pop()
        nest_lx.extend(popped)
    for i in range(len(nest_lx)):
        sum += nest_lx[i]
    return sum


listx = [[2, 4, 5, 6], [6], [5, 4, 5, 6, 7]]
print(sum_list(listx))
