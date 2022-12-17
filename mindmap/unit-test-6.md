---

mindmap-plugin: basic

---

# 6. Test Smells: Trustworthiness

## smells around code comments
- Commented-out tests
   - dead code
   - Try to understand and validate its purpose
   - Otherwise, delete it
- Misleading comments
   - it is arbitrary in that they may suggest something that is not true
   - Replace the comment with better names for variables and methods
   - Extract a method from that commented block of code and name it well

## smells around poor expectation management
- Never-failing tests
- Shallow promises
- Lowered expectations

## smells around conditional execution
- Platform prejudice
- Conditional tests