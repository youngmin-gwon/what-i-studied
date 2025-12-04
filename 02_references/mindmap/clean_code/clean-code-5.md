---
title: clean-code-5
tags: []
aliases: []
date modified: 2025-11-07 08:43:18 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

---

mindmap-plugin: basic

---

## 5. Formatting
### Your style and displine survives, even though your code does not
### Follow team's formatting rule
- But all developers in team should agree upon the formatting style
### Horizontal Formatting
- Openness and Density
  - use whitespace to accentuate like the precedence of operators
- Alignment
  - not useful. IDE will do
- Indentation
  - allow developers quickly hop over scopes, such as if/else
- Breaking Indentation
  - some doesn't like collapsing scopes down to one line
### Vertical Formatting
- Write code like newspaper article
  - simple, but explanatory name
  - high level concepts first, and supporting details later
  - most are very small
- Openness Between Concepts
  - blank line between package / import / each function
- Density
  - tightly related code appear vertically dense like member variables
- Distance
  - related concepts should be kept close
  - variables should be declared as close to their usage
  - instance variables should be declared at the top of the class
  - dependent functions should be vertically close, and the caller should be above the callee
  - the stronger that affinity, the less vertical distance there should be between them
- Ordering
  - a function called should be below a function calling
### Small chunk is better
