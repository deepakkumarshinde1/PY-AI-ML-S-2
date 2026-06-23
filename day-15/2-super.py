# super
class Vehicle:
    def __init__(self,carName):
        self.name = carName
        
    def start(self):
        print(f"Twist Key to Right to Start")


class Car(Vehicle):
    def __init__(self,carName):
        super().__init__(carName)

    def start(self):
        super().start() # call to parent method
        print(f"Press button to start car {self.name}")

class Brand(Car):
    def __init__(self,brand,carName):
        self.brand = brand
        super().__init__(carName)

    def printCarName(self):
        print(f"Car name is {self.name}")


brand = Brand("Honda","Amaze")
brand.printCarName()