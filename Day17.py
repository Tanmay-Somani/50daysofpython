import random
alphar = random.randint(0, 9)


def user_name():
    user_n = input("Enter Your Name")
    username = user_n[::-1]
    username = username+str(alphar)
    return username


print(user_name())
