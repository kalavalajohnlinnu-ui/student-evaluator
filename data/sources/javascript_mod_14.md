# [JAVASCRIPT] Module 14: Async & Promises
**Description**: Event loop, callback hell, Promise .then/.catch, creating Promises

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 54. Event Loop [Async]
### Non-Blocking
JS handles heavy tasks in the background and continues running the rest of the code.

**Code Example / Starter**:
```javascript
console.log("Start");
console.log("End");
```

**Solution Pattern**:
```javascript
console.log("Start"); console.log("End");
```

---

### 55. Creating Promises [Async]
### I Promise
A Promise represents a future value. `new Promise((resolve, reject) => ...)`.

**Code Example / Starter**:
```javascript
// Quest: 55. Creating Promises
// TODO: Write your JavaScript solution here

```

**Solution Pattern**:
```javascript
Promise.resolve("Done").then(console.log);
```

---

### 56. Promise Chaining [Async]
### Step by Step
You can return a value in a `.then()` and catch it in the next `.then()`.

**Code Example / Starter**:
```javascript
// Quest: 56. Promise Chaining
// TODO: Write your JavaScript solution here

```

**Solution Pattern**:
```javascript
Promise.resolve(1).then(v => v + 1).then(console.log);
```

---

### 57. Catching Errors [Async]
### Oops
Use `.catch()` to handle Promise rejections.

**Code Example / Starter**:
```javascript
// Quest: 57. Catching Errors
// TODO: Write your JavaScript solution here

```

**Solution Pattern**:
```javascript
Promise.reject("Error").catch(console.log);
```

---
