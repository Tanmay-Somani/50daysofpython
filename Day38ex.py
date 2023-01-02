def missing_items(list):
    ctr = 1
    listx = []
    one = list[0]
    end = list[len(list)-1]
    for i in range(1, end):
        if i == list[ctr]:
            ctr += 1
        else:
            listx.append(ctr)
            ctr += 1
    return listx


list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,
        18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]

print(missing_items(list))
