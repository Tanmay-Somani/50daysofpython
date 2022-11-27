def convert_add(x):
    sum = 0
    for i in range(0, len(x)):
        sum += int(x[i])
    print(sum)


def check_duplicates(x):
    for i in x:
        if (i == x[1]):
            print(i)
        elif (x[0] != x[len(x)-1]):
            print("No Duplicates")


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
# asd = []
# print("Enter the no of elements in the list: ")
# n = int(input())
# for i in range(n):
#     print("Enter the elements: ")
#     asd.append(input())
# convert_add(asd)
check_duplicates(fruits)
check_duplicates(names)
