# [PYTHON] Module 4: Repetition & Loops
**Description**: Automate repetitive tasks with while and for loops, range(), and loop control statements.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 10. The while Loop [Iteration]
### Repeating While a Condition is True
A **`while`** loop keeps executing its block as long as its condition remains True.

```python
count = 1
while count <= 3:
    print("Count is:", count)
    count = count + 1  # Or count += 1
```

> ⚠️ **Caution:** Always ensure the loop variable changes toward the exit condition, otherwise you create an **infinite loop**!

**Code Example / Starter**:
```python
count = 3

# Write the while loop:


print("Blastoff!")

```

**Solution Pattern**:
```python
count = 3
while count >= 1:
    print(count)
    count -= 1
print("Blastoff!")
```

---

### 11. The for Loop & range() [Core Loop]
### Iterating with for and range()
The **`for`** loop is Python's most common loop. The **`range()`** function generates a sequence of numbers:

- `range(5)` ➔ 0, 1, 2, 3, 4 (starts at 0, stops before 5)
- `range(1, 6)` ➔ 1, 2, 3, 4, 5 (from 1 up to 6)
- `range(2, 11, 2)` ➔ 2, 4, 6, 8, 10 (start, stop, step!)

```python
# Summing numbers
total = 0
for i in range(1, 5):
    total += i
print(total) # 1 + 2 + 3 + 4 = 10
```

**Code Example / Starter**:
```python
total_sum = 0

# Use a for loop with range(1, 11) to add each number to total_sum:


print(total_sum)

```

**Solution Pattern**:
```python
total_sum = 0
for num in range(1, 11):
    total_sum += num
print(total_sum)
```

---

### 12. Loop Controls: break & continue [Control Flow]
### Controlling Loop Flow
Sometimes you need to alter a loop's normal flow:

1. **`break`**: Immediately terminates the entire loop.
2. **`continue`**: Skips the rest of the current iteration and jumps to the next one.

```python
# Example of break:
for num in range(1, 10):
    if num == 4:
        break  # Stops completely when num hits 4
    print(num)  # Prints 1, 2, 3

# Example of continue:
for num in range(1, 5):
    if num == 3:
        continue  # Skips 3
    print(num)  # Prints 1, 2, 4
```

**Code Example / Starter**:
```python
numbers = [10, 20, -5, 30, -1, 40]
positive_sum = 0

for n in numbers:
    # Add continue condition:
    
    positive_sum += n

print(positive_sum)

```

**Solution Pattern**:
```python
numbers = [10, 20, -5, 30, -1, 40]
positive_sum = 0
for n in numbers:
    if n < 0:
        continue
    positive_sum += n
print(positive_sum)
```

---
