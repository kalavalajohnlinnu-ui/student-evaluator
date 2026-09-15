# [JAVASCRIPT] Module 5: Functions Deep Dive
**Description**: Declaration vs expression vs arrow, default/rest params, callbacks, IIFE

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 18. Function Expressions [Functions]
### Functions as Values
You can save a function inside a variable! `const bark = function() { }`

**Code Example / Starter**:
```javascript
const sayHi = function() {
  console.log("Hi");
};
sayHi();
```

**Solution Pattern**:
```javascript
const sayHi = function() { console.log("Hi"); }; sayHi();
```

---

### 19. Default Parameters [Functions]
### Backups
You can give a parameter a default value if none is passed in.

**Code Example / Starter**:
```javascript
function greet(name = "Guest") {
  console.log(name);
}
greet();
```

**Solution Pattern**:
```javascript
function greet(name = "Guest") { console.log(name); } greet();
```

---

### 20. Rest Parameters [Advanced]
### Gathering Arguments
`...args` collects all extra arguments into an array.

**Code Example / Starter**:
```javascript
function show(...items) {
  console.log(items.length);
}
show(1, 2, 3);
```

**Solution Pattern**:
```javascript
function show(...items) { console.log(items.length); } show(1, 2, 3);
```

---

### 21. Callbacks [Callbacks]
### Passing Functions
A callback is a function you pass to another function to be run later.

**Code Example / Starter**:
```javascript
function runCallback(cb) {
  cb();
}
runCallback(() => console.log("Done"));
```

**Solution Pattern**:
```javascript
function runCallback(cb) { cb(); } runCallback(() => console.log("Done"));
```

---
