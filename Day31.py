def longest_word(x):
    max = 0
    fix = " "
    dict = []
    for i in range(len(x)):
        if len(x[i]) > max:
            max = len(x[i])
            fix = x[i]
    dict.append(max)
    dict.append(fix)
    return dict


x = ["Java", "JavaScript", "Python"]
print(longest_word(x))
