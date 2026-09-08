# Decorator Design Pattern — LLD

## What

Decorator adds behavior to an object dynamically by wrapping it with another object that follows the same interface.

In this implementation, `PlainText` can be wrapped by decorators such as `ItalicText` and `BoldText`.

## Why

Use Decorator when:

- Behavior must be added dynamically.
- You want combinations of features without creating many subclasses.
- The original class should remain unchanged.

## How

The implementation contains:

- `Text` — common component interface.
- `PlainText` — concrete component.
- `TextDecorator` — base wrapper.
- `ItalicText` and `BoldText` — concrete decorators.

Decorators can be stacked, allowing behavior to be composed at runtime.

### Design Flow

```text
PlainText
   ↓
ItalicText
   ↓
BoldText
   ↓
Final formatted text
```

## Where

Common use cases include:

- Text formatting.
- Logging enhancements.
- Request/response middleware.
- Compression or encryption wrappers.
- Caching wrappers.
- Access-control wrappers.

## Real-Life Implementation Example

A service method can be wrapped with logging, metrics, caching, and authorization decorators. The original business logic remains focused on its core responsibility while cross-cutting behavior is composed around it.

## Code

The complete Python implementation is available in [`main.py`](./main.py).

## Learning Notes

Decorator is based on **wrapping and composition**, not modifying the original object. It is useful when many optional behaviors can be combined in different orders.
