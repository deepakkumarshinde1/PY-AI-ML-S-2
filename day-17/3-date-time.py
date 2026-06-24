# formatting
from datetime import datetime,date,time

now = datetime.now()
_date = now.strftime("%I")
print(_date)

#  %d => date
#  %m => month
#  %Y => FullYear
#  %y => Shot year
#  %H => Hr (24)
#  %I => Hr (12)
#  %M => Min
#  %S => Sec
# %A = Day
# %B = Month Name

# custom
_date = date(2026,1,26)
print(_date)
_time = time(13,30,30)
print(_time.strftime("%I:%M:%S"))
datetime(2026,1,26,13,30,30)