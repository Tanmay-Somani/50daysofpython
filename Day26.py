def sort_words(x):
    letters = list(set(x.replace(" ", "")))
    letters.sort()
    string = ",".join(letters)
    str = []
    str.append(string)
    return str


x = "love life"
print(sort_words(x))
