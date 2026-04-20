# class Infosystem:
#     def __init__(self,name , age , profession):
#         self.name = name 
#         self.age = age
#         self.profession = profession
    
#     def change_data(self):
#         print("before change:", self.age)
#         self.age = int(input("enter your age: "))
#         print(f"New age is {self.age}")

    

# s1 = Infosystem("waqas",20,"Artificial intelligence Engineer")

# # print("Before change:")
# # print(s1.age)
# # s1.change_data()
# # print("After Change:")

# e2 = Infosystem("roman",23,"Ai scientist")
# # print(getattr(e2,"age"))
# # print(e2.age)
# setattr(e2,"name","ilyas")
# print(e2.name)

# # print(s1.__dict__)
# # print(e2.__dict__)

# setattr(e2,"profession","Electronic Engineer")
# print(e2.__dict__)


# class Int_set(object):
#     def __init__(self):
#         self.__vals = []
    
#     def insert(self, e):
#         if e not in self.__vals:
#             self.__vals.append(e)
    
#     def member(self, e):
#         return e in self.__vals
    
#     def remove(self, e):
#         try:
#             self.__vals.remove(e)
#         except:
#             raise ValueError(str(e) + "not found")
    
#     def get_members(self):
#         return self.__vals[:]
    
#     def __str__(self):
#         if self.__vals == []:
#             return "{}"
#         self.__vals.sort()
#         result = " "
#         for e in self.__vals:
#             result = result + str(e) + ","
        
#         return f"{{{result[:-1]}}}" 
    
# s = Int_set()
# s.insert(3)
# print(s.member(3))


class System:
    company_name = "Xeven solution"
    def __init__(self , name , salary, ):
        self.name = name 
        self.salary = salary
    
    def display(self,age):
        self.age = age
        print(f"{self.name} have salary : {self.salary} of age: {self.age}")
    
    @classmethod
    def show(cls):
        cls.company_name = "Zong"
        cls.highest_position = "Product Manager"
        print(f"The company name is {cls.company_name} and highest profession is {cls.highest_position}")

    

e1 = System("ilyas",5000)
print(e1.show())
e1.display(age=int(input("enter age: ")))
print(System.company_name)