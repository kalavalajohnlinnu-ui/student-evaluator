# [PYTHON] Module 11: Real-World Capstone Projects
**Description**: Apply everything you learned to build 3 real practical Python programs.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 30. Capstone: Smart Calculator Engine [Project 1]
### Capstone Project: Smart Calculator
Build a modular calculator engine that takes two numbers and an operator, computes the result, and tracks history.

```python
def calculate(a, op, b):
    if op == '+': return a + b
    # handle -, *, /
```

**Code Example / Starter**:
```python
def calculate(a, op, b):
    # Implement operations:
    pass

res = calculate(10, '*', 5)
print(res)

```

**Solution Pattern**:
```python
def calculate(a, op, b):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/':
        if b == 0: return "Error: Division by zero"
        return a / b
    return "Unknown operator"

res = calculate(10, '*', 5)
print(res)
```

---

### 31. Capstone: Password Strength Analyzer [Project 2]
### Capstone Project: Password Strength Scorer
Security systems inspect password characteristics:
- Length >= 8
- Contains at least one digit
- Contains at least one uppercase letter
- Contains at least one special character

Using string methods like `.isupper()` and `.isdigit()`, you can build a fast security analyzer.

**Code Example / Starter**:
```python
def check_password(pw):
    # TODO: Write your code to solve the challenge:
    pass

result = check_password("PythonMaster2026")
print(result)

```

**Solution Pattern**:
```python
def check_password(pw):
    has_min_len = len(pw) >= 8
    has_digit = any(c.isdigit() for c in pw)
    if has_min_len and has_digit:
        return "Strong"
    return "Weak"

result = check_password("PythonMaster2026")
print(result)
```

---

### 32. Capstone: Mini RPG Battle Simulator [Project 3]
### Capstone Project: Turn-Based Mini RPG
Bring together classes, loops, conditionals, and arithmetic to build a battle round simulator!

**Code Example / Starter**:
```python
    def __init__(self, name, hp, attack):
    # TODO: Write your code to solve the challenge:
    pass

hero = Character("Knight", 50, 15)
goblin = Character("Goblin", 30, 8)
while goblin.hp > 0:
print(f"{hero.name} defeated the {goblin.name}!")

```

**Solution Pattern**:
```python
class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

hero = Character("Knight", 50, 15)
goblin = Character("Goblin", 30, 8)

while goblin.hp > 0:
    goblin.hp -= hero.attack
    print(f"{hero.name} attacks {goblin.name}! Goblin HP: {max(0, goblin.hp)}")

print(f"{hero.name} defeated the {goblin.name}!")
```

---
