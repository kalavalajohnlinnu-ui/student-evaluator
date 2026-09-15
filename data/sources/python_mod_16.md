# [PYTHON] Module 16: Magic Methods & Operator Overloading
**Description**: Unlock Python's internal protocols using double-underscore magic methods.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 48. __str__ and __repr__ [Magic Methods]
### __str__ and __repr__
Define how objects are printed and represented.

**Code Example / Starter**:
```python
    def __init__(self, title): self.title = title
    # TODO: Write your code to solve the challenge:
    pass

print(Book('Python'))

```

**Solution Pattern**:
```python
class Book:
    def __init__(self, title): self.title = title
    def __str__(self): return f'Book: {self.title}'
print(Book('Python'))
```

---

### 49. __len__, __getitem__, __contains__ [Magic Methods]
### Custom Collections
Implement standard list behaviors in custom classes.

**Code Example / Starter**:
```python
    def __len__(self): return 5
    # TODO: Write your code to solve the challenge:
    pass

print(len(Box()))

```

**Solution Pattern**:
```python
class Box:
    def __len__(self): return 5
print(len(Box()))
```

---

### 50. __eq__, __lt__, __add__ — operator overloading [Overloading]
### Operator Overloading
Use `__add__` for `+`.

**Code Example / Starter**:
```python
    def __init__(self, x): self.x = x
    # TODO: Write your code to solve the challenge:
    pass

print((Vector(2) + Vector(3)).x)

```

**Solution Pattern**:
```python
class Vector:
    def __init__(self, x): self.x = x
    def __add__(self, other): return Vector(self.x + other.x)
print((Vector(2) + Vector(3)).x)
```

---

### 51. __enter__ and __exit__ — custom context managers [Context]
### Context Managers
Use `with` by defining `__enter__` and `__exit__`.

**Code Example / Starter**:
```python
    def __enter__(self): print('entering')
    # TODO: Write your code to solve the challenge:
    pass

with CM(): print('inside')

```

**Solution Pattern**:
```python
class CM:
    def __enter__(self): print('entering')
    def __exit__(self, *args): print('exiting')
with CM(): print('inside')
```

---
