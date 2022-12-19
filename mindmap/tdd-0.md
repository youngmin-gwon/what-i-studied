
---

mindmap-plugin: basic

---

    
# Test Driven Development
## Benefits
- possible to dramatically reduce the defect density of code
  - QA can shift from reactive to proactive work
  - Project managers can estimate accurately enough to involve real customers in daily development
  - we can have shippable software with new functionality every day, leading to new business relationships with customers
- possible to make the subject of work crystal clear
  - Software engineers can work in minute-by-minute collaboration instead of weekly collaboration
## Discipline
- We must design organicallly, with running code providing feedback between decision
- We must write our own tests, because we can't wait 20 times per day for someone else to write a test
- Our development environment must provide rapid response to small changes
- Our designs consist of many highly cohesive, loosely coupled components, just to make testing easy
- The tougher the programming problem, the less ground that each test should cover
## Mantra
- Red
  - Write a little test that doesn't work, and perhaps doesn't even compile at first
- Green
  - Make the test work quickly, commiting whatever sins necessary in the process
- Refactor
  - Eliminate all of the duplication created in merely getting the test to work
## what is motivation for TDD?
- Courage
  - <-> Fear
    - makes you tentative
    - makes you want to communicate less
    - makes you shy away from feedback
    - makes you grumpy
  - TDD is a way of managing fear during development
## Definition
- A proven set of techniques that encourage simple designs and test suites that inspire confidence
- TDD is an awareness of the gap between decision and feedback during programming, and techniques to control that gap
## Always an answer?
- not proper for the topics of
  - Security
  - Concurrency