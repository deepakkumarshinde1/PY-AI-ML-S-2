class Teacher:
    name = "Deepak" #public
    _age = 36 #protected
    __salary = 20000 #private

    def set_salary(self,value):
        self.__salary  = value

    salary = property(fset=set_salary) # set setter

t = Teacher()
print(t.name)
print(t._age)
t.salary = 22000
# print(t.salary)
