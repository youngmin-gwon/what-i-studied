
---

mindmap-plugin: basic

---

    
# 9. Unit Tests
## TDD
- Laws
  - 1. You may not write production code until you have written a failing unit test
  - 2. You may not write more of a unit test than is sufficient to fail, and not compiling is failing
  - You may not write more production code than is sufficient to pass the currently failing test
- These three laws lock you into 30 seconds-long cycle
## Keep tests clean
- Test code is just as important as production code
- Having dirty tests means having no tests
- Tests must change as the production code evolves
- The dirtier the tests, the harder they are to change
## Readability
- principles
  - clarity
  - simplicity
  - density of expression
- Build-Object-Check pattern is useful
- Anyone should be able to work out very quickly, without being misled or overwhelmed by details
- Domain-Specific Testing Language
  - Rather than using the test APIs, we build up a set of functions that make use of test APIs more convenient to write and easier to read
  - succinct and expressive forms
## A dual standard
- Test environment and production environment have very different needs
- Test code must still be simple, succinct, and expressive but not as efficient as production code
  - assertEquals("HBchL", hw.getState());
## Never make test as ad hoc code
## Test suite
- key to keep your design and architecture as clean as possible
- The higher test coverage, the less your fear
## Test unit
- one assert per test
  - defects
    - a lot of duplicate code
  - okay to put more than one assert in a test
    - but, the number of asserts in a test should be minimized
- single concept per test
  - hard to figure out why section is there if more than one concept
  - minimize the number of asserts per concept
## Given-When-Then Convention
## F.I.R.S.T.
- 1. Fast
  - when test runs slow, you won't want to run test frequently
- 2. Independent
  - When tests depend on each other, then the first one to fail causes a cascade of downstream failures, making diagnosis difficult and hiding downstream defects
- 3. Repeatable
  - should be repeatable without network
  - if your test aren't repeatable in any environment, then you'll always have an excuse for why they fail
- 4. Self-validating
  - If the test aren't self-validating, then failure can become subjective and running the tests can require a long manual evaluation
- 5. Timely
  - Unit tests should be written just before the production code that makes them pass