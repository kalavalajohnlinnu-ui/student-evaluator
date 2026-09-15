# [PYTHON] Module 8: Bulletproofing Code - Error Handling
**Description**: Catch and handle exceptions gracefully with try, except, finally, and understand tracebacks.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 22. Handling Exceptions (try & except) [Robustness]
### Preventing Crashes with try & except
When Python encounters an error, it raises an **Exception**. If uncaught, your program terminates immediately!

```python
try:
    number = int("not_a_number")
except ValueError:
    print("That was not a valid number!")
```

Common Built-in Exceptions:
- `ZeroDivisionError`: Dividing by zero
- `ValueError`: Right type, inappropriate value (e.g. `int("abc")`)
- `IndexError`: List index out of bounds
- `KeyError`: Dictionary key not found

**Code Example / Starter**:
```python
a = 10
b = 0
result = ""

# Write try-except block here:


print(result)

```

**Solution Pattern**:
```python
a = 10
b = 0
try:
    result = a / b
except ZeroDivisionError:
    result = "Cannot divide by zero"
print(result)
```

---

### 23. else, finally & Raising Errors [Defensive Coding]
### Complete Error Handling
- **`else`**: Runs ONLY if NO exceptions occurred in `try`.
- **`finally`**: ALWAYS runs no matter what (great for cleaning up connections or files).
- **`raise`**: Manually triggers an exception.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age
```

**Code Example / Starter**:
```python
settings = {"theme": "dark"}
status = ""

# Use try...except KeyError:
try:
    val = settings["missing_key"]
except KeyError:
    status = "Default fallback applied"

print(status)

```

**Solution Pattern**:
```python
settings = {"theme": "dark"}
try:
    val = settings["missing_key"]
except KeyError:
    status = "Default fallback applied"
print(status)
```

---
