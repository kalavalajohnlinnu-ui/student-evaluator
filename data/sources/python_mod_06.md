# [PYTHON] Module 6: Collections II - Dictionaries & Sets
**Description**: Map key-value pairs with dictionaries and perform fast lookups and unique operations with sets.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 16. Dictionaries (Key-Value) [Key-Value]
### Python Dictionaries
A **dictionary** stores pairs of **keys** and **values** enclosed in curly braces **`{}`**.

```python
user = {
    "name": "Leo",
    "role": "Engineer",
    "level": 5
}

# Accessing values
print(user["name"])      # 'Leo'
print(user.get("role"))  # 'Engineer' (safe lookup: returns None if key missing)

# Updating or adding keys
user["level"] = 6         # Updates level
user["city"] = "Tokyo"    # Adds new key
```

**Code Example / Starter**:
```python
# Create and update inventory:
inventory = {
    
}

# Increase gold:

print(inventory["gold"])

```

**Solution Pattern**:
```python
inventory = {
    "gold": 50,
    "potions": 3
}
inventory["gold"] += 25
print(inventory["gold"])
```

---

### 17. Looping Over Dictionaries [Dict Methods]
### Iterating Through Dictionaries
You can loop through keys, values, or both simultaneously using **`.items()`**:

```python
prices = {"apple": 1.5, "banana": 0.75, "mango": 2.0}

# Loop over keys and values
for item, price in prices.items():
    print(item, "costs $", price)
```

**Code Example / Starter**:
```python
scores = {"Alice": 90, "Bob": 85, "Charlie": 95}

total_score = 0
# Loop through scores.values() and add each to total_score:


print(total_score)

```

**Solution Pattern**:
```python
scores = {"Alice": 90, "Bob": 85, "Charlie": 95}
total_score = sum(scores.values())
print(total_score)
```

---

### 18. Sets: Unique Collections [Set Theory]
### Sets in Python
A **`set`** is an unordered collection of **unique** elements. Duplicate entries are automatically eliminated!

```python
tags = {"python", "coding", "python", "ai"}
print(tags)  # {'python', 'coding', 'ai'}

# Set operations:
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)  # Union: {1, 2, 3, 4, 5}
print(set_a & set_b)  # Intersection (common): {3}
print(set_a - set_b)  # Difference: {1, 2}
```

**Code Example / Starter**:
```python
list_with_dupes = [1, 2, 2, 3, 4, 4, 5]

unique_set = 
count = 

print(count)

```

**Solution Pattern**:
```python
list_with_dupes = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(list_with_dupes)
count = len(unique_set)
print(count)
```

---
