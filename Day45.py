import string


def analyse_string(stringx):
    special_characters = 0
    words = 0
    total_characters = 0
    for char in stringx:
        if char in stringx.punctuations:
            special_characters += 1
        if char in stringx.whitespace:
            words += 1
        total_characters += 1
    words -= 1
    return {
        "special character": special_characters,
        "words": words,
        "total characters": total_characters
    }


stringx = "Python has a string format operator %. This functions analogously to printf format strings in C, e.g. \"spam=%s eggs=%d\" % (\"blah\", 2) evaluates to \"spam=blah eggs=2\"."
print(analyse_string(string))
