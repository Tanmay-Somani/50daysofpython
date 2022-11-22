def divide_or_square(n):
    if (n/5):
        return n**0.5
    else:
        return n//5


def longest_value(x):
    a = max(x.values())
    return a


n = int(input())

print(divide_or_square(n))
x = {'wind': 'grey', 'fire': 'red', 'water': 'blue', 'earthen': 'brown'}
print(longest_value(x))
