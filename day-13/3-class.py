class Student:

    name = ""
    def __init__(self,sName):
        self.name = sName

    def printData(self):
        print(self.name)


student = Student("Dipali")
student.printData()

student1 = Student("Rupesh")
student1.printData()
