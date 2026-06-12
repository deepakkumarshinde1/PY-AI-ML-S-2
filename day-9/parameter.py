def welcome():
    print("hello")


welcome() # hello

# function with para
def welcomeStudent(name):
    print(f"hello {name}")

welcomeStudent("om")
welcomeStudent("rani")

def add(a,b):
    print(f" The Addition of number a & b. is :: {a} + {b} = {a+b}")

add(10,20)


# default parameters
def sub(a = 0,b = 0):
    print(a-b)

sub()
sub(10,5)

# keyword arguments
def studentDetails(name,age):
    print(f"student name is {name} and age in {age}")

studentDetails(age="36",name="Deepakkumar")

# * => tuple
# variable length args
def getData(*l):
    l = list(l)
    print(l)

getData(1,"deepak",36,46)

# ** => dict
# keyword variable length args
def getMoreData(**l):
    print(l)

getMoreData(name="deepak",roll_no=1,age=36,marks=46)
# {'name': 'deepak', 'roll_no': 1, 'age': 36, 'marks': 46}