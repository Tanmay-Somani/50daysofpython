def register_check(reg):
    c = 0
    for key in reg:
        if (reg[key] == 'yes'):
            c += 1
    return c


register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
print(register_check(register))
