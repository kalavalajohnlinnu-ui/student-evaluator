# [PYTHON] Module 20: Regular Expressions
**Description**: Master string matching and manipulation using regex and the re module.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 64. Pattern Matching Basics — re.search(), re.findall() [Regex]
### Basic Regex
Use `re.findall` to find all matches.

**Code Example / Starter**:
```python
# Quest: 64. Pattern Matching Basics — re.search(), re.findall()
# Task: Find all digits in 'A1 B2' using `re.findall(r'\d', ...)`.

# TODO: Write your Python solution here

```

**Solution Pattern**:
```python
import re
print(re.findall(r'\d', 'A1 B2'))
```

---

### 65. Character Classes, Quantifiers, Anchors [Regex]
### Quantifiers
`+` means 1 or more, `*` means 0 or more.

**Code Example / Starter**:
```python
# Quest: 65. Character Classes, Quantifiers, Anchors
# Task: Find words with at least one 'a' using `re.findall(r'\w*a\w*', 'cat dog apple')`.

# TODO: Write your Python solution here

```

**Solution Pattern**:
```python
import re
print(re.findall(r'\w*a\w*', 'cat dog apple'))
```

---

### 66. Groups, Alternation & Backreferences [Regex]
### Groups
Use parentheses to capture groups.

**Code Example / Starter**:
```python
m = re.search(r'@(.*)', 'email@gmail.com')

# TODO: Extract the domain from 'email@gmail.com' using `re.search(r'@(.*)', ...)`.
# Write your solution below:

```

**Solution Pattern**:
```python
import re
m = re.search(r'@(.*)', 'email@gmail.com')
print(m.group(1))
```

---

### 67. re.sub() — Search & Replace [Regex]
### Replace
Use `re.sub` to replace patterns.

**Code Example / Starter**:
```python
# Quest: 67. re.sub() — Search & Replace
# Task: Replace all digits in 'A1 B2' with 'X'.

# TODO: Write your Python solution here

```

**Solution Pattern**:
```python
import re
print(re.sub(r'\d', 'X', 'A1 B2'))
```

---
