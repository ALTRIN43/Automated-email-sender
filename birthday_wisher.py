from datetime import datetime
import pandas
import random
import smtplib

my_email = "example@example.com"  # Replace with your email
password = "yourpassword"  # Replace with your password

today = datetime.now() # give current date and time
today_md = (today.month, today.day)  # month and date

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_md in birthdays_dict:
    birthday_person = birthdays_dict[today_md]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email, # sender mail id
            to_addrs=birthday_person['email'], # receiver's mail id
            msg=f"Subject:Happy Birthday!!!\n\n{contents}"
        )

print("Message sent successfully") # prints success message if it's done
