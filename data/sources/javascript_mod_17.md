# [JAVASCRIPT] Module 17: Regular Expressions
**Description**: Creating RegExp, test/match/replace, groups/lookaheads

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 65. RegExp test [Regex]
### Pattern Matching
`/hello/.test('hello world')` checks if 'hello' is in the string.

**Code Example / Starter**:
```javascript
// Quest: 65. RegExp test
// TODO: Write your JavaScript solution here

```

**Solution Pattern**:
```javascript
console.log(/abc/.test("xabcy"));
```

---

### 66. String match [Regex]
### Finding Matches
`'hello'.match(/e/)` returns info about where the match happened.

**Code Example / Starter**:
```javascript
// Quest: 66. String match
// TODO: Write your JavaScript solution here

```

**Solution Pattern**:
```javascript
console.log("abc123def".match(/[0-9]+/)[0]);
```

---

### 67. String replace [Regex]
### Replacing
`'cat'.replace(/a/, 'o')` returns 'cot'.

**Code Example / Starter**:
```javascript
// Quest: 67. String replace
// TODO: Write your JavaScript solution here

```

**Solution Pattern**:
```javascript
console.log("bad dog".replace(/bad/, "good"));
```

---
