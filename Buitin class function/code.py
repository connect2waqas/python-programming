# Following are the some builtin class functions : class function okay..

# getatt()
# setatt()
class Employee:
    def __init__(self,sal,age):
        self.salary = sal
        self.age = age
    def display(self):
        print(f"Salary is {self.salary} and age is {self.age}")



e1 = Employee(30000,20)
e2 = Employee(40000,22)


# print(getattr(e1,"age"))
# setattr(e2,"age",30)
# print("Before: ",e2.__dict__)
# bool = hasattr(e2,"age")
# print(bool)
# print("After :",e2.__dict__)

print(getattr(e2,"age"))
setattr(e2,"age",23)
print(e2.__dict__)
print(hasattr(e2,"salary"))
delattr(e2,"age")
print(e2.__dict__)