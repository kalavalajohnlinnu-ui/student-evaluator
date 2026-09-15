# [JAVASCRIPT] Module 8: Higher-Order Array Methods
**Description**: map, filter, reduce, find/some/every, sort/flat/chaining

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 29. Array Map [Arrays]
### Transforming Arrays
`map` runs a function on every item and returns a new array with the results.

**Code Example / Starter**:
```javascript
const nums = [1, 2, 3];
const doubled = nums.map(n => n * 2);
console.log(doubled);
```

**Solution Pattern**:
```javascript
const nums = [1, 2, 3]; const doubled = nums.map(n => n * 2); console.log(doubled);
```

---

### 30. Array Filter [Arrays]
### Filtering Arrays
`filter` keeps only the items that pass a test.

**Code Example / Starter**:
```javascript
const nums = [1, 2, 3, 4];
const big = nums.filter(n => n > 2);
console.log(big);
```

**Solution Pattern**:
```javascript
const nums = [1, 2, 3, 4]; const big = nums.filter(n => n > 2); console.log(big);
```

---

### 31. Array Reduce [Arrays]
### Reducing Arrays
`reduce` combines all items into a single value, like a sum.

**Code Example / Starter**:
```javascript
const sum = [1, 2, 3].reduce((acc, n) => acc + n, 0);
console.log(sum);
```

**Solution Pattern**:
```javascript
const sum = [1, 2, 3].reduce((acc, n) => acc + n, 0); console.log(sum);
```

---

### 32. Find & Some [Arrays]
### Searching
`find` gets the first match. `some` checks if *any* match exists.

**Code Example / Starter**:
```javascript
const match = [10, 20, 30].find(n => n === 20);
console.log(match);
```

**Solution Pattern**:
```javascript
const match = [10, 20, 30].find(n => n === 20); console.log(match);
```

---

### 33. Chaining Methods [Advanced]
### Combo Moves
You can string methods together! `.filter().map()`

**Code Example / Starter**:
```javascript
const res = [1, 2, 3].filter(n => n > 1).map(n => n * 10);
console.log(res);
```

**Solution Pattern**:
```javascript
const res = [1, 2, 3].filter(n => n > 1).map(n => n * 10); console.log(res);
```

---
