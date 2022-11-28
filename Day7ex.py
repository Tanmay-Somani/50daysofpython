names = ["Joseph", "Nathan", "Sasha", "Kelly",
         "Muhammad", "Jabulani", "Sera", "Patel", "Sera", "Sera", "Sasha"]
ctr_val = 0
dict = {}
for i in names:
    if i[0] == "S":
        if i in dict:
            dict[i] = ctr_val
            ctr_val += 1
        dict[i] = ctr_val+1
print(dict)
