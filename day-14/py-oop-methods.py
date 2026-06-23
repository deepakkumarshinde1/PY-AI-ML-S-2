class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printData(self):
        print(self.name,self.price)

    
product = Product("Lenovo", 12000)
# product.printData()

class Math:
    pi = 3.14
    
    @classmethod
    def areaOfCircle(cls,radius):
        return cls.pi* (radius*radius)
    
result = Math.areaOfCircle(20)
print(f"area or circle is {result}")



class Calc:

    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def sub(a,b):
        return a-b
    
    @staticmethod
    def div(a,b):
        return a/b
    

print(Calc.add(10,20))
print(Calc.sub(10,20))
print(Calc.div(10,20))