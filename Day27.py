def unique_numbers(u):
    v = u
    u = abs(sum(set(u))-sum(v))
    if u % 2 == 0:
        return v
    else:
        return list(set(v))


u = [1, 12, 4, 5, 6, 7, 1, 8, 4]
x = [1, 2, 4, 5, 6, 7, 8, 8]
print(unique_numbers(u))
print(unique_numbers(x))
