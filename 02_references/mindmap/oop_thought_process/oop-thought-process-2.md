---
title: oop-thought-process-2
tags: []
aliases: []
date modified: 2025-11-07 08:45:23 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

---

mindmap-plugin: basic

---

## 2. How to Think in Terms of Objects
### Helpful principles
- Knowing the difference between interface and implementation
  - encapsulation
  - distinguish what user needs to know and doesn't need to know
  - interface
    - what user needs to know
  - implementation
    - what user doesn't need to know
    - does not invoke any change to the user's code
- Thinking more abstractly
  - One of the main advantages of OO programming : classes can be reused
  - making class in more abstract way makes code reusable
- Giving the user the minimal interface possible
  - rules
    - Give the users only what they absolutely need
    - Minimal set is insufficient, and it immediately becomes necessary to add interfaces.
    - It is vital to design classes from a user's perspective and not from an information systems viewpoint.
    - Make sure when you are designing a class that you go over the requirements and the design with the people who will actually use it—not just developers (this includes all levels of testing)
### Work on the conceptual analysis and design first, and then think about specific technologies
### Knowing the end user is always important
### OO design is an iterative process, so you do not have to get it exactly right the first time
### Steps
- Determine the users
  - anyone that sends a message to the object
- Determine object behaviors
- Determine environmental constraints
  - computer hardware might limit software functionality
- Identify the public interfaces
  - Question how abstract you want to get with the design
- Identify the implementation
