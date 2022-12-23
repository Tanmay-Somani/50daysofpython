import re


def email_validator(emails):
    valid_emails = []
    for email in emails:
        if email[0] == '@' or email.count('@') > 1:
            continue
        if not email.endswith('.com'):
            continue
        if re.match(r'[\w\.-]+@[\w\.-]+', email):
            valid_emails.append(email)
    if not valid_emails:
        return 'all emails are invalid'
    return valid_emails


emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
print(email_validator(emails))
