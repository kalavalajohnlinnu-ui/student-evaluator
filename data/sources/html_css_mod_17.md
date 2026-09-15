# [HTML & CSS] CSS Animations
**Description**: Create complex motion.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: HTML & CSS

## Lessons & Concepts Covered:

### 1. Keyframes [Animations]
### @keyframes
Define custom animations step-by-step.

**Code Example / Starter**:
```html_css
<!-- Quest: 1. Keyframes -->
<!-- TODO: Create a bounce animation. -->
<div class="container">
  
</div>

```

**Solution Pattern**:
```html_css
<style>
@keyframes bounce { 0% { top: 0; } 100% { top: 10px; } }
</style>
```

---

### 2. Animation Shorthand [Animations]
### Applying Animations
Apply keyframes to an element.

**Code Example / Starter**:
```html_css
<!-- Quest: 2. Animation Shorthand -->
<!-- TODO: Apply bounce animation. -->
<div class="container">
  
</div>

```

**Solution Pattern**:
```html_css
<style>
.box { animation: bounce 1s infinite; }
</style>
```

---

### 3. Multi-step Animations [Animations]
### Percentages
Add more steps using 50%, 75% etc.

**Code Example / Starter**:
```html_css
<!-- Quest: 3. Multi-step Animations -->
<!-- TODO: Add a 50% step. -->
<div class="container">
  
</div>

```

**Solution Pattern**:
```html_css
<style>
@keyframes bounce { 0% {} 50% { top: 20px; } 100% {} }
</style>
```

---

### 4. Performance [Animations]
### will-change
Optimize animations for smooth rendering.

**Code Example / Starter**:
```html_css
<!-- Quest: 4. Performance -->
<!-- TODO: Use will-change. -->
<div class="container">
  
</div>

```

**Solution Pattern**:
```html_css
<style>
.box { will-change: transform; }
</style>
```

---
