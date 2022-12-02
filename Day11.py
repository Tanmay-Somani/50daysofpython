def equal_strings(str1, str2):
    if len(str1) == len(str2):
        for i in range(0, len(str1)):
            if str1[0] == str2[i]:
                for i in range(0, len(str1)):
                    if str1[1] == str2[i]:
                        for i in range(0, len(str1)):
                            if str1[2] == str2[i]:
                                for i in range(0, len(str1)):
                                    if str1[3] == str2[i]:
                                        print("True")
    else:
        print("False")


str1 = "love"
str2 = "evol"
equal_strings(str1, str2)
