# here is we have to start the higher order function in python. it is used to make the code more modular and more readible okay.

# The first Higher order function that we have to study is:
# 1):  Map function: 
# it is built-in python function that applies specific function to an iterable okay..

# def to_upper(s):
#     return s.upper()

# words = ["apple", "banana", "cherry"]
# uppercase = map(to_upper, words)
# print(list(uppercase))  # Output: ['APPLE', 'BANANA', 'CHERRY']

# def to_upper(s):
#     return s.upper()


# words = ["apple","banana","cherry"]
# uppercase = map(to_upper,words)
# print(list(uppercase)) 

# using built-in function: 

# str_numbers = ["3", "7", "11"]
# int_numbers = map(int, str_numbers)
# print(list(int_numbers))  # Output: [3, 7, 11]

# str_numbers = ["2","4","6"]
# int_numbers = map(int,str_numbers)
# print(list(int_numbers))

# words = ["dog", "elephant", "cat"]
# lengths = map(len, words)
# print(list(lengths))  # Output: [3, 8, 3]
# words = ["dogs","cats","elephant"]

# lengths = map(len,words)

# print(list(lengths))

# def square(n):
#     print(n**2)

# num = 2
# square_n = map(square,num)
# print(square_n)

# def double(x):
#     return x*2
# # using map() to double the list 
# numbers = [2,4,6,8]
# doubled = list(map(double,numbers))
# print(doubled)