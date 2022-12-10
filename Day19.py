def count_words(sstrin):
    wrd_cnt = 0
    for i in sstrin:
        if i == ' ' or i == '.':
            wrd_cnt += 1
    return wrd_cnt


sstrin = "I1 could2 be3 a4 better5 boyfriend6 than7 him8.I9 could10 do11 the12 things13 he14 never15 did16.I17 could18 be19 such20 a21 gentlemen22 than23 him24."
print(count_words(sstrin))
