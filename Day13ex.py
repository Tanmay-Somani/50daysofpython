def Python_snakes(num):
    n = num
    a = "."
    ctr = 1
    print(" "*(n+1), a, " ", a)
    if (num % 2 == 0):
        for i in range(num):
            for j in range(int((i)/2)):
                print(" "*n, ".", " .. "*ctr, ".")
                ctr += 1
                n -= 1
    else:
        for i in range(num):
            for j in range(int((i+1)/2)):
                print(" "*(n), ".", ".. "*ctr, ".")
                ctr += 1
                n -= 1


Python_snakes(4)
Python_snakes(5)
