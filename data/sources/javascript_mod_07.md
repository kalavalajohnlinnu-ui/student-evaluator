# [JAVASCRIPT] Module 7: Destructuring & Spread
**Description**: Array destructuring, object destructuring, spread operator

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 26. Array Destructuring [Modern JS]
### Unpacking Arrays
Extract values easily: `const [a, b] = [1, 2]` assigns 1 to a and 2 to b.

**Code Example / Starter**:
```javascript
const [first, second] = [10, 20];
console.log(first);
```

**Solution Pattern**:
```javascript
const [first, second] = [10, 20]; console.log(first);
```

---

### 27. Object Destructuring [Modern JS]
### Unpacking Objects
Extract properties: `const { name } = { name: 'Hero' }` assigns 'Hero' to name.

**Code Example / Starter**:
```javascript
const { age } = { age: 12, name: 'Alex' };
console.log(age);
```

**Solution Pattern**:
```javascript
const { age } = { age: 12, name: 'Alex' }; console.log(age);
```

---

### 28. Spread Operator [Modern JS]
### Spreading Values
The spread operator `...` unpacks elements. `[...arr1, ...arr2]` combines arrays.

**Code Example / Starter**:
```javascript
const arr1 = [1, 2];
const arr2 = [3, 4];
const combined = [...arr1, ...arr2];
console.log(combined.length);
```

**Solution Pattern**:
```javascript
const arr1 = [1, 2]; const arr2 = [3, 4]; const combined = [...arr1, ...arr2]; console.log(combined.length);
```

---
