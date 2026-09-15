# [PYTHON] Module 21: Type Hints & Modern Python
**Description**: Write robust code using type annotations and structural pattern matching.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 68. Type Annotations — int, str, list[int] [Types]
### Type Hints
Add hints like `def f(x: int) -> str:`.

**Code Example / Starter**:
```python
def double(x: int) -> int:
    # TODO: Write your code to solve the challenge:
    pass

print(double(4))

```

**Solution Pattern**:
```python
def double(x: int) -> int:
    return x * 2
print(double(4))
```

---

### 69. Optional, Union, Any from typing [Types]
### Typing module
Use `Union[int, str]` or `int | str`.

**Code Example / Starter**:
```python
x: Union[int, str] = 'hello'

# TODO: Import `Union` from `typing`. Define `x: Union[int, str] = 'hello'` and print it.
# Write your solution below:

```

**Solution Pattern**:
```python
from typing import Union
x: Union[int, str] = 'hello'
print(x)
```

---

### 70. @dataclass [Dataclass]
### Dataclasses
`@dataclass` auto-generates `__init__` and `__repr__`.

**Code Example / Starter**:
```python
class Point:
    def __init__(self):
        # TODO: Initialize attributes here
        pass

```

**Solution Pattern**:
```python
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
print(Point(1, 2))
```

---

### 71. Structural Pattern Matching match/case [Pattern Matching]
### match / case
Introduced in Python 3.10.

**Code Example / Starter**:
```python
status = 200

# TODO: Write a `match` on `status = 200`. Case `200`: print 'OK'.
# Write your solution below:

```

**Solution Pattern**:
```python
status = 200
match status:
    case 200: print('OK')
    case _: print('Unknown')
```

---
