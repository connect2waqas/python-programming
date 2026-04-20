# Module 06 – Exception Handling

## What you will learn
- The `try` / `except` block to catch errors gracefully
- Handling multiple exception types separately
- The `else` clause (runs when no exception occurs)
- The `finally` clause (always runs, good for cleanup)
- Raising your own exceptions with `raise`
- Custom exception classes

## Files
| File | Topics covered |
|------|---------------|
| `lecture1/main.py` | `try`/`except` with `ZeroDivisionError` and `KeyError` |

## Key concepts

### Basic try / except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Catching multiple exceptions
```python
try:
    a = 10 / 0
    d = {"name": "Waqas"}
    print(d["age"])
except ZeroDivisionError:
    print("Division by zero!")
except KeyError as e:
    print(f"Key not found: {e}")
```

### else and finally
```python
try:
    result = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number.")
else:
    print(f"You entered: {result}")   # only runs if no exception
finally:
    print("Done.")                    # always runs
```

### Raising exceptions manually
```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age
```

### Custom exception class
```python
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough money!")
    return balance - amount
```

## Practice exercises
1. Write a function `safe_divide(a, b)` that catches `ZeroDivisionError` and returns `None` instead of crashing.
2. Ask the user to enter an integer in a loop; keep asking until they enter a valid one using `ValueError`.
3. Create a custom exception `NegativeNumberError` and raise it when a function receives a negative input.
