
---

mindmap-plugin: basic

---

    
# 3. More Object-Oriented Concepts
## Constructor
- methods that share the same name as the class
- one of the first things called when a new object is created
- functions
  - memory allocation
  - attribute initialization
- default constructor
  - at least one constructor always exists, regardless of whether you write a constructor yourself
  - Provide default constructor. Do not count on the compiler to initialize attribute
- multiple constructor
  - in some languages, multiple constructor can be provided using method overloading
- How the superclass is costructed
  - 1. Inside the constructor, the constructor of the class’s superclass is called
  - 2. Each class attribute of the object is initialized
  - 3. The rest of the code in the constructor executes
## Operator Overloading
- it can be downright confusing for people who read and maintain code
## Error Handling
- important advantage for OO programming languages
- this solves the problem of trying to figure out where the problem started and unwinding the code to the proper point
## Scope
- attributes (and methods) exist within a particular scope
- types
  - 1. Local attribute
  - 2. Object attribute
    - member variable
    - not shared between different objects
  - 3. Class attribute
    - static variable
      - as close to global data as we get in OO design
    - shared between different objects
    - potential synchronization problem
## Multiple Inheritance
- one of the more powerful and challenging aspects of class design
- multiple inheritance can significantly increase complexity of a system, both for the programer and the compiler writers
- The modern concept of inheritance is a single-parent inheritance
## Object Operation
- copyWith(), equals() operation
  - deep copy
    - make new copy for all referenced objects
    - the copy itself can create significant overhead
  - shallow copy
    - simple copy the reference and not follow the levels
- not quite simple because object contains reference