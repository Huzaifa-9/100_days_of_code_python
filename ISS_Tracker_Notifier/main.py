import requests
import datetime as dt
import smtplib
import time

MY_EMAIL = "Youremail@gmail.com"
MY_EMAIL_APP_PASSWORD = "Your_EMAIL_APP_PASSWORD"

ISS_POSITION_API_URL = "http://api.open-notify.org/iss-now.json"
SUNSET_API_URL = "https://api.sunrise-sunset.org/json"

MY_LAT = 24.860735
MY_LONG = 67.001137


def is_iss_overhead():
    response = requests.get(url=ISS_POSITION_API_URL)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5  and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url=SUNSET_API_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
    time_now = dt.datetime.now().hour
    sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP(host="smtp.gmail.com",port=587)as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_EMAIL_APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="your_email@gmail.com",
                msg=f"Subject:👆International Space Station Current Location\n\nlook Up 👆👆👆👆👆 The ISS is above you"
            )

