# varName = lambda v1,v2,v3:logic

# def add(a,b):
#     return a+b

add = lambda a,b:a+b
print(add(30,10))
print(add(10,10))


# def evenOdd(n):
#     if( n % 2 ==0):
#         return "even"
#     else:
#         return "odd"
    
evenOdd = lambda n: "even" if n%2==0 else "odd"
# return even if n mod 2 is equals to zero, else return odd


def addNumber1(a,b,c):
    return a+b+c

addNumber2 = lambda a,b,c:a+b+c


def findLarge(a,b):
    if a > b:
        return a
    else:
        return b
    

findLarge1 = lambda a,b: a if a > b else b