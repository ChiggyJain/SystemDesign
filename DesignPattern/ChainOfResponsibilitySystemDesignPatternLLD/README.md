# Chain of Responsibility Design Pattern — LLD

## What

Chain of Responsibility passes a request through a sequence of handlers. Each handler decides whether it can process the request or should pass it to the next handler.

In this implementation, ATM note dispensers form a chain for denominations ₹2000, ₹500, and ₹100.

## Why

Use this pattern when:

- Multiple handlers may process the same request.
- The sender should not know the exact handler.
- Handlers need to be ordered.
- New handlers should be added without changing the client.

## How

Each `NoteDispenser` contains a reference to the next dispenser. A withdrawal request starts at the first handler and moves down the chain.

For example, ₹3100 is processed as:

```text
₹3100
  ↓
₹2000 handler → 1 note
  ↓
₹500 handler  → 2 notes
  ↓
₹100 handler  → 1 note
```

## Where

Common use cases include:

- ATM cash dispensing.
- HTTP middleware pipelines.
- Authorization checks.
- Logging and validation pipelines.
- Customer support escalation.
- Event processing chains.

## Real-Life Implementation Example

An API request may pass through authentication, authorization, validation, rate limiting, and business-rule handlers. Each handler can reject the request or pass it to the next stage, keeping responsibilities separated.

## Code

The complete Python implementation is available in [`main.py`](./main.py).

## Learning Notes

The main benefit is **decoupling the sender from the receiver**. The chain order matters, so production implementations should make handler ordering explicit and easy to test.
