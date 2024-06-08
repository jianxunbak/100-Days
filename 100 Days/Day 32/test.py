# import smtplib
#
# my_email = "ta8549256@gmail.com"
# password = "gtsyvyxfrnuzqezu"
# to_address = "test.account195@yahoo.com"
# gmail_email_server = "smtp.gmail.com"
# yahoo_email_server = "smtp.mail.yahoo.com"
#
# with smtplib.SMTP(gmail_email_server) as connection:  # this code connects to mail server
#     connection.starttls()  # this code makes connection secure
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=to_address,
#                         msg="subject:Hello\n\nhi"
#                         )
# now = dt.datetime.now()   # gives the current date and time
# year = now.year
# month = now.month
# time = now.time()
# day_of_week = now.weekday()
# date_of_birth = dt.datetime(year=1988, month=4, day=24)
# print(date_of_birth)


import datetime as dt
import smtplib
from random import choice

# --- OBTAIN CURRENT DAY OF WEEK --- #
now = dt.datetime.now()
day_of_week = now.weekday()

# --- GENERATE RANDOM QUOTES --- #
if day_of_week == 0:
    with open("quotes.txt") as file:
        quotes_list = file.readlines()
        random_quotes = choice(quotes_list)

# --- EMAIL QUOTE --- #
    my_email = "ta8549256@gmail.com"
    password = "gtsyvyxfrnuzqezu"
    to_address = "test.account195@yahoo.com"
    gmail_email_server = "smtp.gmail.com"

    with smtplib.SMTP(gmail_email_server) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=f"subject:Quote of the day\n\n{random_quotes}"
        )
