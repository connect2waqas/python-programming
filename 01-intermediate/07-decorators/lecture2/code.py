# Here is the 2nd lecture of this decorator series...
# how to apply multiple decorator over the one function...

# def decor1(func):
#     def inner():
#         return func().upper()
#     return inner
# def decor2(func):
#     def inner():
#         return func().split()
#     return inner
# @decor2
# @decor1
# def get_name():
#     name = input("Enter first name: ")
#     sirname= input("Enter second name: ")
#     full_name = name + " " + sirname
#     return full_name

# # get_name =decor2(decor1(get_name)) 
# print(get_name())


def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold  # Second decorator applied (outer layer)
@italic  # First decorator applied (inner layer)
def greet():
    return "Hello!"

print(greet())  # Output: <b><i>Hello!</i></b>