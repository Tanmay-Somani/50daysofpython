def indexed(string):
    list = []
    ctr = 1
    for i in string:
        if i.islower():
            list.append(ctr)
        ctr += 1
    return list


string = "TaNmAY"
print(indexed(string))
