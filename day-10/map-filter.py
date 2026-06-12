numbers = [2,3,4,5,6,7,8,9,10]
# old way
sqNumber = []
def fun(numbers):
    global sqNumber
    for value in numbers:
        result = value*value
        sqNumber.append(result)
    
# fun(numbers)
# print(sqNumber)


# def conToSql(x):
#     return x*x

#new way
sqNumber2 = list(map(lambda x:x*x,numbers))
print(sqNumber2)

evenNumbers = list(filter( lambda x: x%2 ==0 ,numbers))
print(evenNumbers)

getGreaterNumber = list(filter( lambda x: x > 8 , numbers))
print(getGreaterNumber)


cities = ["Mumbai", "Pune", "Nashik", "Nagpur", "Aurangabad", "Kolhapur", "Solapur", "Amravati", "Jalgaon", "Satara"]

ucCity  = list(map(lambda city:city.upper() ,cities))
print(ucCity)

