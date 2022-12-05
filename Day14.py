def flat_list(nest_l):
    for i in nest_l:
        popped = nest_l.pop()
        nest_lx = popped
        return popped


nest_l = [[2, 4, 5, 6]]
print(flat_list(nest_l))
