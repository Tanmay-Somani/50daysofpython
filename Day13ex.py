def Python_snakes(num):
    n = ".."
    for i in range(1, num):
        j = i-1
        if (j == 0):
            print("."*i, "."*i)
        else:
            print(".", ".. "*j, ".")


Python_snakes(7)
