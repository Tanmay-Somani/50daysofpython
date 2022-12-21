def create_user():
    name = input("Your name")
    age = input("Your age")
    password = input("Your password")
    dict = {"name": name, "Age": age, "Password": password}
    print("User saved. Please login")
    A = True
    while A:
        namel = input("Please enter your name")
        passwordl = input("Please enter your password")
        if namel == dict["name"] and passwordl == dict["Password"]:
            print("Logged in successfully")
            A = False
        else:
            print("Wrong password or user name. Please try again")


create_user()
