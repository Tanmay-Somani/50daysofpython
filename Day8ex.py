def prime_numbers():
    list = [2]
    stop = int(input("Insert the range of the integer"))
    for i in range(2, stop):
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                if i in list:
                    break   
                else:
                    list.append(i)
    return list


print(prime_numbers())
