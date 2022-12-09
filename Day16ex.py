Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
nest_lx = []


def unpack_list(Nested_list):
    #ctr = 0
    # for i in Nested_list:
    # if i[ctr] == i[0]:
    # nest_lx.remove(i[ctr])
    #ctr += 1
    for i in range(len(Nested_list)):
        popped = Nested_list.pop()
        nest_lx.extend(popped)
    return nest_lx


print(unpack_list(Nested_list))
