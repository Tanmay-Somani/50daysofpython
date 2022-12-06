def your_age():
    dict = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
    ctr = 0
    ctrx = 0
    user_name = input("Enter your name")
    for i in dict:
        if i == user_name:
            ctr += 1
        else:
            ctrx += 1
    if (ctr == 1):
        print("Hi", user_name, "your age is", dict[user_name])
    elif (ctrx == 4):
        print("You are not in the database")


your_age()
