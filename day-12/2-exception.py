def div():
    try: 
        a = int(input("Enter 1st Number = "))
        b = int(input("Enter 2nd Number = "))
        result = a/b
        print(f" {a} / {b} = {result}")
    except (ValueError,ZeroDivisionError):
        print("Invalid number passed. or Denominator is 0.")

# User defined and raise exception.
try:
    age = 17
    if(age < 18):
        raise ValueError("Age must be Greater than eighteen.")
    print("You are eligible for voting.")
except ValueError as error:
    print(error)


