---
title: clean-code-11
tags: []
aliases: []
date modified: 2025-11-07 08:43:25 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

---

mindmap-plugin: basic

---

## 11. System
### Separate constructing a system from using it
- construction is a very different process from use
- Do not use hard-coded dependency
  - when testing, it is hard to inject test double or mock object
- should separate the startup process, when the application objects are constructed and the dependencies are "wired" together, from the runtime logic that takes over after startup
  - Move all aspects of construction to main
  - abstract factory pattern
- a means to decouple application from the details of how to build objects
### Scale up
- should adopt iterative and incremental way to expand
  - Implement only today's stories, then refactor and expand the system to implement next stories tomorrow
  - TDD, refactoring, clean code
- hard to grow system incrementally only if we maintain the proper separation of concerns
- Cross-cutting concerns
  - Some concerns like persistence tend to cut across the object boundaries of domain
    - AOP
      - programming method to focus on core concerns and minimize duplication for cross-cutting concerns
      - 3 aspect-like mechanisms in Java
        - 1. Java Proxy
          - suitable for simple situations, such as wrapping method calls
          - 1. define a interface
1. implement the interface(POJO)
2. wrap implementation with proxy
          - too much code and not proper for system-wide execution
        - 2. Pure Java AOP Frameworks
          - decorator pattern
          - easy to test
        - 3. AspectJ
      - POJO
        - are purely focused on domain
        - no dependencies on enterprise frameworks
### Dependency Injection
- the application of Inversion of Dependency to dependency management
- a special-purpose container to take responsibility for instantiating dependencies
- most DI containers will provide mechanisms for invoking factories or proxies and won't construct an object until needed = lazy initialization
### Domain-Specific Languages
- good DSL minimized the communication gap between a domain concept and the code that implements it
- code idioms and design patterns
### Postpone architectural decisions until the last possible moment
### Test-driven system
- POJO first
- can be evolved from simple to sophisticated
### Use standards wisely, when they add demonstrable value
- somewhat good, somewhat bad
  - easier to reuse ideas and components, recruit people with relevant experience, encapsulate good ideas, and wire components together
  - creating standards takes too long to wait, and some standards lose touch with the real needs
### Aspect Oriented Programming
