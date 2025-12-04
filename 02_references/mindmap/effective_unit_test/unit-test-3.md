---
title: unit-test-3
tags: []
aliases: []
date modified: 2025-11-07 08:45:10 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

---

mindmap-plugin: basic

---

## 3. Test doubles
### The power of a test double
- Isolate the code under test
  - we can substitute collaborators with test double
- Speed up test execution
  - test double's implementation is often faster than real one
- Make execution deterministic
  - test double can make tests get same results
- Simulate special conditions
  - test double can throw an exception to test failed case
- Gain access to hidden information
  - we can add for-testing-only method to test code
### What kind of test doubles
- Test stub
  - a short thing
  - it stands in for the real implementation with the simplest possible implementation
  - a typical example of what a stub does - nothing
- Fake object
  - a replicated, but thinned-down version of the real thing
  - usually faster than real one
  - good example: persistence test
- Test spy
  - like a cop going undercover and reporting afterward what he observed
  - useful in a case where there is no return value to assert against
  - it gains access to hidden information
    - by inheriting original object and add for-test-only methods to gain information
- Mock object
  - a special kind of test spy
  - an object that's configured to behave in a certain way under certain circumstances
### Guidelines for using test doubles
- Pick the right double for the test
  - There is no hard and fast rule for much of this, but we should probably mix and match a little
  - heuristics when to use which
    - simple version: stub queries; mock actions.
    - details version
      - you care about a certain interaction taking place in the form of method calls between two objects:

mock object

      - you decided to go with a mock object but your test code ends up looking less pretty than you'd like:

test spy

      - you only care about the collaborator objects being there:

stub

      - you want to run a complex scenario that relies on a service or component that's unavailable or unusable for your test's purposes, and your quick attempt at stubbing all of those interactions grinds to a halt or results in messy test code that's going to be a pain to maintain:

fake object

      - none of the above sufficiently describes your particular situation at hand:

toss a coin—heads is a mock, tails is a stub, and if the coin is standing on its side, you have my permission to whip up a fake.

- Arrange, Act, Assert
  - Follow this order of test and add whitespace between the three blocks of code
  - "given, when, then" in BDD term
- Check for behavior, not implementation
  - Such failure comes from lack of focus
  - A test should test just one thing and test it well while communicating its intent clearly
- Choose your tools
  - Mock Library
- Inject your dependencies
  - Collaborator objects you'd like to replace for the purposes of testing should not be instantiated in the same place they are used
    - Store objects as private member or acquire them, for example, through factory method
  - Employ dependency injection and pass dependencies into the object from outside, typically using constructor injection
### Reason for creating
- to serve as a placeholder until the real thing becomes available
  - to allow you to compile and execute one piece of code before its surrounding pieces were in place
