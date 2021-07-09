import smtplib
import datetime as dt
import random

time_msg = dt.datetime.now()
today = time_msg.weekday()
date = time_msg.time
my_mail = "Enter ur email acc"
password = "password"
#Email txt converted to dictionary using dict comprehension
d = {line.split()[0]: line.split()[1] for line in open("email.txt")}
#Names txt converted to dictionary using dict comprehension
names = {line.split()[0]: line.split()[1] for line in open("names.txt")}

numb = len(d) + 1
count = 1
while True:

    if count < numb:
        with open("quotes.txt") as qt:
            all_qt = qt.readlines()
            quote = random.choice(all_qt)
        user_name = names[f"{count}"]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() #to secure the connection
            connection.login(user= my_mail, password = password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs=d[f"{count}"],
                                msg= f"subject: [give subject here] {user_name} \n\n"
                                     f" [Body- Enter texts] {quote} ")
        count += 1
    else:
        exit()
