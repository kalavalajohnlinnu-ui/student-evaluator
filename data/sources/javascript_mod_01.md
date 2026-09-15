# [JAVASCRIPT] Realm 1: The Spark of the Web
**Description**: Master console output, variables with let and const, and template strings.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: JavaScript

## Lessons & Concepts Covered:

### 1. Hello, JavaScript! [Web Basics]
### Welcome to JavaScript! ⚡
JavaScript is the programming language that powers every interactive website on the planet.

In JavaScript, we use **`console.log()`** to print messages to the console.

```javascript
console.log("Hello, Web Hero!");
```

Unlike Python, JavaScript uses parentheses `()` and usually ends lines with a semicolon `;`.

**Code Example / Starter**:
```javascript
// Write your code below and click Run Spell:
console.log("Hello, World!");

```

**Solution Pattern**:
```javascript
console.log("Welcome to JavaScript Hero!");
```

---

### 2. Variables: let vs const [Storage]
### Storing Values in JavaScript
In modern JavaScript, we create variables using:
- **`let`**: When a value can change later (`let score = 0; score = 10;`).
- **`const`**: For constants that never change (`const maxLives = 3;`).

```javascript
let heroName = "Sparky";
let coins = 50;
const level = 1;

console.log(heroName);
console.log(coins);
```

**Code Example / Starter**:
```javascript
// Declare heroName and power:
let heroName = "";
let power = 0;

console.log(heroName);
console.log(power);

```

**Solution Pattern**:
```javascript
let heroName = "Volt";
let power = 900;
console.log(heroName);
console.log(power);
```

---

### 3. Template Literals (`${}`) [String Magic]
### Backticks & Template Literals
Instead of clunky `+` signs, JavaScript lets you combine strings easily with backticks `` ` `` and `${variable}`:

```javascript
const player = "Alex";
const score = 450;

console.log(`Hero ${player} has ${score} points!`);
```

**Code Example / Starter**:
```javascript
const hero = "Sparky";
const gems = 15;

// Use template literals:
console.log(``);

```

**Solution Pattern**:
```javascript
const hero = "Sparky";
const gems = 15;
console.log(`${hero} collected ${gems} gems!`);
```

---

### 4. Decision Making (if / else & ===) [Logic]
### If Statements in JavaScript
In JavaScript, we use triple equals **`===`** for strict equality:

```javascript
let health = 0;

if (health > 0) {
  console.log("Still fighting!");
} else {
  console.log("Game Over!");
}
```

**Code Example / Starter**:
```javascript
let mana = 50;

// Add if / else:
if (mana >= 30) {
  
} else {
  
}

```

**Solution Pattern**:
```javascript
let mana = 50;
if (mana >= 30) {
  console.log("Spell ready!");
} else {
  console.log("Need mana.");
}
```

---

### 5. Arrays & Push / Pop [Collections]
### JavaScript Arrays `[]`
An array is a list of items:

```javascript
const inventory = ["Sword", "Shield"];
inventory.push("Magic Wand"); // Adds to end
console.log(inventory[0]); // 'Sword'
console.log(inventory.length); // 3
```

**Code Example / Starter**:
```javascript
const team = ["Pikachu", "Charmander"];

// Push Squirtle and print length:


```

**Solution Pattern**:
```javascript
const team = ["Pikachu", "Charmander"];
team.push("Squirtle");
console.log(team.length);
```

---

### 6. Arrow Functions [Modern JS]
### Modern Arrow Functions `=>`
Arrow functions are clean and concise ways to write functions:

```javascript
const double = (n) => n * 2;
console.log(double(5)); // 10
```

**Code Example / Starter**:
```javascript
// Create arrow function add:
const add = (a, b) => 

console.log(add(10, 20));

```

**Solution Pattern**:
```javascript
const add = (a, b) => a + b;
console.log(add(10, 20));
```

---
