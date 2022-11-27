def user_name():
    em_add = ''
    em_add = input("Enter your email address: ")
    if em_add.endswith("@gmail.com"):
        em_add = em_add.replace("@gmail.com", "")
        return em_add
    return "Invalid username"


print("The user name is", user_name())
