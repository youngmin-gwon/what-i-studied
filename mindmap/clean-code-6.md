
---

mindmap-plugin: basic

---

    
# 6. Objects and Data Structures
## Object
- exposes behaviors
- hides data
- easy to add new classes without changing exisiting functions
- The Law of Demeter
  - A module should not know about the innards of the objects it manipulates
  - methods that method f of a class C should only call
    - C
    - An object created by f
    - An object passed as an argument to f
    - An object held in an instance variable of C
  - The method should not invoke methods on objects that are returned by any of the allowed functions
  - Do not make the call like Train Wrecks: a bunch of coupled train cars
    - final String outputDir = ctxt.getOptions().getScratchDir();
  - Do not make Hybrid style(=half object, half data structure)
    - Hybrids make it hard to add new functions but also make it hard to add new data structures
  - Look what the intent of train wreck is and make a behavior to achieve that.
- Data Abstraction
  - Hiding implementation is about abstraction
  - An interface class exposes abstract interfaces that allow its users to manipulate the essence of the data, without having to know its implementation
  - Developers do not want to expose the details of class data
  - Abstraction is not merely accomplished by using interfaces and/or getters and setters. Serious thought need to be put into the best way to represent the data that an object contains
## Object is not always an answer. Data structure is sometimes the answer. 
## Data Structure
- exposes data
- no behaviors
- easy to add new functions without changing the existing data structures
- Data Transfer Objects(DTO)
  - A class with public fields and no methods
  - useful when communicating with databases or parsing messages from sockets and so on
  - The quasi-encapsulation(only getter) provides no other benefit. Do not use that pattern
  - Active Record
    - Special case of DTO
    - public fields(or private fields with setter/getter) and methods(save, find)
    - direct translations from database tables, or other data sources
    - Treat Active Record as a data structure
    - Create separate objects that contain the business rules and that hide their internal data