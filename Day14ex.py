def your_salary():
    num_pe = num_per
    teach_name = input("Enter the teachers name")
    num_per = int(input("Number of period"))
    rate = int(input("Enter the rate per period"))
    if (num_per > 100):
        num_pe = num_per
        num_per = 100-num_per
    print("Teacher:", teach_name)
    print("Periods:", num_pe)
    print("Gross  Salary:", num_pe*rate+(num_per*(rate+5)))


your_salary()
