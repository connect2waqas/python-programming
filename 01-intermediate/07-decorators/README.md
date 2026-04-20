# Module 07 – Decorators

## What you will learn
- What a decorator is and why it is useful
- Writing a basic decorator function
- The `@syntax` shorthand
- Stacking multiple decorators on one function
- Decorators that accept arguments (using `functools.wraps`)
- Real-world use cases: logging, timing, authentication

## Files
| File | Topics covered |
|------|---------------|
| `lecture1/code.py` | Basic decorator concept, adding behaviour before/after a function |
| `lecture2/code.py` | Stacking two decorators (`@bold` + `@italic`), order of application |
| `lecture9/code.py` | Additional decorator examples |
| `lecture11/main.py` | Logging and timing decorators with arguments, requests library demo |

## Key concepts

### What is a decorator?
A decorator is a function that **wraps** another function to add behaviour without changing the original code.

```python
def shout(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@shout
def greet():
    return "hello"

print(greet())   # HELLO
```

### The `@` shorthand
`@shout` above is exactly the same as writing:
```python
greet = shout(greet)
```

### Stacking decorators
Decorators are applied from **bottom to top** (innermost first):
```python
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold    # applied second (outer layer)
@italic  # applied first  (inner layer)
def greet():
    return "Hello!"

print(greet())   # <b><i>Hello!</i></b>
```

### Decorator with arguments (use `functools.wraps`)
```python
from functools import wraps

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()   # prints "Hi!" three times
```

### Logging decorator
```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

## Practice exercises
1. Write a decorator `timer` that prints how long a function takes to run.
2. Write a decorator `validate_positive` that raises `ValueError` if any argument to the decorated function is negative.
3. Stack two decorators on a function: one that uppercases the result and one that adds `"!!"` at the end.
