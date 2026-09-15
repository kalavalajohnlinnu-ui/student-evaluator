# [PYTHON] Module 7: Functions & Modular Code
**Description**: Write reusable logic with def, understand parameters vs arguments, return values, and scope.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 19. Defining Functions [Reusability]
### Functions: Reusable Recipes
Instead of repeating code, package it into a function with the **`def`** keyword:

```python
def greet(name):
    return "Hello, " + name + "!"

# Calling the function
message = greet("Maya")
print(message)  # "Hello, Maya!"
```

#### Key Concepts:
- **Parameter**: The placeholder variable in definition (`name`).
- **Argument**: The actual value passed in (`"Maya"`).
- **`return`**: Sends the computed result back to the caller.

**Code Example / Starter**:
```python
# Define square function:
def square(n):
    # return the square of n
    pass

result = square(7)
print(result)

```

**Solution Pattern**:
```python
def square(n):
    return n * n

result = square(7)
print(result)
```

---

### 20. Default Parameters [Clean APIs]
### Default Parameter Values
You can supply fallback default values for function parameters:

```python
def make_coffee(size="Medium", milk=True):
    return f"{size} coffee with {'milk' if milk else 'no milk'}"

print(make_coffee())                # Uses defaults: 'Medium coffee with milk'
print(make_coffee(size="Large"))    # Overrides size
```

**Code Example / Starter**:
```python
# Define function with default tax_rate:
def calc_total(subtotal, tax_rate=0.10):
    pass

total_with_default = calc_total(100)
print(total_with_default)

```

**Solution Pattern**:
```python
def calc_total(subtotal, tax_rate=0.10):
    return subtotal + (subtotal * tax_rate)

total_with_default = calc_total(100)
print(total_with_default)
```

---

### 21. Variable Scope: Local vs Global [Architecture]
### Variable Scope
Where a variable is created determines where it can be seen:

- **Local Scope**: Variables created *inside* a function exist only during that function's execution.
- **Global Scope**: Variables created in the main script are accessible everywhere.

```python
global_var = 100

def my_func():
    local_var = 20
    print(global_var)  # Works!

# print(local_var)     # ERROR! NameError: name 'local_var' is not defined
```

**Code Example / Starter**:
```python
base_salary = 50000

def get_bonus(salary):
    bonus = salary * 0.15
    return bonus

# Call get_bonus with base_salary and assign to final_bonus:
final_bonus = 

print(final_bonus)

```

**Solution Pattern**:
```python
base_salary = 50000
def get_bonus(salary):
    bonus = salary * 0.15
    return bonus

final_bonus = get_bonus(base_salary)
print(final_bonus)
```

---
