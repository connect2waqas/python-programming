# here we have to study operator in pyhton 
# The operator are that part on which other thangs can be made
# it forms logical condition in programming
# it create a stitution in programming 
# there a different type of operator like 
# 1) comparising operator
# 2) assignment operator
# 3) logical operator
# 4) Arthimetic operator
# lets code it

# Basic arthimetic operator
# a , b = 10 , 3

# print("Addition:" , a + b)
# print("Multiplication: ", a*b)
# print("Substration: ", a - b)
# print("Division: ", a/b)
# print("Floor Division: ",a //b)
# print("Modulus: ", a % b)
# print("Exponentation :", a**b)

# # comparsion operator

# x , y = 10 , 5

# print("x > y: ", x > y)
# print("x < y: ", x < y)
# print("x >= y: ", x >= y)
# print("x <= y: ", x <= y)
# print("x != y: ", x != y)
# print("x == y: ", x == y)



# n = int(input().strip())
# for i in range(n):
#     print(n,"x",i, "=", n * i)
from time import time
def sumofN(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

# start_time  = time()
# x = sumofN(9000)
# end_time = time()
# duration = end_time - start_time
# print(f"for {x} time is {duration}")


# def sumofN(n):
#     return int((n*(n+1)) / 2)
# start_time = time()
# x = sumofN(900000000000)
# end_time = time()
# duration = end_time - start_time
# print(f"for {x} is {duration}")

def NumberTable(n):
    for i in range(n):
        print(n,"x",i, "=", n * i)
start_time = time()
x = NumberTable(10)
end_time = time()
duration = end_time - start_time
print(x)
print(duration)