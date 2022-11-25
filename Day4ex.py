
def word_index(list):
    for i in list:
        max = 0
        ctr = 0
        a = list[0]
        if (len(i) > max):
            max = 2
        if (len(list[0]) == len(i)):
            ctr += 1
    if (ctr == 1):
        return 0
    return max


list = ["hello", "world", "its a", "world"]
ast = ["love", "hate"]
print(word_index(list))
print(word_index(ast))
