# [JAVASCRIPT] Module 15: Async/Await & Fetch
**Description**: async/await, try/catch with await, fetch API, Promise.all/race

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 58. Async / Await [Modern Async]
### Pausing Code
`await` pauses a function until a Promise finishes! Must be inside an `async` function.

**Code Example / Starter**:
```javascript
(async () => {
  let res = await Promise.resolve('Awaited');
  console.log(res);
})();
```

**Solution Pattern**:
```javascript
(async () => { let res = await Promise.resolve('Awaited'); console.log(res); })();
```

---

### 59. Fetch API [Network]
### Getting Data
`fetch()` grabs data from the internet. (Simulated)

**Code Example / Starter**:
```javascript
// Quest: 59. Fetch API
// TODO: Write your JavaScript solution here

```

**Solution Pattern**:
```javascript
console.log("Fetched!");
```

---

### 60. Promise.all [Advanced]
### Doing it all at once
`Promise.all([p1, p2])` waits for all promises to finish.

**Code Example / Starter**:
```javascript
(async () => {
  const res = await Promise.all([Promise.resolve(1), Promise.resolve(2)]);
  console.log(res.length);
})();
```

**Solution Pattern**:
```javascript
(async () => { const res = await Promise.all([Promise.resolve(1), Promise.resolve(2)]); console.log(res.length); })();
```

---

### 61. Promise.race [Advanced]
### The Winner
`Promise.race()` takes an array of promises and resolves with the first one to finish.

**Code Example / Starter**:
```javascript
// Quest: 61. Promise.race
// TODO: Write your JavaScript solution here

```

**Solution Pattern**:
```javascript
console.log("Raced!");
```

---
