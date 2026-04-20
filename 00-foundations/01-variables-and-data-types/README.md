# Module 01 – Variables and Data Types

## What you will learn
- How to declare and use variables in Python
- Python's core data types: `int`, `float`, `str`, `bool`, `None`
- Scientific notation for floats (`1.5e2`)
- Multi-line strings with triple quotes
- The four main collection types: `list`, `tuple`, `dict`, `set`

## Files
| File | Topics covered |
|------|---------------|
| `variablepart2/code.py` | float, None, list operations (append, insert, pop, remove, extend, copy, reverse), tuple unpacking, dictionary creation and access, set operations (union, intersection, difference) |

## Key concepts

### Primitive types
```python
x = 42          # int
pi = 3.14       # float
name = "Waqas"  # str
flag = True     # bool
empty = None    # NoneType
```

### Lists (mutable, ordered)
```python
nums = [10, 20, 30]
nums.append(40)       # add to end
nums.insert(1, 15)    # insert at index
nums.pop()            # remove last
nums.remove(20)       # remove first occurrence
```

### Tuples (immutable, ordered)
```python
person = ("Waqas", 23, "AI Engineer")
name, age, role = person   # unpacking
```

### Dictionaries (key-value pairs)
```python
info = {"name": "Waqas", "age": 21}
print(info["name"])        # bracket access
print(info.get("age"))     # .get() access
```

### Sets (unique, unordered)
```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))          # {1, 2, 3, 4, 5}
print(a.intersection(b))   # {3}
```

## Practice exercises
1. Create a list of 5 favourite movies and print them in reverse order.
2. Build a dictionary with your name, age, and city, then add a new key `"job"`.
3. Create two sets of numbers and print their symmetric difference.
