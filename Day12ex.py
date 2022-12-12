from datetime import date


def age_in_minutes():
    year = input("Enter your year of birth")
    xyear = int(year)
    while (len(year) == 4 and xyear < 1900):
        today = date.today()
        tyear = today.year
        cur_age = abs(xyear-tyear)
        print(cur_age)
        return 0
    print("you have entered an invalid number enter again")
    age_in_minutes()


age_in_minutes()
