# Module 02 – Operators and Expressions

## What you will learn
- Arithmetic, comparison, assignment, and logical operators
- Operator precedence
- Measuring execution time with `time.time()`
- Writing and calling simple functions

## Files
| File | Topics covered |
|------|---------------|
| `lecture3/code.py` | Arithmetic operators, comparison operators, timing functions with `time.time()`, multiplication table function |

## Key concepts

### Arithmetic operators
```python
a, b = 10, 3
print(a + b)   # Addition:       13
print(a - b)   # Subtraction:     7
print(a * b)   # Multiplication: 30
print(a / b)   # Division:        3.333...
print(a // b)  # Floor division:  3
print(a % b)   # Modulus:         1
print(a ** b)  # Exponentiation: 1000
```

### Comparison operators
```python
x, y = 10, 5
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False
print(x == y)  # False
print(x != y)  # True
```

### Measuring execution time
```python
from time import time

start = time()
# ... code to measure ...
end = time()
print(f"Duration: {end - start:.6f} seconds")
```

### Assignment operators
```python
n = 10
n += 5   # n = 15
n -= 3   # n = 12
n *= 2   # n = 24
n //= 4  # n = 6
```

## Practice exercises
1. Write a function that takes two numbers and prints all arithmetic operations on them.
2. Measure and compare the execution time of a loop-based sum vs the formula `n*(n+1)/2`.
3. Build a simple calculator that takes two numbers and an operator as input.
