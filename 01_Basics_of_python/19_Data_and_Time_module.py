""" Here we will learn about the datatime module """
import datetime

"""
Datetime : Here we will learn about the datetime.
"""

# Today date and time
present_time = datetime.datetime.now()
print(f"Present time along with the current time : {present_time}")

# Today date
today_date = datetime.date.today()
print(f"Today date : {today_date}")

# Create a specific date
create_date_and_time = datetime.datetime(2024, 2, 14, 11, 30, 25)
print(f"Created date : {create_date_and_time}")

# Specific date and time
now = datetime.datetime.now()
print(f"Year : {now.year}")
print(f"Month : {now.month}")
print(f"Day : {now.day}")
print(f"Hour : {now.hour}")
print(f"Minute : {now.minute}")
print(f"Second : {now.second}")

# formatted date
now = datetime.datetime.now()
formatted_time = now.strftime("%Y - %m - %d %H : %M : %S")
print(f"Formatted date : {formatted_time}")

# anthor formatted date
print(f"Formated date : {now.strftime("%A : %d : %B : %Y")}")


