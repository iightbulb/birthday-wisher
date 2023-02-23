from dotenv import load_dotenv
import pandas
import smtplib
import datetime as dt
import os
import random


def configure():
    load_dotenv()


today = dt.datetime.now()
today = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day):row for (index, row) in data.iterrows()}

if today in birthday_dict:
    chosen_letter = random.choice(os.listdir("letter_templates"))
    with open(f"letter_templates/{chosen_letter}") as letter_file:
        contents = letter_file.read()
        letter = contents.replace("[NAME]", birthday_dict[today]["name"])
        print(letter)
        
    with smtplib.SMTP("smtp.gmail.com") as connection: #URL OF EMAIL SERVER
        connection.starttls()
        connection.login(os.getenv('my_email'), os.getenv('my_password'))
        connection.sendmail(
            from_addr=os.getenv('my_email'),
            # to_addrs=birthday_dict[today]["email"]
            to_addrs=os.getenv('my_email'),
            msg=f"Subject:Happy birthday!\n\n{letter}")





