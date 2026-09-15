# [PYTHON] Module 3: Making Decisions (Conditionals)
**Description**: Direct the flow of your program using if, elif, else, and logical expressions.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 7. The if & else Statements [Logic]
### Making Choices in Code
Programs make decisions using `if` and `else`. Notice the **colon `:`** and the **indentation (4 spaces)**:

```python
age = 18

if age >= 18:
    print("You are eligible to vote!")
else:
    print("Too young to vote.")
```

#### Comparison Operators:
- `==` Equal to (5 == 5 is True)
- `!=` Not equal to (5 != 3 is True)
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

> ⚠️ **Common Mistake:** Use `==` to compare values, and single `=` to assign variables!

**Code Example / Starter**:
```python
temperature = 32

# Add your if / else logic:


```

**Solution Pattern**:
```python
temperature = 32
if temperature >= 30:
    print("It is hot outside!")
else:
    print("Nice weather.")
```

---

### 8. Chained Conditions with elif [Conditionals]
### Multiple Branches with elif
When you have more than two outcomes, use **`elif`** (short for "else if"):

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)
```

Python checks conditions from top to bottom. The first condition that evaluates to True runs, and all subsequent branches are skipped!

**Code Example / Starter**:
```python
score = 88
grade = ""

# Write if-elif-else logic here:


print(grade)

```

**Solution Pattern**:
```python
score = 88
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Needs Improvement"
print(grade)
```

---

### 9. Logical Operators (and, or, not) [Boolean Logic]
### Combining Conditions
You can combine multiple conditions using Python's readable logical keywords:

- **`and`**: Returns True only if **both** sides are True.
- **`or`**: Returns True if **at least one** side is True.
- **`not`**: Reverses the boolean value (not True is False).

```python
has_ticket = True
has_id = True
is_banned = False

if has_ticket and has_id and not is_banned:
    print("Welcome to the concert!")
```

**Code Example / Starter**:
```python
has_vip_pass = True
is_registered = False

# Set access_granted using 'or':
access_granted = 

print(access_granted)

```

**Solution Pattern**:
```python
has_vip_pass = True
is_registered = False
access_granted = has_vip_pass or is_registered
print(access_granted)
```

---
