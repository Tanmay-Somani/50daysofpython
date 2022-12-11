str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success'


def Convert(str1):
    ex = []
    li = list(str1.split(" "))
    for i in li:
        for x in range(len(i)):
            if (i[x].isupper()):
                ex.append(i[::-1])

    return ex


print(Convert(str1))
