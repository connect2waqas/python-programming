# def is_even(num):
#     return num % 2 ==0

# # list of numbers 

# numbers = [1,2,3,4,5,6,7,8,9]

# even_numbers = list(filter(is_even,numbers))
# print(even_numbers)

def filter_even(num):
    if num % 2 ==0:
        return num
numbers = [1,2,3,4,5,6,7,8,9,10]
even_number = list(filter(filter_even,numbers))
print(even_number)

# filtering the odd numbers
def filter_odd(num):
    if num % 2 !=0:
        return num
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_number = list(filter(filter_odd,numbers))
print(odd_number)

def filter_char(char):
    return len(char) > 3
    # if len(char) > 3:
    #     return char
    
words = ["cat", "window", "defenestrate", "dog"]  
check_char= list(filter(filter_char,words))
print(check_char)

data = [0, 1, False, True, "", "hello", None]  

filtered = filter(None, data)  # Remove 0, False, "", None  
print(list(filtered))  # Output: [1, True, 'hello']   

data = [0, 1, False, True, "", "hello", None]  

filtered = list(filter(None,data)) # Remove 0, False , "", None

print(filtered)