def largest_number(case):
    stri = ""
    for i in case:
        stri += str(i)
    dig = [int(d) for d in stri]
    stri = ""
    dig.sort(reverse=True)
    for i in dig:
        stri += str(i)
    return stri


case = [3, 67, 817, 9, 62, 0, 23]
print(largest_number(case))
