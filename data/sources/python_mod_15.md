# [PYTHON] Module 15: Advanced OOP — Encapsulation & Polymorphism
**Description**: Deep dive into properties, class methods, and duck typing.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 44. Private Attributes & Name Mangling [Encapsulation]
### Private Attributes
Use `__` prefix to make attributes private (name mangling).

**Code Example / Starter**:
```python
    def __init__(self, code):
    # TODO: Write your code to solve the challenge:
    pass

s = Secret('42')
print(s.get_code())

```

**Solution Pattern**:
```python
class Secret:
    def __init__(self, code):
        self.__code = code
    def get_code(self): return self.__code
s = Secret('42')
print(s.get_code())
```

---

### 45. @property Getters and Setters [Encapsulation]
### @property
Use `@property` to define getters and setters.

**Code Example / Starter**:
```python
    def __init__(self):
    # TODO: Write your code to solve the challenge:
    pass

print(Weather().temperature)

```

**Solution Pattern**:
```python
class Weather:
    def __init__(self):
        self._temp = 20
    @property
    def temperature(self):
        return self._temp
print(Weather().temperature)
```

---

### 46. @classmethod and @staticmethod [OOP]
### Class and Static Methods
`@classmethod` takes `cls`. `@staticmethod` takes neither `self` nor `cls`.

**Code Example / Starter**:
```python
    def from_string(cls, s):
    # TODO: Write your code to solve the challenge:
    pass

print(type(Date.from_string('2026')).__name__)

```

**Solution Pattern**:
```python
class Date:
    @classmethod
    def from_string(cls, s):
        return cls()
print(type(Date.from_string('2026')).__name__)
```

---

### 47. Polymorphism & Duck Typing [Polymorphism]
### Duck Typing
If it walks like a duck, it's a duck.

**Code Example / Starter**:
```python
def make_sound(entity): return entity.sound()
    # TODO: Write your code to solve the challenge:
    pass

print(make_sound(Dog()))

```

**Solution Pattern**:
```python
class Dog: def sound(self): return 'woof'
def make_sound(entity): return entity.sound()
print(make_sound(Dog()))
```

---
