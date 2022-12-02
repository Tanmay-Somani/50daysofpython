def convert_numbers(list):
    a = []
    for i in list:
        list = '{:,}'.format(i)
        a.append(list)
    return a


list = [100, 23989, 52354672, 9878098, 9074, 9087872]

print(convert_numbers(list))
