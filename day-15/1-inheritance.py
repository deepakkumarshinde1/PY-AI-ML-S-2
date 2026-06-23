class Parent:
    pass

class Child(Parent):
    pass


# example-1
class Employee:
    name = "Deepak"

    def printDetails(self):
        print(f"Emp Name is {self.name}")

class Salary:
    
    def printSalaryDetails(self):
        print(f"The employee salary is 2000/-")

class Staff(Employee,Salary):
    branch = "Computer"
    pass


class Teacher(Staff):
    pass

class Hod(Staff):
    pass

class Subject(Staff):
    subjectName = "Maths"
    
    def subjectDetails(self,name,branch):
        print(f"{name} teach subject as {self.subjectName} of {branch}")


subject = Subject()
subject.printDetails()
print(subject.branch)
subject.subjectDetails(subject.name,subject.branch)
subject.printSalaryDetails()
