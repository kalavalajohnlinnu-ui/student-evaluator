# [JAVASCRIPT] Module 6: Objects & JSON
**Description**: Object literals, dot/bracket notation, Object.keys/values/entries, JSON.stringify/parse

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 22. Object Literals [Objects]
### Data Containers
Objects hold data using keys and values. `const car = { color: 'red' }`.

**Code Example / Starter**:
```javascript
const player = { name: 'Hero', score: 100 };
console.log(player.name);
```

**Solution Pattern**:
```javascript
const player = { name: 'Hero', score: 100 }; console.log(player.name);
```

---

### 23. Bracket Notation [Objects]
### Dynamic Keys
You can access object properties using brackets `[]` instead of a dot. Useful when keys have spaces!

**Code Example / Starter**:
```javascript
const player = { score: 100 };
console.log(player['score']);
```

**Solution Pattern**:
```javascript
const player = { score: 100 }; console.log(player['score']);
```

---

### 24. Object Methods [Objects]
### Getting Keys
`Object.keys(obj)` returns an array of all the keys in an object.

**Code Example / Starter**:
```javascript
const obj = { a: 1, b: 2 };
console.log(Object.keys(obj));
```

**Solution Pattern**:
```javascript
const obj = { a: 1, b: 2 }; console.log(Object.keys(obj));
```

---

### 25. JSON [Data]
### Stringifying
JSON is a text format for objects. `JSON.stringify(obj)` turns an object into a JSON string.

**Code Example / Starter**:
```javascript
const bot = { name: 'Bot' };
console.log(JSON.stringify(bot));
```

**Solution Pattern**:
```javascript
const bot = { name: 'Bot' }; console.log(JSON.stringify(bot));
```

---
