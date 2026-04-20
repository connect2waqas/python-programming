# Module 03 – Control Structures

## What you will learn
- `for` loops with lists, dictionaries, and `range()`
- `enumerate()` to access both index and value in a loop
- `while` loops and `break`/`continue`
- `if`/`elif`/`else` conditional logic

## Files
| File | Topics covered |
|------|---------------|
| `lecture4/code.py` | `for` loop with `enumerate()`, iterating over dictionaries with `.items()` |

## Key concepts

### for loop with a list
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### enumerate() – index + value together
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

### Iterating over a dictionary
```python
person = {"name": "Waqas", "age": 20, "status": "alive"}

# keys only
for key in person:
    print(key, ":", person[key])

# keys and values together
for key, value in person.items():
    print(f"{key}: {value}")
```

### while loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### if / elif / else
```python
score = 75
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
else:
    print("C")
```

## Practice exercises
1. Print every even number from 1 to 50 using a `for` loop and `range()`.
2. Use `enumerate()` to print a numbered shopping list.
3. Write a `while` loop that keeps asking for a number until the user enters 0.
