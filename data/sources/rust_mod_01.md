# [RUST] Realm 1: The Armor of Safety
**Description**: Learn the world's most admired language: Rust, immutability, and blazing speed.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Rust

## Lessons & Concepts Covered:

### 1. Hello, Ferris! [Safe Speed]
### Welcome to Rust! 🦀
Rust is voted the most loved programming language year after year! It offers C++ speeds without memory crashes.

In Rust, functions start with `fn` and prints use `println!` with an exclamation mark:

```rust
fn main() {
    println!("Hello from Rust!");
}
```

**Code Example / Starter**:
```rust
fn main() {
    println!("Hello, World!");
}

```

**Solution Pattern**:
```rust
fn main() {
    println!("Welcome to Rust Hero!");
}
```

---

### 2. Immutable by Default (`let mut`) [Immutability]
### The Power of Immutability
In Rust, all variables are locked (immutable) by default! To change a value, you must write `let mut`:

```rust
let mut shield = 50;
shield = shield + 25;
println!("Shield: {}", shield);
```

**Code Example / Starter**:
```rust
fn main() {
    let mut shield = 50;
    // add 25 here
    println!("{}", shield);
}

```

**Solution Pattern**:
```rust
fn main() {
    let mut shield = 50;
    shield = shield + 25;
    println!("{}", shield);
}
```

---
