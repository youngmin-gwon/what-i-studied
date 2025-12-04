---
title: clean-code-7
tags: []
aliases: []
date modified: 2025-11-07 08:43:22 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

---

mindmap-plugin: basic

---

## 7. Error Handling
### Exception
- clean and robust way to handle errors with grace and style
- displines
  - Use exception rather than return codes
    - easy to forget return values
    - throwing exception is cleaner
    - better not because it is cleaner, but because two concerns, logic and error handling, are separated
  - try-catch-finally first
    - good starting point, and can narrow down next
    - follow TDD process
  - Use unchecked exception
    - Checked exceptions are not necessary for the production of robust software
    - The cost of checked exceptions is an OCP violation: checked exceptions break encapsulation
  - Provide context with Exception
    - Descriptive and informative error messages always help
  - Define Exception Classes in Terms of a Caller's Needs
    - Wrappers for 3rd-party libraries are best practices
    - Wrappers make you untied to a particular vendor's API design choices
    - The information sent with user-defined exception can distinguish the errors
### Define Normal Flow
- Normal Flow: default work flow when nothing is got
- Wrap external APIs so that you can throw your own exceptions
- Use Special Case(=Null Object) pattern
### Null
- Don't pass null
- Don't return null
  - If you are tempted to return null from a method, consider throwing an exception or returning a "Special Case" object
  - If you are calling a null-returning method from a third-party API, consider wrapping that method with a method that either throws an exception or returns a "Special Case" object
### Logic first
- if error handling obscures logic, it's wrong
