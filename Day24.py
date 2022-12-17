def average_calories(*cal):
    avg = sum(cal)/len(cal)
    return avg


print(average_calories(12, 3, 34, 4, 3))
