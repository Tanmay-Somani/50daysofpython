def all_the_same(x):
    ctr = 0
    for i in range(0, len(x)):
        if x[i] == x[i+1]:
            ctr += 1
            if ctr == len(x)-1:
                return True
        else:
            return False


x = ["Mary", "Mary", "Mary", "Mary", "Mary"]
print(all_the_same(x))
