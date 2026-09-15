# [PYTHON] Module 14: Decorators & Closures
**Description**: Master closures and decorators to wrap and modify functions dynamically.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 41. Closures — functions that remember their environment [Closures]
### Closures
A closure is an inner function that remembers the state of its enclosing environment.

**Code Example / Starter**:
```python
def multiplier(factor):
    # TODO: Write your code to solve the challenge:
    pass

print(multiplier(3)(5))

```

**Solution Pattern**:
```python
def multiplier(factor):
    def inner(n):
        return n * factor
    return inner
print(multiplier(3)(5))
```

---

### 42. Writing Function Decorators @decorator [Decorators]
### Decorators
A decorator is a function that modifies another function, applied with `@`.

**Code Example / Starter**:
```python
def uppercase(func):
    # TODO: Write your code to solve the challenge:
    pass

@uppercase
def greet(): return 'hello'
print(greet())

```

**Solution Pattern**:
```python
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet(): return 'hello'
print(greet())
```

---

### 43. Decorators with Arguments & Stacking [Decorators]
### Advanced Decorators
You can stack decorators and use `*args, **kwargs` to pass arguments.

**Code Example / Starter**:
```python
def add_stars(func):
    # TODO: Write your code to solve the challenge:
    pass

@add_stars
def echo(msg): return msg
print(echo('wow'))

```

**Solution Pattern**:
```python
def add_stars(func):
    def wrapper(*args):
        return '***' + func(*args) + '***'
    return wrapper
@add_stars
def echo(msg): return msg
print(echo('wow'))
```

---
