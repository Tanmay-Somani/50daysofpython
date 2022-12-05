def your_salary():
    num_pe = 0
    teach_name = input("Enter the teachers name")
    num_per = int(input("Number of period"))
    rate = int(input("Enter the rate per period"))
    if (num_per > 100):
        num_pe = 100-rate
    print("Teacher:", teach_name)
    print("Periods:", num_per)
    print("Gross  Salary:", num_per*rate+num_pe*(rate+5))


your_salary()
