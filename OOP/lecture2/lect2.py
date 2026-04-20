class Employee:
    def __init__(self, salary, age):
        self.salary = salary
        self.age = age
    
    def display(self):
        print(f"Salary is {self.salary} and age {self.age}")


e1 = Employee(34000,34)
e2 = Employee(24000,23)

# print(e1.__dict__)
e1.salary = 30000
print(e1.__dict__)

e1.display()