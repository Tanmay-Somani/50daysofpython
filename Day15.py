def same_as_reverse(string):
    for i in range(0, int(len(string)/2)):
        if string[i].upper() != string[len(string)-i-1].upper():
            return False
    return True


string = "SDAdadads"
print(same_as_reverse(string))
