def count_dots(strn):
    ctr = 0
    for i in strn:
        if (i == "."):
            ctr += 1
    return ctr


print(count_dots("s.d.f.fgg."))
print(count_dots("a.f.a.c.k."))
