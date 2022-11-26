
def word_index(list):
    ctr = 0
    max = list[0]
    for i in list:
        if (len(i) > len(max)):
            max = i
        elif (len(i) == len(max)):
            ctr += 1
        if (ctr == len(list)):
            return 0
    return list.index(max)


list = ["hello", "world", "its mya", "world"]
words2 = ["Love", "Hate"]
print("the index is", word_index(list))
print(word_index(words2))
