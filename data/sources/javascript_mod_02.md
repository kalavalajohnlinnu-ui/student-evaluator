# [JAVASCRIPT] Module 2: Data Types & Type Coercion
**Description**: Primitive types, typeof, truthy/falsy, == vs ===, explicit conversions

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 7. Primitive Types [Core]
### Types of Toys
JavaScript has different types of values. Just like toy cars are different from stuffed animals, strings (words) are different from numbers.

Use `typeof` to find out what type a value is!

**Code Example / Starter**:
```javascript
// Quest: 7. Primitive Types
// TODO: Write your JavaScript solution here

```

**Solution Pattern**:
```javascript
console.log(typeof "Hero");
```

---

### 8. Truthy & Falsy [Logic]
### Truthy & Falsy
Some values act like 'false' even if they aren't the word false. `0`, `""`, and `null` are falsy. Almost everything else is truthy!

**Code Example / Starter**:
```javascript
if (0) {
  console.log("Yes");
} else {
  console.log("No");
}
```

**Solution Pattern**:
```javascript
if (0) { console.log("Yes"); } else { console.log("No"); }
```

---

### 9. == vs === [Core]
### Strict Equality
`==` compares values loosely (`"5" == 5` is true), but `===` compares strictly (types must match too!). Always use `===`!

**Code Example / Starter**:
```javascript
// Quest: 9. == vs ===
// TODO: Write your JavaScript solution here

```

**Solution Pattern**:
```javascript
console.log("5" === 5);
```

---

### 10. Explicit Conversions [Core]
### Changing Types
You can force a string into a number using `Number("5")` or a number into a string using `String(5)`.

**Code Example / Starter**:
```javascript
let num = Number("10");
console.log(typeof num);
```

**Solution Pattern**:
```javascript
let num = Number("10"); console.log(typeof num);
```

---
