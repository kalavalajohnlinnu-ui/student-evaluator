# [PYTHON] Module 17: Abstract Base Classes & Interfaces
**Description**: Enforce strict class designs using ABCs and protocols.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 52. abc.ABC and @abstractmethod [ABC]
### Abstract Base Classes
Use `ABC` and `@abstractmethod` to enforce method implementation.

**Code Example / Starter**:
```python
    def process(self): pass
    # TODO: Write your code to solve the challenge:
    pass

print('Done')

```

**Solution Pattern**:
```python
from abc import ABC, abstractmethod
class Worker(ABC):
    @abstractmethod
    def process(self): pass
print('Done')
```

---

### 53. Designing class hierarchies with ABCs [ABC]
### ABC Hierarchies
Subclasses must implement abstract methods.

**Code Example / Starter**:
```python
    def area(self): pass
    # TODO: Write your code to solve the challenge:
    pass

class Square(Shape):
print(Square().area())

```

**Solution Pattern**:
```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
class Square(Shape):
    def area(self): return 4
print(Square().area())
```

---

### 54. Protocol classes (structural subtyping) [Protocol]
### Protocols
`typing.Protocol` allows structural subtyping checking.

**Code Example / Starter**:
```python
    def draw(self): pass
    # TODO: Write your code to solve the challenge:
    pass

print('Drawable defined')

```

**Solution Pattern**:
```python
from typing import Protocol
class Drawable(Protocol):
    def draw(self): pass
print('Drawable defined')
```

---
