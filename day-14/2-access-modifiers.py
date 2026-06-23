class Teacher:
    name = "Deepak" #public
    _age = 36 #protected
    __salary = 20000 #private

    @property #getter
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,value):
        self.__salary = value


t = Teacher()
print(t.name)
print(t._age)
t.salary = 22000
print(t.salary)
