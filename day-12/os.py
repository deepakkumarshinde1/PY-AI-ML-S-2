import os

# check File exists.
isFileAvailable = os.path.exists('student.log')

if isFileAvailable == True:
    os.rename('student.log','user.log')


if os.path.exists('user.log'):
    os.remove('user.log')