# Module 08 – Built-in Functions

## What you will learn
- Higher-order functions: `map()`, `filter()`, `reduce()`
- Lambda (anonymous) functions
- `zip()`, `sorted()`, `enumerate()`, `any()`, `all()`
- List comprehensions as a clean alternative to `map`/`filter`
- Built-in class methods (covered in `built-in-class-functions/code.py`)

## Files
| File | Topics covered |
|------|---------------|
| `lecture7/code.py` | `map()` with custom functions, built-in functions, and lambda |
| `lecture8/code.py` | Additional higher-order function examples |
| `built-in-class-functions/code.py` | Built-in methods on classes |

## Key concepts

### map() – apply a function to every element
```python
words = ["apple", "banana", "cherry"]
upper = list(map(str.upper, words))
print(upper)   # ['APPLE', 'BANANA', 'CHERRY']

numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8]
```

### filter() – keep elements that pass a test
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6]
```

### reduce() – fold a sequence to a single value
```python
from functools import reduce
nums = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, nums)
print(total)   # 15
```

### Lambda (anonymous) functions
```python
square = lambda x: x ** 2
print(square(5))   # 25

# Often used inline with map/filter/sorted
nums = [3, 1, 4, 1, 5]
print(sorted(nums, key=lambda x: -x))   # [5, 4, 3, 1, 1]
```

### zip() – pair up two lists
```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

### List comprehension (often cleaner than map/filter)
```python
# map equivalent
doubled = [x * 2 for x in range(5)]

# filter equivalent
evens = [x for x in range(10) if x % 2 == 0]
```

## Practice exercises
1. Use `map()` to convert a list of temperatures in Celsius to Fahrenheit.
2. Use `filter()` to keep only strings longer than 4 characters from a list.
3. Use `reduce()` to find the product of all numbers in a list.
4. Rewrite exercises 1–3 using list comprehensions.
