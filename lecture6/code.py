# here is we have to do defined the local and global variable
# x = "global x"  # global variable

# def outer():
#     x = "outer x"  # enclosing variable

#     def inner():
#         x = "inner x"  # local variable
#         print(x)  # prints local variable

#     inner()
#     print(x)  # prints enclosing variable
#     print(x)  # prints global variable
# outer()
# print(x)  # prints global variable
# prints global variable

# counter = 2

# def increment():
#     global counter 
#     counter +=8

# increment()

# print("Updated counter :", counter)

x = [1,2,3]

y = x 

z = [1,2,3]

print(x is y)
print(x is z)

# but for simple integer like if z = 123 then it will print true . also in list it print the False ones.



