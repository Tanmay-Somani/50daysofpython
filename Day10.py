def hide_password():
    passw = input()
    passw = "*"*len(passw)
    print(passw)
    print("the password is ", len(passw), "characters long")

passw = " "
hide_password()
