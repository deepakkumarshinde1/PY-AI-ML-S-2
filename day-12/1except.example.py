def div():
    try: 
        a = int(input("Enter 1st Number = "))
        b = int(input("Enter 2nd Number = "))
        result = a/b
        print(f" {a} / {b} = {result}")
    except ValueError:
        print("Invalid number passed.")
    except ZeroDivisionError:
        print("denominator is 0.")


def listHandling():
    try:
        numbers = [1,2,3,4,5]
        print(numbers[5])
    except IndexError:
        print(f"Invalid index passed, last index must be {len(numbers)-1}")

def DictionaryHandling():
    try:
        student = {
            "name":"Deepak"
        }
        print(student['rollNo'])
    except KeyError:
        print("Invalid key passed")

# else in exception
try:
    result = 10/5
except ZeroDivisionError:
    print("Denominator is 0.")
else:
    print(result)

# Finally
try:
    result = 10/5
except ZeroDivisionError:
    print("Denominator is 0.")
finally:
    print("This will run always")


# else and finally
try:
    result = 10/5
except ZeroDivisionError:
    print("Denominator is 0.")
else:
    print(result)
finally:
    print("This will run always")