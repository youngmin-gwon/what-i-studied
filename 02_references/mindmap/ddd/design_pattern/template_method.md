---
title: template_method
tags: []
aliases: []
date modified: 2025-11-07 08:44:59 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

```mermaid
classDiagram
    AbstractClass <|--ConcreteClass
    class AbstractClass {
        +templateMethod()
        #hook1()
        #hook2()
    }
    
    class ConcreteClass {
        #hook1()
        #hook2()
    }
```
