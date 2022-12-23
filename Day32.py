def password_validator():
    passw = input("Enter a password:")
    if len(passw) >= 8:
        if any(c.isupper() for c in passw):
            if any(c.islower() for c in passw):
                if any(c.isdigit() for c in passw):
                    print("You have a valid password!")
                else:
                    print("You need to have at least one digit")
            else:
                print("You need to have at least one small letter")
        else:
            print("You need to have at least one capital letter")
    else:
        print("You need to have at least 8 characters in your password")


password_validator()


def password_validatorex():
    a = True
    while a:
        EMPTY = " "
        passw = input("Enter a password:")
        if len(passw) <= 8:
            EMPTY += "You need to have at least 8 characters in your password"
        if any(c.isupper() for c in passw):
            if EMPTY == " ":
                EMPTY += "You need to have at least one digit"
                a = False
            else:
                EMPTY += " and at least one digit"
        if any(c.lower() for c in passw):
            if EMPTY == " ":
                EMPTY += "You need to have at least one lower alpabet"
            else:
                EMPTY += " and at least one lower alphabet"
                a = False
        if any(c.isdigit() for c in passw):
            if EMPTY == " ":
                EMPTY += "You need to have at least one capital alphabet"
            else:
                EMPTY += " and at least one capital alphabet"
                a = False

    print(EMPTY)


password_validatorex()
