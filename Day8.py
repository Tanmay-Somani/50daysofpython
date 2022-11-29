def odd_even(list):
    max_ev = 0
    min_odd = 1
    for i in list:

        if (i % 2 == 0):
            if (max_ev <= i):
                max_ev = i
        else:
            if (min_odd > i):
                min_odd = i
    return max_ev-min_odd


lisz = [3, 2, 4, 1, 6, 12]
print(odd_even(lisz))
