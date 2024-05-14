import smtplib
import random
import datetime as dt

MY_EMAIL = "your_email@gmail.com"
PASSWORD = "your_email_app_password"


def random_quote():
    with open("quotes.txt", mode="r") as quote_file:
        all_quotes = quote_file.readlines()
        r_quote = random.choice(all_quotes)
    return r_quote


def send_quote(quote_to_send):
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="any_email@gmail.com",
            msg=f"Subject: Every Monday Motivational Quote\n\n{quote_to_send}"
        )


now = dt.datetime.now()
# week_day = now.strftime("%A")
week_day = now.weekday()
print(week_day)

if week_day == 0:
    quote = random_quote()
    print(quote)
    send_quote(quote)
