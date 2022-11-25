def only_floats(a, b):
    if (type(a) == float and type(b) == float):
        return 2
    elif (type(a) != float and type(b) != float):
        return 0
    else:
        return 1


print(only_floats(12.1, 23))
