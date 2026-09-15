# [JAVASCRIPT] Module 20: Functional Programming
**Description**: Pure functions, currying, composition/pipe

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 75. Pure Functions [FP]
### No Side Effects
Pure functions always return the same result for the same input and don't change outside variables.

**Code Example / Starter**:
```javascript
const add = (a, b) => a + b;
console.log(add(2, 2));
```

**Solution Pattern**:
```javascript
const add = (a, b) => a + b; console.log(add(2, 2));
```

---

### 76. Currying [FP]
### Russian Dolls
Currying turns `f(a, b)` into `f(a)(b)`. `const add = a => b => a + b;`

**Code Example / Starter**:
```javascript
const add = a => b => a + b;
console.log(add(2)(3));
```

**Solution Pattern**:
```javascript
const add = a => b => a + b; console.log(add(2)(3));
```

---

### 77. Composition [FP]
### Piping
Composition is combining multiple functions to create a new one.

**Code Example / Starter**:
```javascript
// Quest: 77. Composition
// TODO: Write your JavaScript solution here

```

**Solution Pattern**:
```javascript
console.log("Composed");
```

---
