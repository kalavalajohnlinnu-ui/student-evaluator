# [PYTHON] Module 19: Standard Library Power Tools
**Description**: Leverage built-in tools like math, random, collections, and datetime.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 59. math module [Math]
### Math Module
Use `math.sqrt`, `math.pi`, etc.

**Code Example / Starter**:
```python
# Quest: 59. math module
# Task: Import `math` and print `math.sqrt(16)`.

# TODO: Write your Python solution here

```

**Solution Pattern**:
```python
import math
print(math.sqrt(16))
```

---

### 60. random module [Random]
### Random Module
Use `random.randint`, `random.choice`.

**Code Example / Starter**:
```python
# Quest: 60. random module
# Task: Set `random.seed(1)`. Print `random.randint(1, 10)`.

# TODO: Write your Python solution here

```

**Solution Pattern**:
```python
import random
random.seed(1)
print(random.randint(1, 10))
```

---

### 61. datetime [Dates]
### Datetime
Manage dates and times.

**Code Example / Starter**:
```python
# Quest: 61. datetime
# Task: Import `datetime`. Print `datetime.date(2026, 1, 1).year`.

# TODO: Write your Python solution here

```

**Solution Pattern**:
```python
import datetime
print(datetime.date(2026, 1, 1).year)
```

---

### 62. collections — Counter, defaultdict, deque [Collections]
### Collections
Use `Counter` to count items.

**Code Example / Starter**:
```python
c = collections.Counter(['a', 'a', 'b'])

# TODO: Use `collections.Counter` to count `['a', 'a', 'b']`. Print the count of 'a'.
# Write your solution below:

```

**Solution Pattern**:
```python
import collections
c = collections.Counter(['a', 'a', 'b'])
print(c['a'])
```

---

### 63. functools — lru_cache, partial [Functools]
### Functools Cache
Use `@lru_cache` to memoize functions.

**Code Example / Starter**:
```python
def f(x): return x * 2
    # TODO: Write your code to solve the challenge:
    pass

print(f(5))

```

**Solution Pattern**:
```python
from functools import lru_cache
@lru_cache
def f(x): return x * 2
print(f(5))
```

---
