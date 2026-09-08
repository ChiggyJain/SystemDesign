# Factory Method Design Pattern — LLD

## What

Factory Method defines an interface for creating an object while allowing subclasses to decide which concrete object is created.

In this implementation, `Logistics` defines the delivery workflow and subclasses choose the transport: `Truck` for road logistics and `Ship` for sea logistics.

## Why

Use Factory Method when:

- Object creation should be separated from business logic.
- The concrete type depends on a subclass or runtime context.
- New product types should be added with minimal changes to client code.

## How

The implementation contains:

- `Transport` — product interface.
- `Truck` and `Ship` — concrete products.
- `Logistics` — creator with the common `planDelivery()` workflow.
- `RoadLogistics` and `SeaLogistics` — creators that implement `create_transport()`.

### Design Flow

```text
Client
  ↓
Logistics.planDelivery()
  ↓
create_transport()
  ├── RoadLogistics → Truck
  └── SeaLogistics  → Ship
```

## Where

Common use cases include:

- Logistics and shipping systems.
- Notification provider creation.
- Database connection creation.
- Cloud resource clients.
- Report/export generation.

## Real-Life Implementation Example

A logistics platform supports road, sea, and air delivery. The common delivery process stays unchanged, while each logistics type creates its own transport implementation.

## Code

The complete Python implementation is available in [`main.py`](./main.py).

## Learning Notes

The important distinction is that the **creation decision is delegated**, while the creator can still define a common business workflow around the created product.
