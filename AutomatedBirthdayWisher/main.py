import datetime as dt
import smtplib
import pandas
import random

MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_email_app_password"

now = dt.datetime.now()
today = (now.month, now.day)

birthdays = pandas.read_csv("birthdays.csv")

birthdays_dict = {(row.month, row.day): row for (index, row) in birthdays.iterrows()}


def read_letter(person_name):
    random_letter = random.randint(1, 3)
    with open(f"letter_templates/letter_{random_letter}.txt", mode="r") as data_file:
        data = data_file.read()
        letter_text = data.replace("[NAME]", person_name)
    return letter_text


def send_wish(email_to, letter_text):
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email_to,
            msg=f"Subject: Happy Birthday\n\n{letter_text}"
        )


if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    email = birthday_person["email"]
    name = birthday_person["name"]
    letter = read_letter(name)
    send_wish(email, letter)