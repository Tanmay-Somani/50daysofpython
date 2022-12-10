def count_words(sstrin):
    wrd_cnt = 0
    for i in sstrin:
        if i == ' ' or i == '.' or i == "/n":
            wrd_cnt += 1
    return wrd_cnt


def count_elements(sstrin):
    ele_cnt = 0
    for i in sstrin:
        if i != ' ':
            ele_cnt += 1
    return ele_cnt


sstrin = "I1 could2 be3 a4 better5 boyfriend6 than7 him8.I9 could10 do11 the12 things13 he14 never15 did16.I17 could18 be19 such20 a21 gentlemen22 than23 him24."
sstring = "I love learning."
print(count_words(sstrin))
print(count_elements(sstrin))
