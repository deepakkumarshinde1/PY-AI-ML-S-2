
# file handling exception
try:
    file = open('user.log',"r")
except FileNotFoundError:
    print("File not found")


try:
    print(1/0)
    # risk code
except ZeroDivisionError:
    print("Denominator number is 0.")
    # issue output
    # handling issue



print("Hello")


# ZeroDivisionException => Divide by 0.
# ValueError => Invalid value 
# TypeError => Wrong data type
# IndexError => So if the index is not available or invalid.
# KeyError => Your dictionary does not have that key.
# NameError => If your value is not defined.
# FileNotFoundError => If you try to read a file, but it's not available.
# AttributeError => Invalid object structure.