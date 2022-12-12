def even_or_average():
    user = []
    max = 0
    sum = 0
    for i in range(5):
        user.append(int(input("Enter a number")))
        if max < user[i]:
            max = user[i]

    if user[0] % 2 != 0 or user[1] % 2 != 0 or user[2] % 2 != 0 or user[3] % 2 != 0 or user[4] % 2 != 0:
        avg = (user[0]+user[1]+user[2]+user[3]+user[4])/5
        return avg
    return max


print(even_or_average())
