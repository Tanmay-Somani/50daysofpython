def Python_snakes(num):
    n = ".."
    for i in range(num):
        j = i-1
        if (j == 0):
            print(("."*i, "."*i).center(65))
        else:
            print(("."*i, ".."*j, "."*i).center(65))


Python_snakes(7)
