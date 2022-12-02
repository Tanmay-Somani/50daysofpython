def swap_values(list):
    repl = list[0]
    inss = list[len(list)-1]
    list.remove(repl)
    list.remove(inss)
    list.append(repl)
    list.insert(0, inss)
    return list


list = [2, 4, 67, 6]
listx = [1, 2, 3, 4]
listv = [9, 3, 3, 3, 3, 3, 3, 6]
print(swap_values(list))
print(swap_values(listx))
print(swap_values(listv))
