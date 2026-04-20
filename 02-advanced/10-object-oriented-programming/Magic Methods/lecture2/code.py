# # Next magic method is str method.

# class infosys:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"The student name is {self.name} and age of {self.age}"

# s1 = infosys("Waqas", 20)
# print(s1)
# # # Next magic method is __len__ method:
# # # __getin__ method in python:

# class Bank:
#     def __init__(self,balance,addaar,account_number,name):
#         self.balance = balance
#         self.addar_number = addaar
#         self.account_no = account_number
#         self.customer_name = name
    
#     def __len__(self):
#         return len(self.__dict__)
    
#     def __getitem__(self,key):
#         return self.__dict__[key]

# b1 = Bank(23442,2343235234,3432,"waqas")
# print(len(b1)) 
# del b1.account_no
# print(len(b1))
# __getin__ Method:
# indexing is involve here:

# data = [10,20,30,40,50] # it is object of class list.
# print(data[2]) # it call the __getitem__ Method for indexing:

# print(b1["addar_number"],b1["customer_name"])
from datetime import datetime
class Person:
    def __init__(self,name):
        self._name = name
        try:
            last_blank = name._rindex(" ")
            self._last_name = name[last_blank + 1]
        except:
            self._last_name = name
        self.birthday = None
    
    def get_name(self):
        return self._name
    
    def get_last_name(self):
        return self._last_name
    
    def set_birthday(self,birthdate):
        self._birthday = birthdate

    def get_age(self):
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days
    
    def __lt__(self,other):
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name
    
    def __str__(self):
        return self._name
    

me = Person("Michael Guttag")
him = Person("Barack Hussein Obama")
her = Person("Madonna")

print(him.get_last_name())
him.set_birthday(datetime.date(2005,3,8))

her.set_birthday(datetime.date(2007,8,16))

print(him.get_name() , "is", him.get_age(), "days old")