# Composite Design Pattern — LLD

## What

Composite lets clients treat individual objects and groups of objects uniformly.

In this implementation, `File` is a leaf and `Directory` is a composite. Both are represented through the common `FileSystemNode` abstraction.

## Why

Use Composite when:

- Data naturally forms a tree structure.
- Individual objects and collections should expose the same interface.
- Operations need to work recursively over nested structures.

## How

The implementation contains:

- `FileSystemNode` — common abstraction.
- `File` — leaf node with its own size/content.
- `Directory` — composite node containing child nodes.

A directory can contain files and other directories. Operations such as calculating size or displaying content can therefore recurse through the tree.

### Design Flow

```text
FileSystemNode
     ├── File
     └── Directory
          ├── File
          └── Directory
               └── File
```

## Where

Common use cases include:

- File systems.
- Organization hierarchies.
- Product/category trees.
- UI component trees.
- Menu and submenu structures.
- Document structures.

## Real-Life Implementation Example

A document-management system can model folders and documents using one common node interface. A folder can contain documents or subfolders, while operations such as total size, search, and display recursively traverse the hierarchy.

## Code

The complete Python implementation is available in [`main.py`](./main.py).

## Learning Notes

The core idea is **tree structure + uniform interface**. Composite is particularly powerful when recursive operations are central to the domain.
