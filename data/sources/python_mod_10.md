# [PYTHON] Module 10: Pythonic Superpowers
**Description**: Master list comprehensions, f-strings, enumerate, zip, and idiomatic Python.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 27. List Comprehensions [Pythonic]
### The Elegance of List Comprehensions
List comprehensions provide a concise way to create new lists by transforming or filtering elements:

```python
# Standard loop:
squares = []
for x in range(5):
    squares.append(x ** 2)

# Pythonic List Comprehension:
squares = [x ** 2 for x in range(5)]
# [0, 1, 4, 9, 16]

# With filtering condition:
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

**Code Example / Starter**:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Create list comprehension:
doubled_high = 

print(doubled_high)

```

**Solution Pattern**:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
doubled_high = [x * 2 for x in numbers if x > 4]
print(doubled_high)
```

---

### 28. F-Strings & Formatting [String Magic]
### Modern String Formatting: f-strings
Introduced in Python 3.6, **f-strings** are fast and readable:

```python
name = "Kiran"
points = 88.547

# Interpolation and decimal formatting:
msg = f"Player {name} scored {points:.2f} points!"
print(msg)  # 'Player Kiran scored 88.55 points!'
```

Formatting Modifiers:
- `:.2f`: 2 decimal places
- `:>10`: Right-align in 10 spaces
- `:, `: Adds commas to large numbers (e.g. 1,000,000)

**Code Example / Starter**:
```python
product = "Laptop"
cost = 899.95
discount = 0.15

final_price = cost * (1 - discount)
summary = 

print(summary)

```

**Solution Pattern**:
```python
product = "Laptop"
cost = 899.95
discount = 0.15
final_price = cost * (1 - discount)
summary = f"{product} costs ${final_price:.2f}"
print(summary)
```

---

### 29. Built-in Superheroes: enumerate & zip [Idiomatic]
### enumerate() and zip()
#### 1. `enumerate()`: Loop with Index
Never use `range(len(items))` again!
```python
heroes = ["Batman", "Iron Man", "Spider-Man"]
for index, hero in enumerate(heroes, start=1):
    print(f"{index}. {hero}")
```

#### 2. `zip()`: Pair Two Lists Together
```python
names = ["Alice", "Bob"]
scores = [95, 88]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

**Code Example / Starter**:
```python
tasks = ["Wake up", "Code Python", "Sleep"]

# Loop with enumerate:
for i, t in enumerate(tasks, start=1):
    pass

```

**Solution Pattern**:
```python
tasks = ["Wake up", "Code Python", "Sleep"]
for i, t in enumerate(tasks, start=1):
    print(f"{i}: {t}")
```

---
