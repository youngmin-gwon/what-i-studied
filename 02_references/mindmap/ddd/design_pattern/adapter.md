---
title: adapter
tags: []
aliases: []
date modified: 2025-11-07 08:44:08 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

```mermaid
---
title: Adapter Pattern
---
classDiagram
    ITarget <-- Client
    ITarget <|.. Adapter
    Adaptee <-- Adapter
    class ITarget{
        +operation()
    }
    class Adapter{
        -Adaptee adaptee
        +operation()
    }
    class Adaptee{
        +concreteOperation()
    }

```
