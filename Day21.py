
def make_tuples(a, b):
    x = []
    for i in range(len(a)):
        p = a.pop(i)
        q = b.pop(i)
        a.insert(0, 0)
        b.insert(0, 0)
        y = (p, q)
        x.append(y)
    return x


a = [1, 2, 3, 4, ]
b = [5, 6, 7, 8]
print(make_tuples(a, b))
