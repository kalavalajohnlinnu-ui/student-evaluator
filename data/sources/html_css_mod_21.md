# [HTML & CSS] Modern CSS Features
**Description**: Use cutting-edge CSS.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: HTML & CSS

## Lessons & Concepts Covered:

### 1. Container Queries [Modern CSS]
### @container
Style elements based on container size, not viewport size.

**Code Example / Starter**:
```html_css
<!-- Quest: 1. Container Queries -->
<!-- TODO: Define a container. -->
<div class="container">
  
</div>

```

**Solution Pattern**:
```html_css
<style>
.wrap { container-type: inline-size; }
</style>
```

---

### 2. CSS Nesting [Modern CSS]
### Nesting
Write CSS selectors inside each other natively.

**Code Example / Starter**:
```html_css
<!-- Quest: 2. CSS Nesting -->
<!-- TODO: Nest a p inside .card. -->
<div class="container">
  
</div>

```

**Solution Pattern**:
```html_css
<style>
.card { & p { color: red; } }
</style>
```

---

### 3. :has() Selector [Modern CSS]
### Parent Selector
Target an element if it contains a specific child.

**Code Example / Starter**:
```html_css
<!-- Quest: 3. :has() Selector -->
<!-- TODO: Style div if it has an img. -->
<div class="container">
  
</div>

```

**Solution Pattern**:
```html_css
<style>
div:has(img) { border: 1px solid black; }
</style>
```

---

### 4. Scroll Animations [Modern CSS]
### Scroll-timeline
Animate based on scroll position.

**Code Example / Starter**:
```html_css
<!-- Quest: 4. Scroll Animations -->
<!-- TODO: Add animation-timeline. -->
<div class="container">
  
</div>

```

**Solution Pattern**:
```html_css
<style>
.box { animation-timeline: scroll(); }
</style>
```

---
