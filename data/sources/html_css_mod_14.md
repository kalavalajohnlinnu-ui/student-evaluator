# [HTML & CSS] Responsive Web Design
**Description**: Make it look good everywhere.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: HTML & CSS

## Lessons & Concepts Covered:

### 1. Viewport Meta [Responsive]
### Mobile Support
The viewport meta tag is essential for mobile design.

**Code Example / Starter**:
```html_css
<head>
</head>
```

**Solution Pattern**:
```html_css
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

---

### 2. Media Queries [Responsive]
### Breakpoints
Change styles based on screen size with @media.

**Code Example / Starter**:
```html_css
<style>
</style>
```

**Solution Pattern**:
```html_css
<style>
@media (max-width: 600px) { body { background: red; } }
</style>
```

---

### 3. Fluid Units [Responsive]
### rem, vw, vh
Use relative units for responsive text and sizing.

**Code Example / Starter**:
```html_css
<style>
</style>
```

**Solution Pattern**:
```html_css
<style>
.hero { height: 100vh; }
</style>
```

---

### 4. Clamp & Min/Max [Responsive]
### clamp()
Set a minimum, preferred, and maximum size.

**Code Example / Starter**:
```html_css
<style>
</style>
```

**Solution Pattern**:
```html_css
<style>
h1 { font-size: clamp(1rem, 5vw, 3rem); }
</style>
```

---

### 5. Responsive Images [Responsive]
### srcset
Serve different images for different screens.

**Code Example / Starter**:
```html_css
<!-- add img -->
```

**Solution Pattern**:
```html_css
<img src="small.jpg" srcset="large.jpg 1024w, small.jpg 600w" alt="img">
```

---
