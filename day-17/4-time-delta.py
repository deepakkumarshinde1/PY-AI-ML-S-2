# Add a date
from datetime import datetime,timedelta

now = datetime.now()

nextDate = now + timedelta(days=28);

print(nextDate)


preDate = now - timedelta(days=28);

print(preDate)


examDate = now + timedelta(days=15)

print(f"exam date is {examDate.strftime("%d-%m-%Y")}")


# Example -1 get days

date1 = datetime(2026,6,24)
date2 = datetime(2026,7,17)

date3 = date2 - date1
print(date3.days)


# Example 2 check age
dob = datetime(2008,8,25)
today = datetime.now()

age = today.year - dob.year
print(age)