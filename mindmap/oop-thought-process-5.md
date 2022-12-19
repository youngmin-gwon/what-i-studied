
---

mindmap-plugin: basic

---

    
# 5. Class Design Guidelines
## Goals
- Model real-world systems in ways similar to the ways in which people actually think
## Encapsulate the behaviors into single-responsibility interfaces and code to the interfaces
## Steps
- Identify the public interfaces
  - minimum public interface makes the class as concise as possible
  - the implementation should not involve the users at all
    - the best way to enable change of behaviors:
the use of interfaces and composition
- Design robust constructors (and perhaps destructors)
  - a constructor should put an object into an initial, safe state
  - In languages that include destructors, it is of vital importance that the destructors include proper clean-up functions
- Design error handling into a class
  - application should never crash
- Design with reuse in mind
- Design with extensibility in mind
  - OCP
  - Make names descriptive
  - Abstract out non-portable code
  - Provide a way to copy and compare objects
  - Keep the scope as small as possible
- Design with maintainability in mind
  - Make class as small as possible
    - changes in one class have no impact or minimal impact on other classes
  - Use iteration in the development process
  - Test the interface
    - Use stub and do not delete it
- Use object persistence
  - the state of the object must be saved for later use