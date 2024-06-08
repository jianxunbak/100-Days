import requests
from datetime import datetime
import smtplib
import time
import os


gmail_email_server = "smtp.gmail.com"
to_address = "ta8549256@gmail.com"
MY_LAT = 1.352083
MY_LONG = 103.819839


def compare_coordinates():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def compare_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    current_hour = time_now.hour

    if sunrise > current_hour or current_hour > sunset:
        return True
    else:
        return False



while True:
    time.sleep(60)
    if compare_coordinates and compare_time:
        with smtplib.SMTP(gmail_email_server) as connection:
            connection.starttls()
            connection.login(os.environ.get("my_mail"), os.environ.get("password"))
            connection.sendmail(
                from_addr=os.environ.get("my_mail"),
                to_addrs=to_address,
                msg="ISS is overhead now!\n\nlook up now!!!"
            )
    else:
        print("iss not overhead yet")