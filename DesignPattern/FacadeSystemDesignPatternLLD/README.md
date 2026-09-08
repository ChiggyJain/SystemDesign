# Facade Design Pattern — LLD

## What

Facade provides a simple, high-level interface over a set of complex subsystems.

In this implementation, `BankFacade` hides the coordination between `Account`, `Security`, and `Funds`.

## Why

Use Facade when:

- A subsystem has many classes or complex workflows.
- Clients should not depend on internal subsystem details.
- You want one easy entry point for a common operation.

## How

`BankFacade.withdraw()` coordinates the complete withdrawal flow:

```text
Client
  ↓
BankFacade.withdraw()
  ↓
Security verification
  ↓
Account/PIN validation
  ↓
Funds check
  ↓
Debit account
```

The client does not need to know how the individual subsystems cooperate.

## Where

Common use cases include:

- Banking workflows.
- E-commerce checkout.
- Order processing.
- Payment orchestration.
- Cloud SDK wrappers.
- Complex service integrations.

## Real-Life Implementation Example

An e-commerce `CheckoutFacade` can expose one `place_order()` operation while internally coordinating inventory, pricing, payment, shipping, and notification services. The controller only interacts with the facade.

## Code

The complete Python implementation is available in [`main.py`](./main.py).

## Learning Notes

Facade does not necessarily reduce the complexity inside the system; it **hides that complexity from the client** by providing a simpler entry point.
