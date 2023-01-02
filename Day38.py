import random


def guess_a_number(x):
    while x:
        y = int(input("Enter your guess"))
        if y > x:
            print("Too high, Aim lower")
        elif y < x:
            print("Too low, Aim higher")
        else:
            print("Yess, you guessed it correctly , the correct number was", y)
            break


x = random.randint(0, 30)
guess_a_number(x)
