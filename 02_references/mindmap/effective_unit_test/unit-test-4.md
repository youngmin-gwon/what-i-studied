---
title: unit-test-4
tags: []
aliases: []
date modified: 2025-11-07 08:44:50 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

---

mindmap-plugin: basic

---

## 4. Test Smells: Readability
### Test smells around assertions
- Primitive Assertions
  - assertion should express an assumption or intent
  - level of abstraction is too low when it comes to asserting stuff
  - Ask yourself whether the level of abstraction is right whenever seeing comparisons such as != or ==, especially to magic numbers like -1 or 0
- Hyperassertions
  - it's hard to say what exactly it's supposed to check, and when you step back to observe, the test is probably breaking far more frequently than the average.
  - this test is too broad
    - it fails too easily, making it brittle and fragile
  - this test violate a fundamental guiding principle for what constitutes a good test:
    - A test should have only one reason to fail (test version of SRP)
  - Make test more focused and easier to grasp
- Bitwise Assertions
  - Bit operation is powerful feature but too abstract to understand
  - we are not in the domain of bits and bytes
  - Replace the bit operator with one or more boolean operators, expressing the expectations clearly one by one
### Test smells around information scatter within the code base
- Split Logic
  - tests that span several screenfuls of code
  - Chunk test code into smaller pieces
  - a heuristic for quickly determining what you should pull into the test and what to push out to the sidelines
    - 1. if it's short, inline it
    - 2. if it's too long to keep inlined, stash it behind a factory method or a test data builder
    - 3. if that feels inconvenient, pull it out into a separate file
      - Trim your data to bare essentials
      - Place such data files in the same folder as the tests that use them
      - Whatever structure you end up with, make it a convention with your team and stick to it
### Test smells around excess or irrelevant detail
- Incidental Details
  - test has too much details
  - how to express core assertion
    - 1. Extract the non-essential setup into private method or the setup
    - 2. Give things appropriate, descriptive names
    - 3. Strive for a single level of abstraction in a method
- Split Personality
  - A test should only check one thing and check it well
- Magic Numbers
  - Replace them with constants or variables that give the number that much-desired meaning
- Setup Sermon
  - messy setup code looks complicated
  - how to set up
    - 1. Extract the nonessential details from the setup into private methods
    - 2. Give things appropriate, descriptive name
    - 3. Strive for a single level of abstraction in the setup
- Overprotective Tests
  - this assertion is superfluous
