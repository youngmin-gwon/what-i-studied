
---

mindmap-plugin: basic

---

    
# 2. In search of good
## What makes a test "good"?
- readability and maintainability
  - we cannot edit code when we don't understand code
- structure
  - we are not confident if all codes place in one
  - helpful feedback term gets longer when code is too long
- right target to test
  - name and contents should be suitable
- independence
  - time
  - randomness
  - concurrency
  - infrastructure
  - pre-existing data
  - persistence
  - networking
- reliability and repeatability
  - test case contains assert
- how a test makes use of test doubles
  - test doubles: stubs, fakes, or mocks
    - benefits
      - can speed up test execution by simplifying the code
      - can simulate exceptional conditions
      - can observe state and interaction