# [PYTHON] Module 2: Variables & Data Types
**Description**: Store information in memory, manipulate numbers, inspect types, and master strings.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 3. Variables: Memory Boxes [Core]
### What is a Variable?
Think of a variable as a labeled storage box in your computer's memory. You assign a value to a variable using the assignment operator **`=`**.

```python
player_name = "Aria"
health = 100
level = 1

print(player_name)
print(health)
```

#### Variable Naming Rules:
- Names can contain letters, numbers, and underscores (`_`).
- Cannot start with a number (e.g. `1player` is illegal, `player_1` is good).
- In Python, we use **snake_case**: lowercase words separated by underscores (e.g. `user_age`, `total_score`).

**Code Example / Starter**:
```python
# Define your variables and print them:
player_name = ""
score = 0

print(player_name)
print(score)

```

**Solution Pattern**:
```python
player_name = "Shadow"
score = 950
print(player_name)
print(score)
```

---

### 4. Numbers & Arithmetic [Math]
### Working with Numbers
Python has two main number types:
1. **Integers (`int`)**: Whole numbers like `10`, `-5`, `0`.
2. **Floats (`float`)**: Numbers with decimal points like `3.14`, `-0.5`.

#### Python Arithmetic Operators:
- **`+`** Addition (`10 + 5 = 15`)
- **`-`** Subtraction (`10 - 4 = 6`)
- **`*`** Multiplication (`3 * 4 = 12`)
- **`/`** Division (always produces a float: `10 / 2 = 5.0`)
- **`//`** Floor Division (rounds down to integer: `10 // 3 = 3`)
- **`%`** Modulo (remainder: `10 % 3 = 1`)
- **`**`** Exponent / Power (`2 ** 3 = 8`)

**Code Example / Starter**:
```python
meal = 80
tip = 15

# 1. Calculate total
total = 

# 2. Calculate per_person
per_person = 

print(per_person)

```

**Solution Pattern**:
```python
meal = 80
tip = 15
total = meal + tip
per_person = total / 2
print(per_person)
```

---

### 5. String Superpowers [Text]
### Manipulating Strings
Strings come with built-in superpower methods:

```python
msg = "  python rocks!  "

print(msg.strip())       # "python rocks!" (removes outer spaces)
print(msg.upper())       # "  PYTHON ROCKS!  "
print(msg.lower())       # "  python rocks!  "
print(msg.title())       # "  Python Rocks!  "
print(msg.replace("rocks", "rules")) # "  python rules!  "
print(len(msg))          # Counts character length
```

#### String Slicing:
You can grab parts of a string with brackets `[start:end]`:
```python
word = "Python"
print(word[0])    # 'P' (First character, 0-indexed!)
print(word[0:3])  # 'Pyt' (From index 0 up to, but not including, index 3)
print(word[-1])   # 'n' (Last character)
```

**Code Example / Starter**:
```python
raw_email = "  USER@EXAMPLE.COM  "

# Clean the email:
clean_email = 

print(clean_email)

```

**Solution Pattern**:
```python
raw_email = "  USER@EXAMPLE.COM  "
clean_email = raw_email.strip().lower()
print(clean_email)
```

---

### 6. Booleans & Type Conversion [Types]
### Truth Values & Converting Types
A **Boolean** has only two possible values: **`True`** or **`False`** (capitalized!).

#### Type Conversion (Casting):
When you read data from files or user input, numbers often arrive as strings (`"42"`). You must convert them:
- `int("42")` ➔ 42
- `float("3.14")` ➔ 3.14
- `str(100)` ➔ "100"
- `bool(1)` ➔ True (0 is False, empty strings are False)

```python
# Check type with type()
x = 50
print(type(x))  # <class 'int'>
```

**Code Example / Starter**:
```python
price_str = "45.50"
quantity_str = "4"

# Convert types and compute:
price_num = 
quantity_num = 
total_cost = 

print(total_cost)

```

**Solution Pattern**:
```python
price_str = "45.50"
quantity_str = "4"
price_num = float(price_str)
quantity_num = int(quantity_str)
total_cost = price_num * quantity_num
print(total_cost)
```

---
