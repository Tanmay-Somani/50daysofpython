# Creating a simple calculator app with python
def add(x, y):
    try:
        return x+y
    except:
        return "Invalid Argument Entered,Please enter again"


def subtract(x, y):
    try:
        return x-y
    except:
        return "Invalid Argument Entered,Please enter again"


def divide(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "cannot divide by zero"
    except NameError or ValueError:
        return "Invalid Argument Entered,Please enter again"


def multiply(x, y):
    try:
        return x*y
    except:
        return "Invalid Argument Entered,Please enter again"


print("Calculator")
a = input("Enter what function you wanna perform - 1|ADD| 2|SUB| 3|MUL| 4|DIV|")
x = input("Enter the first digit")
y = input("Enter the second digit")
if a == 1:
    add(x, y)
elif a == 2:
    subtract(x, y)
elif a == 3:
    multiply(x, y)
else:
    divide(x, y)
