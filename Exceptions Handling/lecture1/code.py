# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def show(self):
#         return f"{self.name} with age {self.age} and gender {self.gender}"
        

# person = Person("waqas Ahmad",21, "male")
# import pickle
 
# with open("my_data.pkl","wb") as file:
#     pickle.dump(person, file)

# with open("my_data.pkl","rb") as file:
#     p = pickle.load(file)
#     print(type(p))
# print(p.show())
# p.name = "ilyas"
# print(p.show())


with open("sample.txt","w") as f:
    f.write("Hello world")

# try:
#     with open("sample1.txt","r") as f:
#         print(f.read())
# except:
#     print("Sorry file not found")

# num1 = 20
# num2 = 2
# try:
#     division = num1/ num2
#     print(division)
# except:
#     print("Division by zero")


# try:
#     with open("sample.txt","r") as f:
#         print(f.read())
#     num1 = 50
#     num2 = 0
#     division = num1/ num2
#     print(division)
#     l = [1,2,4,5]
# except FileNotFoundError:
#     print("file not found")
# except ZeroDivisionError:
#     print("Can't divide by Zero")
# except IndexError:
#     print("Out of range")
# except Exception as e:
#     print(e)

# try:
#     file = open("sample.txt", "r")
# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print(e)
# else:
#     print(file.read())

# try:
#     num = 50
#     num1 = 2
#     division = num/ num1
# except ZeroDivisionError:
#     print("Can divide by 0")
# except Exception as e:
#     print(e)
# else:
#     print(f"division = {division}")
# finally:
#     print("This will always executed.")

# class BankAccount:
#     def __init__(self, balance):
#          self.balance = balance
    
#     def withdraw(self, amount):
#         if not isinstance(amount,int):
#             raise Exception("Amount should be a value.")
#         if amount <= 0:
#             raise Exception("Amount can't zero or less")
#         if amount > self.balance:
#             raise Exception("Insufficient Balance")
#         self.balance -= amount

# obj = BankAccount(10000)
# try:
#     obj.withdraw(432)
# except Exception as e:
#     print(e)
# else:
#     print(obj.balance)

# class SecruityError(Exception):
#     def __init__(self, message):
#         print(message)
    
#     def logout(self):
#         print("You are logout from all devices")
# class Google:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password
#         self.device = "Andriod"
#     def login(self,email, password, device):
#         if device != self.device:
#             raise SecruityError("Unknown Device")
#         if email == self.email and password == self.password:
#             print("Welcome")
#         else:
#             print("Login error")
# obj = Google("Waqas","waqasnadan972@gmail.com",1234)
# try:
#     obj.login("waqasnadan972@gmail.com",1234,"Andriod")
# except Exception as e:
#     e.logout()
# else:
#     print(obj.name)
# finally:
#     print("Connection closed")

# def temp():
#     global a
#     a = 1
#     print(a)
# temp()
# print(a)
# import builtins
# print(dir(builtins))

# def outer():
#     def inner():
#         print(a * 2)
#     inner()
#     print("outer functions")

# a = 1
# outer()
# print("Main programm")

# def outer():
#     print("outer Function")
#     def inner_1():
#         print("inner 1")
#         def inner_2():
#             print("inner 2")
#             def inner_3():
#                 print("inner 3")
#                 def inner_4():
#                     print("inner 4")
#                 inner_4()
#             inner_3()
#         inner_2()
#     inner_1()
# outer()
# print("Main program")

# def outer():
#     a = 1
#     def inner():
#         nonlocal a
#         a +=2
#         print("inner: ", a)
#     inner()
#     print("outer: ", a)
# outer()

"New concept: "
# def func():
#     print("Hello function")

# a = func
# print(a)


def modify(func, num):
    return func(num)

def square(num):
    return num **2

val = modify(square,4)
print(val)