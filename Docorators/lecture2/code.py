"Decorator: it is a function that recives another  function as a input and adds some functionality to that function and return it."
"Reason: Python works on first class citizen. function is first class citizens."

# def decorator(func):
#     def wrapper():
#         print("*********")
#         func()
#         print("*********")
#     return wrapper

# def hello():
#     print("Hello world!")

# a = decorator(hello)
# a()

# def decorator(add):
#     a = 50
#     b  = 50
#     def addition():
#         print("********")
#         added = add(a,b)
#         print(added)
#         print("********")
#     return addition
# @decorator
# def add(a , b):
#     return a + b
# add()



# import time

# def timer(func):
#     def wrapper(*args):
#         start = time.time()
#         func(*args)
#         end = time.time()
#         total_time = end - start
#         print(f"Time taken by {func.__name__} is : {total_time} secs")
#     return wrapper

# @timer
# def addition(*args):
#     add = sum(args)
#     time.sleep(2)
#     print(add)

# addition(2,4,4,3,5,6,7,9,7,6,7,8)

# def sanity_check(data_type):
#     def outer_wrapper(func):
#         def inner_wrapper(*args):
#             if type(*args) == data_type:
#                 func(*args)
#             else:
#                 raise TypeError("Invalid datatype")
#         return inner_wrapper
#     return outer_wrapper

# @sanity_check(int)
# def square(num):
#     print(num ** 2)

# square())

# def log(func):
#     def wrapper(*args):
#         print(f"name of function: {func.__name__} with {args}")
#         return func(*args)
#     return wrapper

# @log
# def addition(*args):
#    added =  sum(args)
#    print(added)
# addition(3,4,5,6)

