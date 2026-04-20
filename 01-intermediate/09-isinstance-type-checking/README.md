# Module 09 – isinstance and Type Checking

## What you will learn
- What `isinstance()` does and when to use it
- Checking against multiple types at once with a tuple
- How `isinstance()` respects inheritance (subclass check)
- Writing defensive code that validates input types
- `type()` vs `isinstance()` — the difference

## Files
| File | Topics covered |
|------|---------------|
| `isinstances/code.py` | Basic `isinstance()`, inheritance check, checking multiple types, input validation with `TypeError`, dynamic dispatch by type |

## Key concepts

### Basic isinstance()
```python
x = 5.5
print(isinstance(x, float))   # True
print(isinstance(x, int))     # False
```

### Checking multiple types at once
```python
value = 42
print(isinstance(value, (int, float, str)))   # True
```

### isinstance() respects inheritance
```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True  ← because Dog inherits from Animal
```

### Input validation
```python
def process(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Expected a list or tuple!")
    return sum(data)

print(process([1, 2, 3]))   # 6
```

### Dynamic dispatch by type
```python
def handle(value):
    if isinstance(value, int):
        print(f"Integer doubled: {value * 2}")
    elif isinstance(value, str):
        print(f"String uppercased: {value.upper()}")
    elif isinstance(value, list):
        print(f"List sum: {sum(value)}")

handle(10)          # Integer doubled: 20
handle("hello")     # String uppercased: HELLO
handle([1, 2, 3])   # List sum: 6
```

### type() vs isinstance()
```python
# type() does NOT consider inheritance
class Dog(Animal):
    pass

dog = Dog()
print(type(dog) == Animal)      # False — exact match only
print(isinstance(dog, Animal))  # True  — includes subclasses
```
Prefer `isinstance()` in most cases.

## Practice exercises
1. Write a function `describe(value)` that prints the type name and a short description for `int`, `float`, `str`, `list`, and `dict`.
2. Write a function `safe_add(a, b)` that raises `TypeError` if either argument is not a number.
3. Build a simple class hierarchy (`Vehicle → Car, Bike`) and use `isinstance()` to check which type each object belongs to.
