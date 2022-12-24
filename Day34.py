import csv
filename = "python.csv"


def just_digits():
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        print("Total no. of rows: %d" % (csvreader.line_num))
    print('Field names are:' + ', '.join(field for field in fields))


just_digits()
