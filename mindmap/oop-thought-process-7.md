
---

mindmap-plugin: basic

---

    
# 7. Mastering inheritance and composition
## Purpose of both inheritance and composition
- object reuse
## Inheritance
- is-a relationship
- it inherits attributes and methods from parent class
  - it saves some design and coding time
  - it saves testing and maintenance time
  - it factors out commonality in one place
- from the general to the specific by factoring out commonality
- the more you factor out, the more complex your system get
  - Deciding whether to design for less complexity or more functionality is a balancing act
- misconception:

Turn away from inheritance by implementing designs solely with composition
  - Use both composition and inheritance, but only in their proper contexts
  - composition is more appropriate in more cases than inheritance—not that it should be used whenever possible
## Composition
- has-a relationship
- it builds objects by using other objects
- idea that objects are made up of other objects
- an aggregate, a compound, or a composite object
- too much composition leads to more complexity
## Back to OO
- Why encapsulation is fundamental to OO
  - because OO implements paradoxical principle:

inheritance weakens encapsulation
    - the change from a superclass ripples through the class hierarchy
    - how to reduce the risk posed by this dilemma: 

stick to the strict is-a condition when using inheritance
- Polymorphism
  - designing a class for the purpose of creating totally independent objects is what OO is all about
  - you can send messages to various objects, and they will respond according to their object’s type