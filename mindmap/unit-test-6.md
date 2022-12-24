---

mindmap-plugin: basic

---

# 6. Test Smells: <br/>Trustworthiness

## smells around<br/> code comments
- Commented-out tests
   - dead code
   - Try to understand and validate its purpose
   - Otherwise, delete it
- Misleading comments
   - it is arbitrary in that they may suggest something that is not true
   - Replace the comment with better names for variables and methods
   - Extract a method from that commented block of code and name it well

## smells around<br/> poor expectation management
- Never-failing tests
   - worse than not having test
   - Make sure you don't forget assertion when exception is not thrown
   - Develop a habit of triggering a failing test and edit the test
- Shallow promises
   - category
      - Test doesn't do anything
         - test is commented out inside
      - Test doens't actually test anything<br/>(=happy path tests)
         - no assertions in test
      - Test isn't as thorough as its name suggests
   - Principle
      - Delete commented-out code
      - Start with the assertion
         - it is hard to accidently remove that assertion
         - it helps you focus on the essence of the test
      - Leave the test's name initially empty or call it, for example, <br/>*TODO()*, until you've fully sketched out the test
- Lowered expectations
   - an easy way sacrificing standard of certainty and precision
   - Raise the bar higher and make the test more specific about what you expect
   - Caution!
      - being totally exact is not a virtue as such (remember pixel perfect in Ch.5)
      - Balance test between abstraction and precision

## smells around<br/> conditional execution
- Platform prejudice
   - it inevitably contains *if-else*
      - only one of branches gets executed on any given platform
      - only checking the platform that we happen to run on
   - Refactor __Platform__ so that it can be substituted on a test-by-test basis
- Conditional tests
   - it hides a secret conditional within, making the test logic different from what its name suggests
   - if some condition turns false, some assertion logic would not be made
   - Substitute conditional with assertion