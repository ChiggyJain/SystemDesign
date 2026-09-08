# Abstract Factory Design Pattern — LLD

## What

Abstract Factory provides an interface for creating **families of related objects** without exposing the concrete classes to the client.

In this implementation, a theme factory creates related UI components such as `Button` and `Checkbox`.

## Why

Use Abstract Factory when:

- Multiple objects must belong to the same product family.
- The client should not depend on concrete implementations.
- You need to switch an entire family of implementations together.

For example, a UI application can switch from a Light theme to a Dark theme without changing the client code.

## How

The implementation contains:

- `Button` and `Checkbox` — abstract product interfaces.
- `DarkButton`, `DarkCheckbox` — dark-theme products.
- `LightButton`, `LightCheckbox` — light-theme products.
- `WidgetFactory` — abstract factory.
- `DarkThemeWidgetFactory` and `LightThemeWidgetFactory` — concrete factories.

The client works with `WidgetFactory`, so it does not need to know which concrete button or checkbox is created.

### Design Flow

```text
Client
  ↓
WidgetFactory
  ├── createButton()   → Button
  └── createCheckbox() → Checkbox
          ↓
   Dark / Light Factory
          ↓
 Dark / Light Products
```

## Where

Common use cases include:

- Cross-platform UI components.
- Light/Dark UI themes.
- Database-driver families.
- Cloud-provider-specific SDK components.
- OS-specific integrations.

## Real-Life Implementation Example

A SaaS application supports multiple database vendors. Instead of directly creating MySQL, PostgreSQL, or MongoDB-specific objects throughout the application, a provider-specific factory can create the matching connection, query builder, and transaction objects as one compatible family.

## Code

The complete Python implementation is available in [`main.py`](./main.py).

## Learning Notes

The key idea is **family-level object creation**. Factory Method usually creates one product, while Abstract Factory creates multiple related products that should work together.
