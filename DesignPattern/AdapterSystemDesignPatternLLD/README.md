# Adapter Design Pattern — LLD

## What

Adapter converts the interface of an existing class into an interface expected by the client.

In this implementation, different payment gateways such as Stripe and Razorpay are adapted to one common `PaymentProcessor` interface.

## Why

Use Adapter when:

- Existing classes have incompatible interfaces.
- You cannot or do not want to modify third-party code.
- Your application needs one consistent interface for multiple implementations.

## How

The implementation contains:

- `PaymentProcessor` — target interface expected by the application.
- `StripePaymentAdapter` — adapts Stripe's payment behavior.
- `RazorPayPaymentAdapter` — adapts Razorpay's payment behavior.

The client calls `pay(amount)` without knowing which external gateway is being used.

### Design Flow

```text
Client
  ↓
PaymentProcessor
  ↓
Adapter
  ├── StripePaymentAdapter
  └── RazorPayPaymentAdapter
       ↓
Third-Party Payment Gateway
```

## Where

Common use cases include:

- Payment gateway integrations.
- Legacy system integration.
- Third-party SDK integration.
- Cloud-provider abstraction.
- Migrating from one external service to another.

## Real-Life Implementation Example

An e-commerce application defines its own payment interface. Stripe, Razorpay, and another gateway expose different SDK methods. Each gateway gets an adapter implementing the application's common payment interface, allowing the checkout service to remain unchanged.

## Code

The complete Python implementation is available in [`main.py`](./main.py).

## Learning Notes

The Adapter pattern is mainly about **interface compatibility**. It does not change the underlying third-party object's core behavior; it translates how the application communicates with it.
