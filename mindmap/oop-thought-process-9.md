
---

mindmap-plugin: basic

---

    
# 9. Building Objects and Object-Oriented Design
## Composition
- it builds systems by combining less complex parts
  - Stable, complex systems are nearly decomposable.
  - decoupling is quite important for some languages because objects are dynamically loaded
- types
  - Aggregation
    - a complex object composed of other objects
  - Association
    - association is used when one object wants another object to perform a service for it
- dividing lines between association and aggregation are often blurred
- Avoid making objects highly dependent on one another
  - But, mixing domain gives convenience
  - the convenience of mixing domain is design decision. if benefit outweighs risk, then it might be the preferred decision
## Cardinality
- the number of objects that participate in an association and whether the participation is optional or mandatory
- how to determine
  - Which objects collaborate with which other objects?
  - How many objects participate in each collaboration?
  - Is the collaboration optional or mandatory?