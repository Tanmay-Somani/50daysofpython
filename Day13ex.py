def Python_snakes(num):

    for i in range(1, num):
        j = i-1
        a = "."*i
        b = ".. "*j
        if (j == 0):
            print(a, a)
        else:
            print(".", b, ".")


Python_snakes(7)
