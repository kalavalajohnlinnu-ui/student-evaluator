# [SQL] Realm 1: The Royal Data Vault
**Description**: Query database tables, filter rows with WHERE, and sort results.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: SQL

## Lessons & Concepts Covered:

### 1. Inspecting Tables (SELECT *) [Querying]
### What is a Database? 🗄️
Every game, bank, and social network stores its data in tables (like supercharged Excel sheets).

In SQL, **`SELECT * FROM table_name;`** grabs every row and column:

```sql
SELECT * FROM heroes;
```

**Code Example / Starter**:
```sql
CREATE TABLE heroes (name TEXT, level INTEGER, gold INTEGER);
INSERT INTO heroes VALUES ('Aria the Rogue', 12, 600), ('Bartholomew', 15, 1000), ('Celeste the Mage', 11, 800), ('Noob', 2, 10);
-- Write your SQL query:
SELECT * FROM heroes;
```

**Solution Pattern**:
```sql
SELECT * FROM heroes;
```

---

### 2. Filtering with WHERE [Filtering]
### Searching with WHERE
To find only specific rows, use the **`WHERE`** clause:

```sql
SELECT name, gold FROM heroes WHERE gold > 500;
```

**Code Example / Starter**:
```sql
CREATE TABLE heroes (name TEXT, level INTEGER, gold INTEGER);
INSERT INTO heroes VALUES ('Aria the Rogue', 12, 600), ('Bartholomew', 15, 1000), ('Celeste the Mage', 11, 800), ('Noob', 2, 10);
-- Find heroes with level > 10:
SELECT * FROM heroes WHERE level > 10;
```

**Solution Pattern**:
```sql
SELECT * FROM heroes WHERE level > 10;
```

---

### 3. The Inventory Table & LIMIT [Limits]
### Limiting Rows with LIMIT
If a table has 1,000,000 items, you only want the top ones! Use **`LIMIT n`**:

```sql
SELECT item_name, cost FROM inventory LIMIT 2;
```

**Code Example / Starter**:
```sql
CREATE TABLE inventory (item_name TEXT, cost INTEGER);
INSERT INTO inventory VALUES ('Mana Crystal', 100), ('Dragon Scale Armor', 500), ('Apple', 5);
-- Find expensive inventory items:
SELECT * FROM inventory WHERE cost > 50;
```

**Solution Pattern**:
```sql
SELECT * FROM inventory WHERE cost > 50;
```

---
