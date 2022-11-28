names = ["Joseph", "Nathan", "Sasha", "Kelly",
         "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
ctr = 0
ctrs = 0
dict = {}
for i in names:
    if i == "Sera":
        ctr += 1
        dict[i] = ctr
    if i == "Sasha":
        ctrs += 1
        dict[i] = ctrs

print(dict)
