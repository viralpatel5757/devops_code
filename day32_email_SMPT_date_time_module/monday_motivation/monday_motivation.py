import datetime as dt
import random
import smtplib

# read the quote file and make list out of it
with open("quotes.txt") as file:
    cont = file.read()
    cont_list = cont.split("\n")

# get today's date information
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    my_email = "crossrugs@gmail.com"
    password = "abc123"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="viralbusiness7@gmail.com",
            msg=f"Subject:Motivation quote\n\n{random.choice(cont_list)}"
        )


