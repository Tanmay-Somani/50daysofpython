# names = ["Peter", "Beezelbub", "Jon", "Andrew"]


# def sort_length(names):
#     lenli = len(names)
#     max = 0
#     for i in range(0, lenli):
#         ind = len(names[i])
#         if (int(ind) > max):
#             max = names[i]
#             max = len(max)
#             temp = names[i]
#     return temp


# print(sort_length(names))
names = ["Peter", "Beezelbub", "Jon", "Andrew"]


def sort_length(names):
    lenli = len(names)
    for i in range(lenli):
        ind = len(names[i])
        indi = len(names[i+1])
        if (indi < ind):
            temp = names[i]
            names[i] = names[i+1]
            names[i+1] = temp

    return names


print(sort_length(names))
