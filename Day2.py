def convert_add(x):
    sum = 0
    for i in range(0, len(x)):
        sum += int(x[i])
    print(sum)


def check_duplicates(x):
    for i in range(0, len(x)):
        if (x[0] == x[i]):
            print(x[i])
            return x[i]
        else:
            print("No duplicates")
            return "No duplicates"


asd = []
print("Enter the no of elements in the list: ")
n = int(input())
for i in range(n):
    print("Enter the elements: ")
    asd.append(input())
convert_add(asd)
check_duplicates(asd)
