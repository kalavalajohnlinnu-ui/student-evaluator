# [PYTHON] Module 9: Object-Oriented Programming (OOP)
**Description**: Model real-world entities with classes, methods, the __init__ constructor, and inheritance.

**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/

**Language Realm**: Python

## Lessons & Concepts Covered:

### 24. Classes & Objects [OOP Basics]
### Classes: Blueprints for Objects
A **class** is a blueprint (like architectural plans for a house). An **object** is an actual house built from that blueprint.

```python
class Car:
    pass

# Creating an instance
my_car = Car()
my_car.color = "Red"
print(my_car.color)
```

**Code Example / Starter**:
```python
# Define Book class and instantiate:
class Book:
    pass

my_book = Book()
# Set attributes:


print(my_book.title)

```

**Solution Pattern**:
```python
class Book:
    pass

my_book = Book()
my_book.title = "Python Mastery"
my_book.pages = 320
print(my_book.title)
```

---

### 25. The __init__ Method & self [Constructors]
### The __init__ Constructor & self
The **`__init__()`** method runs automatically whenever a new object is instantiated.
The **`self`** parameter refers to the specific instance being created!

```python
class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def take_damage(self, amount):
        self.hp -= amount
        return self.hp

player = Hero("Aragorn", 100)
player.take_damage(25)
print(player.hp)  # 75
```

**Code Example / Starter**:
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        # Add amount to self.balance and return it:
        pass

acc = BankAccount("Alice", 100)
acc.deposit(50)
print(acc.balance)

```

**Solution Pattern**:
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance

acc = BankAccount("Alice", 100)
acc.deposit(50)
print(acc.balance)
```

---

### 26. Inheritance & super() [OOP Advanced]
### Inheritance: Code Hierarchy
Inheritance lets a child class inherit all methods and attributes from a parent class:

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"  # Overrides parent method!

dog = Dog()
print(dog.speak())  # 'Woof!'
```

**Code Example / Starter**:
```python
class Vehicle:
    def get_fuel_type(self):
        return "Gasoline"

# Define ElectricCar inheriting from Vehicle:
class ElectricCar(Vehicle):
    pass

tesla = ElectricCar()
print(tesla.get_fuel_type())

```

**Solution Pattern**:
```python
class Vehicle:
    def get_fuel_type(self):
        return "Gasoline"

class ElectricCar(Vehicle):
    def get_fuel_type(self):
        return "Electricity"

tesla = ElectricCar()
print(tesla.get_fuel_type())
```

---
