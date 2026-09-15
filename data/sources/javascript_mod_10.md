# [JAVASCRIPT] Module 10: Error Handling
**Description**: try/catch/finally, throw, defensive programming

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 38. Try/Catch [Safety]
### Safety Nets
Use `try` to run code that might fail, and `catch` to handle errors without crashing.

**Code Example / Starter**:
```javascript
try {
  unknownFunction();
} catch (e) {
  console.log("Caught it!");
}
```

**Solution Pattern**:
```javascript
try { unknownFunction(); } catch (e) { console.log("Caught it!"); }
```

---

### 39. Throwing Errors [Safety]
### Raising Flags
Use `throw new Error('msg')` to create your own errors.

**Code Example / Starter**:
```javascript
try {
  throw new Error("Bad");
} catch (e) {
  console.log(e.message);
}
```

**Solution Pattern**:
```javascript
try { throw new Error("Bad"); } catch (e) { console.log(e.message); }
```

---

### 40. Finally [Safety]
### Always Runs
`finally` block runs whether there was an error or not.

**Code Example / Starter**:
```javascript
// Quest: 40. Finally
// TODO: Write your JavaScript solution here

```

**Solution Pattern**:
```javascript
try { } catch(e) {} finally { console.log("Done"); }
```

---
