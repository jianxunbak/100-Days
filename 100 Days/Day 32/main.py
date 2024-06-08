import pandas
import datetime as dt
from random import choice, randint
import smtplib
import os

data = pandas.read_csv("./birthday-wisher-extrahard-start/birthdays.csv")
details = data.to_dict("records")
gmail_email_server = "smtp.gmail.com"

today_info = dt.datetime.now()
current_day = today_info.day
current_month = today_info.month

for items in details:
    if items["month"] == current_month and items["day"] == current_day:
        letter_num = randint(1, 3)
        with open(f"./birthday-wisher-extrahard-start/letter_templates/letter_{letter_num}.txt", "r") as letter:
            letter_a = letter.read()
            formatted_letter = letter_a.replace("[NAME]", items["name"])
        with smtplib.SMTP(gmail_email_server) as connection:
            connection.starttls()
            connection.login(user=os.environ.get("my_email"), password=os.environ.get("password")
                             )
            connection.sendmail(
                from_addr=os.environ.get("my_email"),
                to_addrs=items["email"],
                msg=f"subject:Happy Birthday!\n\n{formatted_letter}"
            )
