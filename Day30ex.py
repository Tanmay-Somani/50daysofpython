
names = ["Beyonce Knowles", "Alicia Keys",
         "Katie Perry", "Chris Brown", "Tom Cruise"]
for i in range(len(names)):
    a = names[i].split(" ")
    z = a[1] + " " + a[0]
    names.append(z)
    names.pop(0)
print(names)
