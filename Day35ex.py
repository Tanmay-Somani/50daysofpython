def find_index(find_n, listx):
    empt_list = []
    if find_n in listx:
        for i in range(len(listx)):
            if find_n == listx[i]:
                empt_list.append(i)
        print(empt_list)
    else:
        for i in range(len(listx)):
            listx[i] = find_n
        print(listx)


listx = [1, 7, 8, 1, 2, 4, 6, 7, 4, 2, 4, 6, 4]
find_index(1, listx)
find_index(5, listx)
