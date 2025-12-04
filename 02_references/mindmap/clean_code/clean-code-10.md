---
title: clean-code-10
tags: []
aliases: []
date modified: 2025-11-07 08:43:24 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

---

mindmap-plugin: basic

---

## 10. Classes
### Class organization
- orders
  - 1. a list of variables
    - static constants
    - private static variables
    - private instance variables
  - 2. public functions
  - 3. private utilities
- Encapsulation
  - no good reason to have a public variable
### Class should be small
- How small?
  - small to have one responsibility
    - SRP
      - helps us recognize and create better abstractions in our code
      - a large number of small, single-purpose classes makes it more difficult to understand the bigger picture?
        - a system with many small classes has no more moving parts than a system with a few large classes
        - The primary goal in managing such complexity is to organize it so that a developer knows where to look to find things and need only understand the directly affected complexity at any given time
- Cohesion
  - classes should have a small number of instance variables
  - each of the methods of a class should manipulate one or more of those variables
  - the more variables a method manipulates the more cohesive that method is to its class
  - we would like cohesion to be high
  - when class lose cohesion, split them
    - the program might get longer
### Name
- The first way of helping determine class
- should describe what responsibilities it fulfills
- The more ambiguous the class name, the more likely it has too many responsibilities
  - weasel words like Processor, Manager, or Super
- should be able to write a brief description of the class in about 25 words, without the words "if", "and", "or", or "but."
### Adaptive to change
- organize our classes so as to reduce the risk of change
  - command pattern
- Isolate code from change
  - a client class depending upon concrete details is at risk when those details change
  - dependencies upon concrete details create challenges for test
  - Introduce interfaces and abstract classes to help isolate the impact of details
### Attitude to make class
- Don't think we are done once the program works. Make your program clean and organized next.
