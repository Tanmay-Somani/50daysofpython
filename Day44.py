import csv


def save_emails():
    with open('emails.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        print("Enter email addresses (enter 'done' when finished):")
        emails = []
        while True:
            email = input()
            if email == 'done':
                break

            emails.append(email)
        writer.writerows(emails)


save_emails()


def open_emails():
    with open('emails.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        for email in reader:
            print(email)


open_emails()
