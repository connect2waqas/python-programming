# x = int(input("enter a number greater than 2: "))

# smallest_divisor = None

# for guess in range(2, x):
#     if x % guess == 0:
#         smallest_divisor = guess
#         break
# if smallest_divisor != None:
#     print("smallest  divisor of", x ,"is", smallest_divisor)
# else: print(x , "is prime number ")


# def is_prime(n):
#     if n <=1:
#         return False
#     if n == 2 :
#         return True
#     if n % 2 ==0:
#         return False
#     max_divisor = int(n**0.5) + 1
#     for d in range(3,max_divisor,2):
#         if n % d ==0:
#             return False
#         return True
    
# def sum_of_primes():
#     prime_sum = 0
#     for num in range(3,1000,2):
#         if is_prime(num):
#             prime_sum += num
#     prime_sum += 2
#     return prime_sum

# print(sum_of_primes())

