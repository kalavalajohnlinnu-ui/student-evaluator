# [PYTHON] Module 12: Lambda & Functional Programming
**Description**: Learn anonymous functions and functional tools like map, filter, and reduce.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 33. Lambda Expressions [Functional]
### Anonymous Functions with lambda
A lambda is a small, one-line function without a name.

```python
# Normal function
def add(x, y): return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y
print(add_lambda(5, 3))  # 8
```

**Code Example / Starter**:
```python
times_ten = lambda x: 
result = times_ten(5)
print(result)

```

**Solution Pattern**:
```python
times_ten = lambda x: x * 10
result = times_ten(5)
print(result)
```

---

### 34. map() — transform every item [Functional]
### Transforming Lists with map()
`map()` applies a function to every item in a collection.

```python
nums = [1, 2, 3]
doubled = list(map(lambda x: x * 2, nums))
```

**Code Example / Starter**:
```python
scores = [10, 20, 30]

# TODO: Use `map()` and a lambda to subtract 1 from every number in `scores = [10, 20, 30]`. Store in `adjusted`.
# Write your solution below:

```

**Solution Pattern**:
```python
scores = [10, 20, 30]
adjusted = list(map(lambda x: x - 1, scores))
print(adjusted)
```

---

### 35. filter() — pick items that pass a test [Functional]
### Filtering Lists with filter()
`filter()` keeps only items where the function returns True.

```python
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
```

**Code Example / Starter**:
```python
words = ['cat', 'apple', 'dog', 'banana']

# TODO: Use `filter()` to keep only words longer than 3 letters in `words = ['cat', 'apple', 'dog', 'banana']`.
# Write your solution below:

```

**Solution Pattern**:
```python
words = ['cat', 'apple', 'dog', 'banana']
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)
```

---

### 36. reduce() from functools [Functional]
### Accumulating with reduce()
`reduce()` repeatedly applies a function to combine elements into a single value.

```python
from functools import reduce
nums = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, nums)
```

**Code Example / Starter**:
```python
nums = [1, 2, 3, 4, 5]

# TODO: Use `reduce()` to find the product of all numbers in `nums = [1, 2, 3, 4, 5]`.
# Write your solution below:

```

**Solution Pattern**:
```python
from functools import reduce
nums = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, nums)
print(product)
```

---
