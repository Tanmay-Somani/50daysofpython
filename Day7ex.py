names = ["Joseph", "Nathan", "Sasha", "Kelly",
         "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
ctr_val = 0
dict = {}
for i in names:
    if i[0] == "S":
        alpha = i
        ctr_val += 1
        dict[alpha] = ctr_val
print(dict)
