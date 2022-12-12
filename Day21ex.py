def even_or_average():
    user = []
    max = 0
    avg = 0
    for i in range(5):
        user.append(int(input("Enter a number")))
        if max < user[i]:
            max = user[i]
    for i in range(5):
        if user[i] % 2 != 0:
            avg = (user[0]+user[1]+user[2]+user[3]+user[4])/5
        else:
            return max
        return avg
    return max


print(even_or_average())
