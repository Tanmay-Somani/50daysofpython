def multiply_words(string):
    ctr = 0
    mul = 1
    for i in string:
        if i != " ":
            ctr += 1
        if i == " ":
            mul *= ctr
            ctr = 0
    return mul


string = "love live and laugh "
print(multiply_words(string))
