def middle_figure(a, b):
    c = a+b
    r = int(len(c)/2)
    return c[r: r+1: 1]


a = "make love"
b = "not war"
print(middle_figure(a, b))
