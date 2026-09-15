# [JAVASCRIPT] Module 9: Scope, Hoisting & Closures
**Description**: Block vs function scope, hoisting, closures, practical closures

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 34. Block Scope [Scope]
### Variable Visibility
Variables made with `let` inside `{ }` are locked in there!

**Code Example / Starter**:
```javascript
{
  let x = 5;
}
console.log(typeof x);
```

**Solution Pattern**:
```javascript
{ let x = 5; } console.log(typeof x);
```

---

### 35. Closures [Advanced]
### Backpacks
A closure is a function that remembers its outer variables even after it is returned.

**Code Example / Starter**:
```javascript
function makeHello() {
  return () => 'Hello';
}
console.log(makeHello()());
```

**Solution Pattern**:
```javascript
function makeHello() { return () => 'Hello'; } console.log(makeHello()());
```

---

### 36. Practical Closures [Advanced]
### Using Closures
You can make private counters using closures.

**Code Example / Starter**:
```javascript
function counter() {
  let c = 0;
  return () => ++c;
}
const next = counter();
console.log(next());
```

**Solution Pattern**:
```javascript
function counter() { let c = 0; return () => ++c; } const next = counter(); console.log(next());
```

---

### 37. Hoisting [Theory]
### Floating Up
Function declarations are 'hoisted' (moved) to the top of the file, so you can call them before you define them.

**Code Example / Starter**:
```javascript
sayBoo();
function sayBoo() { console.log('Boo!'); }
```

**Solution Pattern**:
```javascript
sayBoo(); function sayBoo() { console.log('Boo!'); }
```

---
