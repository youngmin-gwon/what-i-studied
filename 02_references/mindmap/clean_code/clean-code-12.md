---
title: clean-code-12
tags: []
aliases: []
date modified: 2025-11-07 08:43:25 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

---

mindmap-plugin: basic

---

## 12. Emergence
### Kent Beck's four rules of Simple Design
- Runs all the tests
  - small and simple purpose = testable
  - more tests = more DIP, DI, interface/abstract class
  - low coupling and high cohesion
- Contains no duplication
  - commonality extraction => starts to recognize violations of SRP
  - template method pattern
- Expresses the intent of the programmer
  - software project cost = maintenance => should be clear to understand
  - choose good names
  - keep your functions and classes small
  - use standard nomenclature such as design patterns
  - write unit tests well
  - most important part: try
  - craftmanship
- Minimizes the number of classes and methods
  - but it should be more pragmatic
  - goal: keep our overall system small while we are keeping our functions and classes small
  - lowest priority of the 4 Simple Design rules
### Refactoring
- more tests = confidence to clean up the code
- low coupling, high cohesion, separation of concerns, system concern modularization, small functions and classes, better names
