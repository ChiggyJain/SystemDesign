# Bridge Design Pattern — LLD

## What

Bridge separates an abstraction from its implementation so both can evolve independently.

In this implementation, remote controls are the abstraction and devices such as TV and Radio are the implementation side.

## Why

Use Bridge when:

- You have two dimensions of change that should evolve independently.
- Inheritance would create too many combinations.
- You want to switch implementations at runtime.

## How

The implementation contains:

- `Device` — implementation interface.
- `TV` and `Radio` — concrete devices.
- `BasicRemoteControl` and `AdvanceRemoteControl` — abstractions that compose a `Device`.

The remote does not inherit from TV or Radio. It holds a device reference and delegates device operations to it.

### Design Flow

```text
Remote Control Abstraction
          ↓
       Device
       ↙   ↘
      TV   Radio

BasicRemote ─┐
AdvanceRemote┘ → can work with either device
```

## Where

Common use cases include:

- Remote controls and electronic devices.
- Cross-platform UI frameworks.
- Notification abstractions over different providers.
- Payment abstractions over different gateways.
- Storage abstractions over local/cloud implementations.

## Real-Life Implementation Example

A smart-home application provides one remote-control abstraction that can operate TVs, speakers, and lights. New remote features and new device types can be added independently instead of creating a separate class for every combination.

## Code

The complete Python implementation is available in [`main.py`](./main.py).

## Learning Notes

The key idea is **composition over inheritance**. Bridge is especially useful when both the abstraction hierarchy and implementation hierarchy are expected to grow.
