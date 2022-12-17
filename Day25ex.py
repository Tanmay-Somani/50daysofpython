str1 = "the love is real"


def read_backwards(str1):
    words = str1.split()
    words.reverse()
    return " ".join(words)


print(read_backwards(str1))
