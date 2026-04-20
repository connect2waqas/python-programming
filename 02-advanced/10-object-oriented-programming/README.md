# Module 10 – Object-Oriented Programming

## What you will learn
- Classes, objects, attributes, and methods
- The `__init__` constructor
- Instance vs class attributes
- Inheritance and `super()`
- Magic (dunder) methods: `__str__`, `__repr__`, `__dict__`, `__new__`
- `getattr()` / `setattr()` for dynamic attribute access
- Encapsulation concepts

## Files
| File | Topics covered |
|------|---------------|
| `lecture1/code.py` | Class basics — `AIstudent`, `Employee`, `Management`; `__dict__`; `getattr`/`setattr` |
| `lecture2/lect2.py` | Class examples continued |
| `lecture3/lect3.py` | More class examples |
| `lecture4/lect4.py` | More class examples |
| `lecture 5/lect5.py` | More class examples |
| `inheritance/lecture1/main.py` | Inheritance with `Pet`→`Cat`→`Cheshire`; `super()`; `Book`→`PaperBook`/`EBook`; `Library` |
| `Magic Methods/lecture1/code.py` | `__dict__`, `__new__`; `Bank` class |
| `Magic Methods/lecture2/code.py` | Additional magic methods |
| `object to strings/main.py` | `__str__` and `__repr__` |

## Key concepts

### Defining a class
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name}, age {self.age}")

s = Student("Waqas", 21)
s.greet()
```

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.speak())   # Woof!
```

### super() – calling the parent constructor
```python
class PaperBook(Book):
    def __init__(self, title, author, num_pages):
        super().__init__(title, author)   # call Book.__init__
        self.num_pages = num_pages
```

### __str__ – human-readable string representation
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book("Atomic Habits", "James Clear")
print(b)   # Atomic Habits by James Clear
```

### getattr / setattr – dynamic attributes
```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Waqas")
print(getattr(p, "name"))        # Waqas
setattr(p, "age", 21)            # add new attribute
print(p.__dict__)                # {'name': 'Waqas', 'age': 21}
```

## Practice exercises
1. Create a `BankAccount` class with `deposit()` and `withdraw()` methods and a balance that cannot go below zero.
2. Create a `Shape` base class with an `area()` method, then subclass it into `Circle` and `Rectangle`.
3. Add `__str__` to both subclasses so that `print(shape)` gives a friendly description including the area.
