# [JAVASCRIPT] Module 4: Loops & Iteration
**Description**: for, while, do...while, for...of, for...in, break/continue

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 14. The For Loop [Loops]
### Doing Things Repeatedly
A `for` loop has a start, an end condition, and a step. `for(let i = 0; i < 3; i++)` runs 3 times.

**Code Example / Starter**:
```javascript
for(let i = 1; i <= 3; i++) {
  console.log(i);
}
```

**Solution Pattern**:
```javascript
for(let i = 1; i <= 3; i++) { console.log(i); }
```

---

### 15. The While Loop [Loops]
### While True
A `while` loop runs as long as a condition is true.

**Code Example / Starter**:
```javascript
let count = 3;
while(count > 0) {
  console.log(count);
  count--;
}
```

**Solution Pattern**:
```javascript
let count = 3; while(count > 0) { console.log(count); count--; }
```

---

### 16. For...of Loop [Arrays]
### Loop through Arrays
`for(let item of array)` goes through every item in a list without needing a counter.

**Code Example / Starter**:
```javascript
const letters = ['A', 'B'];
for(let l of letters) {
  console.log(l);
}
```

**Solution Pattern**:
```javascript
const letters = ['A', 'B']; for(let l of letters) { console.log(l); }
```

---

### 17. Break & Continue [Control]
### Stop and Skip
`break` stops a loop entirely. `continue` skips the rest of the current turn and moves to the next.

**Code Example / Starter**:
```javascript
for(let i=1; i<=3; i++) {
  if(i === 2) continue;
  console.log(i);
}
```

**Solution Pattern**:
```javascript
for(let i=1; i<=3; i++) { if(i === 2) continue; console.log(i); }
```

---
