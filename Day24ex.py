def nested_lists(lists):
    listm = []
    for i in list(lists):
        listm.append(i)
    return listm


lists = [1, 2, 3, 5], [1, 2, 3,
                       4], [1, 3, 4, 5]

print(nested_lists(lists))
