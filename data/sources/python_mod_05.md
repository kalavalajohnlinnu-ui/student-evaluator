# [PYTHON] Module 5: Collections I - Lists & Tuples
**Description**: Store ordered sequences of data, mutate lists with methods, and understand immutable tuples.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 13. Lists & Indexing [Data Structures]
### Python Lists
A **list** is an ordered, mutable collection of items wrapped in square brackets **`[]`**.

```python
fruits = ["apple", "banana", "cherry", "date"]

# Indexing starts at 0!
print(fruits[0])   # 'apple'
print(fruits[2])   # 'cherry'

# Negative indexing counts from the end!
print(fruits[-1])  # 'date' (last item)
print(fruits[-2])  # 'cherry' (second to last)
```

**Code Example / Starter**:
```python
colors = ["red", "green", "blue", "yellow", "purple"]

# Access elements:
first_color = 
last_color = 

print(first_color)
print(last_color)

```

**Solution Pattern**:
```python
colors = ["red", "green", "blue", "yellow", "purple"]
first_color = colors[0]
last_color = colors[-1]
print(first_color)
print(last_color)
```

---

### 14. Modifying Lists (Methods) [Mutations]
### List Methods
Lists are **mutable** (can be modified in place):

```python
items = ["sword", "shield"]

items.append("potion")       # Adds to the end: ['sword', 'shield', 'potion']
items.insert(0, "helmet")     # Inserts at index 0
items.remove("shield")       # Removes first matching item
removed = items.pop()        # Removes & returns last item ('potion')
items.sort()                 # Sorts the list
print(len(items))            # Length of list
```

**Code Example / Starter**:
```python
cart = ["apple", "banana"]

# Perform modifications:


print(cart)

```

**Solution Pattern**:
```python
cart = ["apple", "banana"]
cart.append("orange")
cart.insert(0, "bread")
print(cart)
```

---

### 15. Slicing & Immutable Tuples [Sequences]
### Slicing & Tuples
#### Advanced Slicing: `[start : stop : step]`
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7]
print(nums[1:5])    # [1, 2, 3, 4]
print(nums[::2])    # [0, 2, 4, 6] (every 2nd item)
print(nums[::-1])   # [7, 6, 5, 4, 3, 2, 1, 0] (reverse!)
```

#### Tuples: Frozen Lists
A **tuple** is created with parentheses **`()`**. Unlike lists, tuples are **immutable**—they cannot be changed after creation!
```python
point = (10, 20)
# point[0] = 15  # ERROR! Tuples cannot be modified.
x, y = point    # Unpacking! x = 10, y = 20
```

**Code Example / Starter**:
```python
data = [1, 2, 3, 4, 5, 6]

# 1. Reverse data using slice:
reversed_data = 

# 2. Define tuple coords and unpack:
coords = (100, 250)
pos_x, pos_y = 

print(pos_x)
print(pos_y)

```

**Solution Pattern**:
```python
data = [1, 2, 3, 4, 5, 6]
reversed_data = data[::-1]
coords = (100, 250)
pos_x, pos_y = coords
print(pos_x)
print(pos_y)
```

---
