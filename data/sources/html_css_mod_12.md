# [HTML & CSS] CSS Grid Layout
**Description**: Master 2D layouts.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: HTML & CSS

## Lessons & Concepts Covered:

### 1. Display Grid [Grid]
### CSS Grid
Grid is for 2D layouts! Rows and columns.

**Code Example / Starter**:
```html_css
<style>
</style>
```

**Solution Pattern**:
```html_css
<style>
.container { display: grid; }
</style>
```

---

### 2. Templates [Grid]
### Columns and Rows
Define tracks with grid-template-columns.

**Code Example / Starter**:
```html_css
<style>
</style>
```

**Solution Pattern**:
```html_css
<style>
.container { grid-template-columns: 1fr 1fr; }
</style>
```

---

### 3. Grid Span [Grid]
### Spanning
Make an item take up multiple columns.

**Code Example / Starter**:
```html_css
<style>
</style>
```

**Solution Pattern**:
```html_css
<style>
.item { grid-column: span 2; }
</style>
```

---

### 4. Template Areas [Grid]
### Areas
Name your grid areas for easy layouts.

**Code Example / Starter**:
```html_css
<style>
</style>
```

**Solution Pattern**:
```html_css
<style>
.container { grid-template-areas: 'header header' 'main sidebar'; }
</style>
```

---

### 5. Advanced Grid [Grid]
### Auto-fit
Use auto-fit and minmax for responsive grids.

**Code Example / Starter**:
```html_css
<style>
</style>
```

**Solution Pattern**:
```html_css
<style>
.container { grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
</style>
```

---
