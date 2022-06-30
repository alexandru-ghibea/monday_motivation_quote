import datetime
import random
import getpass
import smtplib
today = datetime.datetime.now()
year = today.year
day_of_week = today.weekday()
if day_of_week == 0:
    with open("quotes.txt") as file:
        read = file.readlines()
        random_quote = random.choice(read)
    email = "your email"
    #get your password from password for apps inside gmail/yahoo account security settings
    password_email = getpass.getpass("Password: ")
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        #secures connection
        connection.starttls()
        connection.login(user=email, password=password_email)
        subject = "Monday Motivation"
        message = random_quote
        email_body = "Subject: " + subject + '\n' + message
        connection.sendmail(from_addr=email, to_addrs=email, msg=email_body)
