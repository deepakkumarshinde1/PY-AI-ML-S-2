# 3-abstract-class
# Abstract Base Class 
from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start():
        pass

    def stop(self):
        print("stop")

class Car(Vehicle):
    
    def start(self):
        print("Start car")


class Bike(Vehicle):
    
    def start(self):
        print("Start bike")


car = Car()

car.start()
car.stop()