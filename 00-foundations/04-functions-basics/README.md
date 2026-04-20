# Module 04 – Functions Basics

## What you will learn
- Defining and calling functions with `def`
- Parameters, return values, and default arguments
- Variable scope: local, enclosing, and global variables
- The `global` keyword
- Identity vs equality: `is` vs `==`

## Files
| File | Topics covered |
|------|---------------|
| `lecture6/code.py` | LEGB scope rules, `global` keyword, `is` vs `==` identity check |
| `lecture10/code.py` | (see file for additional function examples) |

## Key concepts

### Defining and calling a function
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Waqas"))   # Hello, Waqas!
```

### Default parameter values
```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9  (uses default exponent)
print(power(3, 3))   # 27
```

### LEGB scope (Local → Enclosing → Global → Built-in)
```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)   # local
    inner()
    print(x)       # enclosing

outer()
print(x)           # global
```

### Modifying a global variable
```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)   # 1
```

### Identity (`is`) vs equality (`==`)
```python
x = [1, 2, 3]
y = x           # same object
z = [1, 2, 3]   # equal but different object

print(x == z)   # True  (same values)
print(x is y)   # True  (same object)
print(x is z)   # False (different object)
```

## Practice exercises
1. Write a function `factorial(n)` that returns `n!` using a loop.
2. Write a function `celsius_to_fahrenheit(c)` and test it for freezing, body, and boiling temperatures.
3. Create two variables that point to the same list, then show that modifying one modifies the other.
