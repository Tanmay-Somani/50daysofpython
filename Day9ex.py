def zeroes_last(list):
    list.sort()
    for i in list:
        if i == 0:
            list.append(i)
            list.pop(0)
    print(list)


list = [21, 0, 42, 33, 0, 0, 0, 5, 32, 40, 0, 60, 8, 0, 45, 32]
zeroes_last(list)
