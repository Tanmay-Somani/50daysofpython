def biggest_odd():
    max = 0
    user_in = input()
    user_in = [int(x) for x in str(user_in)]
    for i in user_in:
        if (i % 2 != 0):
            if (i > max):
                max = i
    return max


print(biggest_odd())
