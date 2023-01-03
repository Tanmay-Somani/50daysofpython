def words_with_vowels(liu):
    alep = []
    ale = liu.split(' ')
    for i in ale:
        if "a" in i or "e" in i or "i" in i or "u" in i or "o" in i:
            alep.append(i)
    print(alep)


alist = "You have No Rhytm"
words_with_vowels(alist)
