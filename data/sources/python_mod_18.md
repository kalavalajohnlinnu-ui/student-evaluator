# [PYTHON] Module 18: File I/O & Serialization
**Description**: Read, write, and serialize data to disk with files, paths, and json.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 55. Reading & Writing Text Files (open(), with) [File I/O]
### File I/O
Use `with open()` to automatically handle closing files. Since we are in a simulated browser, we'll simulate output.

**Code Example / Starter**:
```python
f = io.StringIO('hello')

# TODO: Simulate reading from a file by using `import io`. `f = io.StringIO('hello')`. Print `f.read()`.
# Write your solution below:

```

**Solution Pattern**:
```python
import io
f = io.StringIO('hello')
print(f.read())
```

---

### 56. Reading & Writing CSV files [CSV]
### CSV files
Use the `csv` module.

**Code Example / Starter**:
```python
f = io.StringIO('A,B\n1,2')
reader = csv.reader(f)

# TODO: Simulate reading CSV using `csv.reader` on an `io.StringIO` object.
# Write your solution below:

```

**Solution Pattern**:
```python
import csv, io
f = io.StringIO('A,B\n1,2')
reader = csv.reader(f)
for row in reader: print(','.join(row))
```

---

### 57. JSON Serialization (json.loads, json.dumps) [JSON]
### JSON
`json.dumps` stringifies, `json.loads` parses.

**Code Example / Starter**:
```python
d = json.loads('{"x": 1}')

# TODO: Parse `{"x": 1}` using `json.loads` and print the `x` value.
# Write your solution below:

```

**Solution Pattern**:
```python
import json
d = json.loads('{"x": 1}')
print(d['x'])
```

---

### 58. Working with File Paths (pathlib.Path) [Pathlib]
### pathlib
`pathlib.Path` makes path joining and checking easy.

**Code Example / Starter**:
```python
p = Path('folder') / 'file.txt'

# TODO: Create a `Path('folder') / 'file.txt'` and print it.
# Write your solution below:

```

**Solution Pattern**:
```python
from pathlib import Path
p = Path('folder') / 'file.txt'
print(p.as_posix())
```

---
