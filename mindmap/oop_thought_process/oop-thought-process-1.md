
---

mindmap-plugin: basic

---

    
# 1. Introduction to Object-Oriented Concept
## Object-Oriented concepts
- Encapsulation
  - data hiding is a major part of encapsulation
  - object need not reveal all the attributes and methods
  - important in security, testing, and maintenance
  - composition
    - interface
      - public attributes and methods
      - the fundamental means of communication between objects
    - implementation
      - implementation can change, and it will not affect the user's code
- Inheritance
  - inherits the attributes and methods of another class
  - the ability to create new classes by abstracting out common attributes and behaviors from another class
  - composition
    - superclass(parent class)
      - contains all the attributes and behaviors that are common to classes that inherit from it
    - subclass(child class)
      - an extension of the superclass
  - is-a relationship
- Polymorphism
  - = many shapes
  - tightly coupled to inheritance, but there is a way to implement polymorphism using composition
- Composition
  - objects are built, or composed, from other objects
  - users can use the common functionality in various classes by using composition
  - has-a relationship
## Class
- blueprint for an object
- an object cannot instantiated without class
## Object
- a building block of OO program
- a complete package containing both data and behaviors
  - you can control access to the data in the object using encapsulation
  - you can change how object works without making a change of code in which object is used
- composition
  - attribute
    - state of the object
  - method
    - what the object can do
    - invoked by sending a message
  - message
    - communication mechanism between objects
- normally better to build small objects with specific tasks than
build large objects that perform many.