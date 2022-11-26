ctrm = 0
ctrf = 0
students = ['Male', 'Female', 'female', 'male', 'male', 'male',
            'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
for i in students:
    if i == "Male" or i == 'male':
        ctrm += 1
    elif i == 'Female' or i == 'female':
        ctrf += 1

M = ('Male', ctrm)
F = ('female', ctrf)

li = []
li.append(M)
li.append(F)
print(li)
