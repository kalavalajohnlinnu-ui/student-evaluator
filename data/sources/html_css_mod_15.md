# [HTML & CSS] CSS Variables
**Description**: Write smarter CSS.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: HTML & CSS

## Lessons & Concepts Covered:

### 1. Declaring Variables [CSS]
### Custom Properties
Store colors in variables using --name.

**Code Example / Starter**:
```html_css
<style>
:root {
}
</style>
```

**Solution Pattern**:
```html_css
<style>
:root { --main-color: blue; }
</style>
```

---

### 2. Using var() [CSS]
### Using Variables
Use the var() function to apply your variables.

**Code Example / Starter**:
```html_css
<style>
p {
}
</style>
```

**Solution Pattern**:
```html_css
<style>
p { color: var(--main-color); }
</style>
```

---

### 3. Theming [CSS]
### Dark Mode
Change variable values in media queries for dark mode.

**Code Example / Starter**:
```html_css
<style>
@media (prefers-color-scheme: dark) {
}
</style>
```

**Solution Pattern**:
```html_css
<style>
@media (prefers-color-scheme: dark) { :root { --main-color: black; } }
</style>
```

---
