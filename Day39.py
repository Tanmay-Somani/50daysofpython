import random
import string


def generate_password():
    type = input("What is the level of security you want")

    if type == "weak":
        for i in range(5):
            All = random.choice(string.printable)
            print(All, end="")
    elif type == "medium":
        for i in range(8):
            All = random.choice(string.printable)
            print(All, end="")
    elif type == "strong":
        for i in range(12):
            All = random.choice(string.printable)
            print(All, end="")


generate_password()
