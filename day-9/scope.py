# local / global

# local
def sum():
    x = 10
    y = 20
    print(x+y)

sum()

# global
z = 10
def printData():
    global z 
    z = 20
    print(z)


printData()
print(z)