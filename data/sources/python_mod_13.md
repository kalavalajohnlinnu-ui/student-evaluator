# [PYTHON] Module 13: Generators & Iterators
**Description**: Create memory-efficient iterables using yield and custom iterators.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 37. Generator Functions with yield [Generators]
### Yielding Values
A generator uses `yield` instead of `return`. It pauses execution and saves memory.

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
```

**Code Example / Starter**:
```python
def even_numbers(limit):
    # TODO: Write your code to solve the challenge:
    pass

print(list(even_numbers(10)))

```

**Solution Pattern**:
```python
def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i
print(list(even_numbers(10)))
```

---

### 38. Generator Expressions [Generators]
### Generator Expressions
Like list comprehensions, but with `()` instead of `[]`. They evaluate lazily.

**Code Example / Starter**:
```python
squares_gen = (x*x for x in range(1, 4))

# TODO: Create a generator expression `squares_gen = (x*x for x in range(1, 4))` and print `list(squares_gen)`.
# Write your solution below:

```

**Solution Pattern**:
```python
squares_gen = (x*x for x in range(1, 4))
print(list(squares_gen))
```

---

### 39. Custom Iterators with __iter__ and __next__ [Iterators]
### Custom Iterators
Classes can be iterators by implementing `__iter__` and `__next__`.

**Code Example / Starter**:
```python
    def __init__(self, high):
    # TODO: Write your code to solve the challenge:
    pass

print(list(Counter(2)))

```

**Solution Pattern**:
```python
class Counter:
    def __init__(self, high):
        self.current = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < 0: raise StopIteration
        val = self.current
        self.current -= 1
        return val
print(list(Counter(2)))
```

---

### 40. itertools — chain, product, permutations [Itertools]
### itertools Module
`itertools` provides fast, memory-efficient tools for iteration.

**Code Example / Starter**:
```python
# Quest: 40. itertools — chain, product, permutations
# Task: Use `itertools.permutations` to find all 2-length permutations of `['A', 'B']`.

# TODO: Write your Python solution here

```

**Solution Pattern**:
```python
import itertools
perms = list(itertools.permutations(['A', 'B'], 2))
print(perms)
```

---
