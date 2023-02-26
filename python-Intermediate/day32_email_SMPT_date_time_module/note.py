# automated birthday wisher
# email SMPT is an inbuilt module which helps us in sending emails using python code
# datetime module helps us with formatting date and time and many more things.
# create a new email and lower the security of that account (allow access to less secure apps + no two-step verification)
#------------------------------------------------------------------------------------------------------------------
import smtplib

my_email = "crossrugs@gmail.com"
password = "abc123"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="viralbusiness7@gmail.com",
        msg="Subject:hello\n\nThis is the body of my email"
    )
# ------------------------------------------------------------------------------------------------------------------
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month

print(now)
print(year)

date_of_birth = dt.datetime(year=1995, month=4, day=30)
print(date_of_birth)
























