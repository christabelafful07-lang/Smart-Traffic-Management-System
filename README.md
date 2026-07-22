# POLYMORPHISM-Traffic-Management-System

## Overview
This project demonstrates the concept of **Polymorphism** in Object-Oriented Programming (OOP) using Python. It models a Smart Traffic Management System where different traffic devices respond to the same `activate()` command in different ways.

The project also showcases other OOP principles such as **Inheritance**, **Encapsulation**, and **Method Overriding**.

---

## Features
- Parent class: `TrafficDevice`
- Child classes:
  - `TrafficLight`
  - `SpeedCamera`
  - `PedestrianSignal`
  - `EmergencySiren`
- Uses **polymorphism** to activate all devices through a single loop.
- Demonstrates **encapsulation** using private attributes and getter methods.
- Demonstrates **inheritance** and **method overriding**.

---

## Project Structure

```
POLYMORPHISM-Traffic-Management-System/
│
├── traffic_management.py
└── README.md
```

---

## How It Works

Each traffic device inherits from the `TrafficDevice` class and overrides the `activate()` method to perform its own unique task.

Instead of checking the type of each object, all devices are stored in a list and activated using a single loop.

Example:

```python
for device in devices:
    device.activate()
```

This demonstrates **runtime polymorphism**, where the correct `activate()` method is called based on the object's class.

---

## Sample Output

```text
Smart Traffic Management System

Traffic Light: Changing lights (Red → Yellow → Green).
Speed Camera: Capturing speeding vehicles.
Pedestrian Signal: Displaying WALK signal for pedestrians.
Emergency Siren: Sounding emergency alert for priority vehicles.
```

---

## OOP Concepts Demonstrated

### Encapsulation
- The device name is stored as a private attribute.
- A getter method is used to access the value.

### Inheritance
- All traffic devices inherit from the `TrafficDevice` parent class.

### Method Overriding
- Each child class provides its own implementation of the `activate()` method.

### Polymorphism
- The same `activate()` method call produces different behaviors depending on the object.

---



- Python 3.x

---



2. Navigate into the project folder:

```bash
cd POLYMORPHISM-Traffic-Management-System
```


```

---

## Author

**NAME: AFFUL CHRISTABEL**
INDEX NUMBER: FOE.41.006.014.25
CLASS: EL-1A

---

## Acknowledgement

This project was completed as part of an Object-Oriented Programming (OOP) case study on **Polymorphism**, demonstrating how multiple objects can respond differently to the same method call without modifying the activation loop.# Smart-Traffic-Management-System
