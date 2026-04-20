# Deocorator:
# Decorator are the functions that takes other functions as a inputs and then return it..

# def decor(printer):
#     def inner():
#         printer()  # existing functionality 
#         print("welcome!")
#     return inner
# @decor
# def printer():
#     print("welcome!")
#     print("welcome!")

# # printer = decor(printer)
# printer()

# def decor(addition):
#     def inner():
#         result = addition()
#         num3 = float(input("Enter third number: "))
#         result +=num3
#         return result
#     return inner
# @decor
# def addition():
#     num1 = float(input("Enter a number: "))
#     num2 = float(input("Enter another number: "))
#     result = num1 + num2
#     return result

# addition = decor(addition)
# print("Addition is : ",addition())