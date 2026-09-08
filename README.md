# System Design

This repository contains **System Design and Low-Level Design (LLD) implementations in Python**.

The goal is to understand design concepts through practical, executable examples rather than only theoretical definitions.

## Design Pattern

The following design patterns are implemented with Python LLD examples. Each pattern folder contains a `main.py` implementation and a dedicated `README.md` explaining **what, why, how, where**, and a real-life implementation example.

| Design Pattern | Description |
|---|---|
| [Abstract Factory](./DesignPattern/AbstractFactorySystemDesignPatternLLD/) | Creates families of related objects without coupling the client to concrete implementations |
| [Adapter](./DesignPattern/AdapterSystemDesignPatternLLD/) | Converts an incompatible interface into the interface expected by the application |
| [Bridge](./DesignPattern/BridgeSystemDesignPatternLLD/) | Separates an abstraction from its implementation so both can evolve independently |
| [Chain of Responsibility](./DesignPattern/ChainOfResponsibilitySystemDesignPatternLLD/) | Passes a request through a chain of handlers until the appropriate handler processes it |
| [Composite](./DesignPattern/CompositeSystemDesignPatternLLD/) | Treats individual objects and groups of objects uniformly through a tree structure |
| [Decorator](./DesignPattern/DecoratorSystemDesignPatternLLD/) | Adds responsibilities or behavior dynamically by wrapping an existing object |
| [Facade](./DesignPattern/FacadeSystemDesignPatternLLD/) | Provides a simple interface over a complex set of subsystems |
| [Factory Method](./DesignPattern/FactorySystemDesignPatternLLD/) | Defines object creation through a method while allowing subclasses to choose the concrete product |
| [Observer](./DesignPattern/ObserverSystemDesignPatternLLD/) | Notifies multiple subscribers automatically when the subject's state changes |
| [Prototype](./DesignPattern/PrototypeSystemDesignPatternLLD/) | Creates new objects by cloning an existing configured prototype |
| [Singleton](./DesignPattern/SingletonSystemDesignPatternLLD/) | Ensures controlled creation of a single shared instance within the application process |
| [Strategy](./DesignPattern/StrategySystemDesignPatternLLD/) | Encapsulates interchangeable algorithms or behaviors and selects one at runtime |
| [Template Method](./DesignPattern/TemplateSystemDesignPatternLLD/) | Defines a fixed algorithm skeleton while allowing subclasses to customize individual steps |

## Repository Structure

```text
SystemDesign/
└── DesignPattern/
    ├── AbstractFactorySystemDesignPatternLLD/
    ├── AdapterSystemDesignPatternLLD/
    ├── BridgeSystemDesignPatternLLD/
    ├── ChainOfResponsibilitySystemDesignPatternLLD/
    ├── CompositeSystemDesignPatternLLD/
    ├── DecoratorSystemDesignPatternLLD/
    ├── FacadeSystemDesignPatternLLD/
    ├── FactorySystemDesignPatternLLD/
    ├── ObserverSystemDesignPatternLLD/
    ├── PrototypeSystemDesignPatternLLD/
    ├── SingletonSystemDesignPatternLLD/
    ├── StrategySystemDesignPatternLLD/
    └── TemplateSystemDesignPatternLLD/
```

## Learning Approach

Each implementation focuses on:

1. Understanding the design problem.
2. Identifying the responsibilities of each class.
3. Applying the appropriate design pattern.
4. Implementing the LLD in Python.
5. Connecting the pattern to a real-world software system.

## Technology

- Python 3
- Object-Oriented Programming
- SOLID principles
- Low-Level Design
- Design Patterns
