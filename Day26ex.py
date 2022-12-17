def string_length(string):
    words = string.split()
    lengths = {}
    for word in words:
        lengths[word] = len(word)
    return lengths


string = "Hi my name is Richard"
print(string_length(string))
