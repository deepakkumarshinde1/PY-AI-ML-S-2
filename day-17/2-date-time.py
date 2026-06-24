from datetime import datetime,date 

# modules
# datetime
# date
# time
# timedelta

# yyyy-mm-dd H:M:S.microsec
now = datetime.now() # 2026-06-24 15:10:20.652688
today = date.today() # 2026-06-24
todaysTime = now.time() # 15:13:09.262496
print(todaysTime)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.timestamp())


