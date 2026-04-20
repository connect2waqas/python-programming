class Employee:
    def setname(self,name):
        self.name = name
    
    def get_name(self):
        print(f"The name is : {self.name}")


e1 = Employee()
e2 = Employee()

e1.setname(input("enter employee 1 name: "))
e2.setname(input("enter employee 2 name: "))

print(f"e1 object is: {e1.__dict__}")
print(f"e2 object is: {e2.__dict__}")

e1.get_name()
e2.get_name()