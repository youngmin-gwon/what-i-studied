---

mindmap-plugin: basic

---

# 7. Testable

## What is
- testable design
   - "A given piece of code should be easy
          and quick to write a unit test against."
   - easy to
      - instantiate classes
      - substitute implementations
      - simulate different scenarios
      - invoke particular execution paths form our test code
   - how?
      - modular design
         - the system is partitioned
                into discrete functional elements
                with their respective responsibilities
                over a specific function or capability
         - it aims at having as few dependencies
                between modules as possible
         - it breaks down overall functionalities into distinct responsibilities
                and assigns those responsibilities to separate components
         - advantages
            - flexibility between components
            - boost of collaboration on larger products
                   thanks to isolating features
            - it enables after-the-fact augmentation of a system,
                   changing ad adding new functionality by merely plugging in
         - SOLID
            - SRP
               - "there should never be more than one reason for a class to change"
               - class should be small, focused, and have a high cohesion
               - code with SRP is easier to approach and understand
                      expected behaviors
                  - it makes easier to test
            - OCP
               - "open for extension but,
                      closed for modification"
               - it can change what a class does
                      without changing its source code
               - it allows tests to substitute a test double
                      when needed to simulate a specific scenario
            - LSP
               - "subclass should be substitutable for their base classes"
               - it is about class hierarchies that exist for the right reason,
                      embodying a valid abstraction, and not merely as a vehicle of code reuse
               - it contributes to testability
                      by enabling the use of contract tests
                  - tests written for an interface that
                        can be executed against all implementations
                        of that interface
            - ISP
               - "many client specific interfaces are better than
                      one general purpose interface"
               - Keep interface small and focused
               - small interface improve testability by
                      making it easier to write and use test doubles
            - DIP
               - "depend on abstraction, not on concretion"
               - class should not instantiate its own collaborators
                      but rather have their interfaces passed in
               - a boon to testability
                  - substituting collaborators properly
                  - it is also made effortless
         - a sufficient collection of mental notes
         - Make the design envision solutions as part of the larger whole
         - Make your test drive your development
            - it minimize duplication
            - it maximize clarity
- untestable design
   - it can't instantiate a class
      - because of collaborators in class,
           especially third-party library
      - conservative visibility modifiers
      - static initialization
   - it can't invoke a method
      - private method
      - opacity
         - you can't figure out what the method
              expects to receive as its arguments
         - ex) Map
   - it can't observe the outcome
      - you don't know the right things happened afterward
         - void
      - incapable of intercepting the interaction
           you are interested in
         - collaborator is hard-wired into the method,
              so it cannot be substituted with test double
   - it can't substitute a collaborator
      - production code has
           a hardcoded *new Collaborator()*
           where you want to test its interaction
           with that particular collaborator
      - a method chain,
           demeter's law
         - you need a chain of test doubles to test
   - it can't override a method
      - **private, final, static** keywords

## Guidelines
- Avoid complex private methods
   - you fell you don't need to test your private method directly
   - it means
      - you should not test private method directly
      - ! you should not test your private method
         - trivial utility and shorthand
             to make your public class read well
   - Refactor the private method to public as it should,
       or move encapsulated logic to another responsible object
- Avoid final methods
   - Get rid of it if the keyword *final* interfere testability
- Avoid static methods
   - case
      - method does not relate to a specific instance of a class
      - we could not bother figuring out where it belongs
      - we want to make it easier to provide global access to the method
   - Do not make method static
      if you foresee that you might want to
      stub it out in a unit test one day
   - Create an object that
      provides that functionality through an instance method
- Use new with care
   - Every time you "new up" an object,
      you are nailing down its exact implementation
   - Pass the object into the method
      rather than instantiating it within the method 
      if it is a true collaborator
- Avoid logic in constructors
   - constructor is hard to bypass because
      a subclass's constructor will always trigger
      at least one of the superclass constructors
   - Extract all of the logic into protected methods
      that can be overridden by subclasses
- Avoid the Singleton
   - it is hard to mock
   - Make a promise in team
      that team will only instantiate
      one of objects in production 
      rather than singleton
- Favor composition over inheritance
   - inheritance does allow you to reuse code
      but it also brings a rigid class hierarchy that 
      inhibits testability
   - the point of inheritance is
      to take advantage of polymorphic behavior 
      NOT to reuse code
- Wrap external libraries
   - Be extremely wary of inheriting from
      classes in third-party libraries
   - Think twice before scattering direct calls
      to an external library throughout your code base
   - Wrap the library behind your own interface
      that is test-friendly and makes it easy to substitute
- Avoid service lookups
   - like acquiring a singleton instance
      through a static method
   - dependency is hidden within the class
      - harder to stub than constructor parameters
      - stubbing out a service lookup implies an extra code
   - passing dependencies explicitly through the constructor
      is a natural, straightforward means
      to wire up objects with their collaborators
      - too many arguments in constructor?
         - Use parameter object