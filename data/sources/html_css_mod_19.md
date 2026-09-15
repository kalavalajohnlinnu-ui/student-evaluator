# [HTML & CSS] Accessibility
**Description**: Make web for everyone.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: HTML & CSS

## Lessons & Concepts Covered:

### 1. Contrast [Accessibility]
### WCAG Contrast
Make sure text is readable against its background.

**Code Example / Starter**:
```html_css
<!-- Quest: 1. Contrast -->
<!-- TODO: Use high contrast colors. -->
<div class="container">
  
</div>

```

**Solution Pattern**:
```html_css
<style>
.text { color: black; background: white; }
</style>
```

---

### 2. ARIA Labels [Accessibility]
### Screen Readers
Provide extra context with aria-label.

**Code Example / Starter**:
```html_css
<!-- Quest: 2. ARIA Labels -->
<!-- TODO: Add aria-label to button. -->
<div class="container">
  
</div>

```

**Solution Pattern**:
```html_css
<button aria-label="Close Menu">X</button>
```

---

### 3. Keyboard Navigation [Accessibility]
### Focus
Style the :focus state for keyboard users.

**Code Example / Starter**:
```html_css
<!-- Quest: 3. Keyboard Navigation -->
<!-- TODO: Add a focus outline. -->
<div class="container">
  
</div>

```

**Solution Pattern**:
```html_css
<style>
button:focus { outline: 2px solid blue; }
</style>
```

---

### 4. Alt Text [Accessibility]
### Describing Images
Always use meaningful alt text for images.

**Code Example / Starter**:
```html_css
<!-- Quest: 4. Alt Text -->
<!-- TODO: Add descriptive alt text. -->
<div class="container">
  
</div>

```

**Solution Pattern**:
```html_css
<img src="dog.jpg" alt="A brown dog running">
```

---
