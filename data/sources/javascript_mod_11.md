# [JAVASCRIPT] Module 11: OOP with Classes
**Description**: class/constructor/this, extends/super, static/private #, prototypes

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 41. Classes & Constructors [OOP]
### Factories
A class is a blueprint. The `constructor` runs when you create a new instance using `new`.

**Code Example / Starter**:
```javascript
class Hero {
  constructor(name) {
    this.name = name;
  }
}
console.log(new Hero('Batman').name);
```

**Solution Pattern**:
```javascript
class Hero { constructor(name) { this.name = name; } } console.log(new Hero('Batman').name);
```

---

### 42. Methods [OOP]
### Actions
Methods are functions inside a class.

**Code Example / Starter**:
```javascript
class Hero {
  speak() { return "I am Hero"; }
}
console.log(new Hero().speak());
```

**Solution Pattern**:
```javascript
class Hero { speak() { return "I am Hero"; } } console.log(new Hero().speak());
```

---

### 43. Extends & Super [OOP]
### Inheritance
Use `extends` to base a class on another, and `super()` to call the parent's constructor.

**Code Example / Starter**:
```javascript
class Hero { constructor(name) { this.name = name; } }
class Mage extends Hero {
  constructor(name) { super(name); }
}
console.log(new Mage('Merlin').name);
```

**Solution Pattern**:
```javascript
class Hero { constructor(name) { this.name = name; } } class Mage extends Hero { constructor(name) { super(name); } } console.log(new Mage('Merlin').name);
```

---

### 44. Static Methods [OOP]
### Class-Level Methods
Static methods belong to the class itself, not the instances.

**Code Example / Starter**:
```javascript
class Hero {
  static info() { return "Class"; }
}
console.log(Hero.info());
```

**Solution Pattern**:
```javascript
class Hero { static info() { return "Class"; } } console.log(Hero.info());
```

---
