# inheritance syntax 
class Parent:
    pass

class Child(Parent):
    pass



# Single level inheritance
class Animal:
    def walking(self):
        print("animal is walking")


class Dog(Animal):
    def barking(self):
        print("dog is barking")

dog = Dog()
dog.walking()
dog.barking()


# multiple inheritance
class ParentOne:
    def printParentOne(self):
        print('printParentOne')

class ParentTwo:
    def printParentTwo(self):
        print('printParentTwo')

class Child(ParentOne,ParentTwo):
    def printChild(self):
        print('printChild')

c = Child()

c.printChild()
c.printParentOne()
c.printParentTwo()