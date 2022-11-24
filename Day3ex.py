names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
named = []
for i in names:
    if (i[0].islower()):
        named.append(i)
names.sort(reverse=True)
print(tuple(named))
