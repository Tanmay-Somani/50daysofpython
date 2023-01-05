def student_marks():
    dictx = {}
    a = True
    while a:
        a = input("Enter if you wish for no more")
        student_name = input("Enter the student name")
        student_marks = input("Enter the student marks")
        dictx[student_name] = student_marks
    print(dictx)


student_marks()
