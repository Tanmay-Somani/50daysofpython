def zeroed(listn):
    listn[0] = 0
    listn[-1] = 0
    return listn


def zerolistmaker(q):
    ni = []
    for i in range(q):
        ni.append([0])
    print(ni)


listn = [2, 5, 7, 8, 9]
n = int(input())
print(zeroed(listn))
zerolistmaker(n)
