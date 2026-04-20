# what we have to learn to are as under :
# what is decorator
# function of decrotor and their funtion:

# Example ::

# def decor(printer):
#     def inner():
#         printer()
#         print("Hello")
#     return inner

# @decor
# def printer():
#     print("Welcome!")
#     print("Welcome!")
# printer()

# def decor(addition):
#     def inner():
#         result = addition()
#         num3 = float(input("enter 3rd number: "))
#         result = result + num3
#         return result
#     return inner

# @decor
# def addition():
#     num1 = float(input("enter a number: "))
#     num2 = float(input("enter another number: "))
#     result = num1 + num2
#     return result

# print("The addition is ", addition())

def decor(string):
    def inner():
        result = string()
        str3 = input("enter another one: ")
        result += str3
        return result
    return inner

@decor
def string():
    str1 = input("enter a string: ")
    str2 = input("enter another string: ")
    concatnate = str1 + " " +str2
    return concatnate
print("The full string is ", string())