## Metadata
- Author: Vernon, Vaughn
- [Apple Books Link](ibooks://assetid/3D684B9434F257F160F1781A092A47B3)

## Highlights
DDD is about discussion, listening, understanding, discovery, and business value, all in an effort to centralize knowledge.

---
Remember, the efforts in developing the solutions in the Core Domain are a key business investment!

---
using one of the DDD strategic design tools, we can to some degree cut through the complexity by externally dissecting these intertwined models into logically separated Subdomains according to their actual functionality

---
It provides a context for the Ubiquitous Language that is spoken by the team and expressed in its carefully designed software model

---
• What is the name of and vision for the strategic Core Domain?• What concepts should be considered part of the strategic Core Domain?• What are the necessary Supporting Subdomains and the Generic Subdomains?• Who should do the work in each area of the domain?• Can the right teams be assembled?

---
deeper understanding of their Core Domain

---
Bounded Contexts are relatively small, smaller than we might at first imagine. A Bounded Context is large enough only to capture the complete Ubiquitous Language of the isolated business domain, and no larger.

---
test data must be realistic and support and enhance the desired expressiveness

---
This book is about helping you correctly implement DDD

---
Here we really need to think in terms of cleanly separated Bounded Contexts because we are looking at the Ubiquitous Language of each

---
Is there a clean distinction between an Item being ordered, one being received, one in stock, and one moving out of stock?

---
We can now use this method to save a Customer under at least a dozen business situations, and more! But is that really a good thing? How could we actually test this method to ensure that it doesn’t save a Customer under the wrong situations?

---
It is not about creating a real-world model, as in trying to mimic reality

---
how to cut through the complexity barrier to use Aggregates that create consistency boundaries around small object clusters

---
Head First Design Patterns


---
architecture is better organized

---
hexagonal architecture

---
Clean boundaries

---
proper expressiveness using the Ubiquitous Language

---
Chapter 8: Domain Events

---
That’s why in the end it is team speech and the model in the code that are the most enduring and the only guaranteed current denotations of the Ubiquitous Language.

---
more thought is needed to create the BacklogItem of the second example than that of the first.

---
These kinds of Subdomains are important to the success of the business, yet there is no need for the business to excel in these areas

---
more technically driven benefits

---
Context Maps are a powerful tool to help a team understand their business domain, the boundaries between distinct models, and how they are currently, or can be, integrated

---
The Language may start out with terms that are the natural lingo of the domain experts, but it isn’t limited to that because the Language must grow over time

---
Context Maps

---
understanding where Factories should exist

---
Chapter 14: Application

---
utmost importance to the ongoing success of the business

---
how can we use the more modern modularization facilities, such as OSGi and Jigsaw, provided by languages and frameworks?

---
making software that is as close as possible to what the business leaders and experts would create if they were the coders

---
Keep problem space assessment high-level, but make it thorough.

---
Chapter 12: Repositories

---
Subdomains

---
If it models some aspect of the business that is essential, yet not Core, it is a Supporting Subdomain

---
The Ubiquitous Language is a shared language developed by the team—a team composed of both domain experts and software developers.

---
strategic business challenge to be solved

---
Agile, iterative, continuous modeling

---
DDD is not a heavyweight, high-ceremony design and development process. DDD is not about drawing diagrams

---
must remain transactionally consistent throughout the Aggregate’s lifetime

---
Thus, your team and management will have to determine if a system you are planning to work on deserves the cost of making a DDD investment.

---
zero translations

---
software development experience doesn’t give you the ability to listen and learn from domain experts, the people who know the most about some high-priority area of the business

---
the benefits of using DDD and how to achieve the most from it

---
Justification for Domain Modeling

---
a Domain, a Subdomain, and a Core Domain

---
Remember that if you design your Modules mechanically rather than according to the Ubiquitous Language, they will probably do more harm than good

---
What you may like best about DDD is that the domain experts are also going to have to listen to you

---
Chapter 5: Entities

---
designing a worthy Factory in a DDD setting

---
strategic modeling mindset

---
Domain Events

---
Changing the way developers think about solutions in their domain

---
A better user experience

---
The implementation of saveCustomer() itself adds hidden complexity

---
The use of the word ubiquitous is not an attempt to describe some kind of enterprise-wide, company-wide, or worldwide, universal domain language.

---
your problem space is the combination of the Core Domain and the Subdomains it must use

---
The Subdomains in the problem space are usually different from project to project since they are used to explore a current strategic business problem

---
software model of the very specific business domain you are working in.

---
Domain

---
The honest answer to almost any question in software development is, “It depends.”

---
 If you are developing a Supporting Subdomain that, for various reasons, cannot be acquired as a third-party Generic Subdomain, it is possible that the tactical patterns would benefit your efforts

---
Implement each domain object behavior until the test passes

---
They have both a problem space and a solution space

---
causing the creation of two models in one

---
When we model a domain through software, we are required to give careful thought to which model objects do what. It’s about designing the behaviors of objects

---
circle back with the rest of the team to review the resulting phrases

---
iterative and incremental

---
how to design Entities well. How do we express the Ubiquitous Language with an Entity? How are Entities tested, implemented, and persisted?

---
Context Mapping

---
 Value Object design from several angles, discussing how to identify the special characteristics in the model as a means to determine when to use a Value rather than an Entity

---
A Bounded Context is a conceptual boundary where a domain model is applicable

---
I think the best justification for using any technology or technique is to provide value to the business

---
If you think that design is a dirty word when agile is in practice, it’s not with DDD. Using DDD with agile is completely natural. Always keep design in check with agile. Design need not be heavy.

---
Summary

---
There is little intention revealed

---
why strategic design is so essential, and why designing without it hurts

---
Why Strategic Design Is So Incredibly Essential

---
Using DDD, models are developed in Bounded Contexts.

---
developing a Domain Model is actually one way that we focus on only one specific

---
document-based and key-value storage

---
Domain experts contribute to software design

---
Chapter 4: Architecture

---
While modularization is an essential DDD modeling tool, it doesn’t fix linguistic misalignment

---
You can actually teach the business more about itself

---
Bounded Context,

---
 The premise is that this approach simplifies persistence and allows capturing concepts with complex behavioral properties, besides the far-reaching influence the Events themselves can have on your own and external systems.

---
It is about carefully refining the mental model of domain experts into a useful model for the business

---
how we will implement the software to solve the problem of the business challenge

---
everybody learns because everybody contributes to discovery discussions.

---
Domain can refer to both the entire domain of the business, as well as just one core or supporting area of it

---
Chapter 10: Aggregates

---
As you search for answers, you learn that nobody can explain why this one method works the way it does, or how many correct uses there are.

---
Consider the following short list of more detailed decision parameters

---
Here’s some practical guidance. I begin with the high-level ones and progress to more details:

---
How to Do DDD

---
how to design a Repository that is used with an ORM, one that supports the Coherence grid-based distributed cache, and one that uses a NoSQL key-value store

---
what made the best modeling choice stand out even more boldly was the realization that the team’s next Core Domain project would have very similar role-based access needs and would lean on the use of domain-specific role characteristics. Clearly, Users and Roles were truly part of a Supporting or Generic Subdomain that had an enterprise-wide, and even customer-facing, part to play in the fut

---
To succeed in implementing DDD, you have to get these right

---
Chapter 6: Value Objects

---
The design is the code, and the code is the design

---
Rules of thumb don’t have to be right in all cases

---
Context Map

---
Chapter 7: Services

---
Since team speech and the code will be the lasting expression of the Ubiquitous Language, be prepared to abandon the drawings, glossary, and other documentation that will be difficult to keep up-to-date with the spoken Ubiquitous Language and source code as they are rapidly enhanced.

---
Later you also add tests that verify the correctness of the new domain object from every possible (and practical) angle

---
time and effort required to create a Ubiquitous Language

---
Here are some questions that should be answered in order to steer your project in the right direction

---
Never use DDD to make your solution more complex.

---
DDD meets the real technical demands of the software by using tactical design modeling tools to analyze and develop the executable software deliverables

---
Chapter 2: Domains, Subdomains, and Bounded Contexts

---
If you don’t like the idea of a glossary, still capture some kind of documentation that includes the informal drawings of important software concepts

---
Design Patterns

---
Chapter 1: Getting Started with DDD

---
First we want to focus on how the model will be used by clients, and these tests drive the model’s design

---
software developers are typically drawn to technology and technical solutions to business problems. It’s not that software developers have wrong motivations; it’s just what tends to grab their attention

---
implicit, completely subjective code “design.”

---
Demonstrate the code to team members

---
how to determine when to model a concept as a fine-grained, stateless Service that lives in the domain model

---
The solution space is one or more Bounded Contexts, a set of specific software models

---
Chapter 9: Modules

---
Draw pictures of the physical and conceptual domain and label them with names and actions

---
DDD Is Not Heavy

---
gains a useful model of its domain

---
It helps define the best inter-team organizational relationships and provides early-warning systems for recognizing when a given relationship could cause software and even project failure.

---
When using DDD, we’d leave none of it to guesswork.

---
A good portion of our industry is made up of sample code followers

---
if it captures nothing special to the business, yet is required for the overall business solution, it is a Generic Subdomain

---
why Domain Events published by the model are so powerful, and the diverse ways that they can be used, even in supporting integration and autonomous business services

---
There is one Ubiquitous Language per Bounded Context.

---
If there is a single “invention” Evans delivers to the software development community, it is the Ubiquitous Language

---
Chapter 11: Factories

---
Without going into extensive detail, this method could function incorrectly in more ways than it could correctly.

---
Event Sourcing

---
Ubiquitous Language

---
A Core Domain is a part of the business Domain that is of primary importance to the success of the organization

---
A domain that may become a Generic Subdomain (2) or Supporting Subdomain to its consumers may actually be a Core Domain to your business.

---
If a Bounded Context is being developed as the Core Domain, it is strategically vital to the success of the business.

---
Big Ball of Mud

---
Write a test

---
How DDD Helps

---
Ubiquitous, but Not Universal

---
How do the Application Services and infrastructure work?

---
Centralizing knowledge

---
the solution space

---
Create a glossary of terms with simple definitions

---
your strategically and tactically designed domain models should be architecturally neutral

---
Be sure that all stakeholders are aligned with and committed to successfully delivering on the vision

---
DDD provides sound software development techniques that address both strategic and tactical design.

---
how do other members of your team design the areas of the application that surround the model? Should they use DTOs to transfer data between the model and the user interface? Or are there other options for conveying model state up to the presentation components?

---
realistic business value of employing DDD

---
If you try to apply a single Ubiquitous Language to an entire enterprise, or worse, universally among many enterprises, you

---
will fail.

---
Yet oversimplified sample code, which usually demonstrates with a lot of getters and setters, is copied every day without a second thought about design

---
vigorously separating distinct areas of the whole business domain will help us succeed

---
Refactor both

---
aggregate-oriented storage.

---
how to create a Publish-Subscribe mechanism, how Domain Events are published to integrated subscribers across the enterprise, ways to create and manage an Event Store, and how to properly deal with common messaging challenges faced.

---
Did you notice the name Collaboration Context used here? This is the way we name a Bounded Context, which is in the form Name-of-Model Context

---
This does not mean that effort is spent on modeling the “real world.” Rather, DDD delivers a model that is the most useful to the business.

---
you are interested in the correctness of the expression of a domain concept that is embodied in the new domain object

---
Involving domain experts at the outset and continuously with the project

---
Remember: Ask the Domain Experts!

---
the role of Values in integration and modeling Standard Types

---
Domain Model

---
common challenges and how do we justify using DDD as we face them

---
how to use DDD within such architectures as Hexagonal (Ports and Adapters), Service-Oriented, REST, CQRS, Event-Driven (Pipes and Filters, Long-Running Processes or Sagas, Event Sourcing), and Data Fabric/Grid-Based

---
When you have a good understanding of the problem space, you then turn to the solution space

---
Why You Should Do DDD

---
Put domain experts and developers on a level playing field, which produces software that makes perfect sense to the business, not just the coders

---
designing from the model client’s perspective adds a very desirable dimension

---
One of the most important patterns of tactical design is Aggregate (10)

---
Use DDD to Simplify, Not to Complicate

---
a few different ways to implement model integrations using Context Mapping

---
How do we organize model objects into right-sized containers with limited coupling to objects that are in different containers? How do we name these containers so they reflect the Ubiquitous Language?

---
• What software assets already exist, and can they be reused?• What assets need to be acquired or created?• How are all of these connected to each other, or integrated?• What additional integration will be needed?• Given the existing assets and those that need to be created, what is the required effort?• Do the strategic initiative and all supporting projects have a high probability of success, or will any one of them cause the overall program to be delayed or even fail?• Where are the terms of the Ubiquitous Languages involved completely different?• Where is there overlap and sharing of concepts and data between Bounded Contexts?• How are shared terms and/or overlapping concepts mapped and translated between the Bounded Contexts?• Which Bounded Context contains the concepts that address the Core Domain and which of the [Evans] tactical patterns will be used to model it?

---
one cannot properly stand without the other.

---
It’s just that there are times when thinking less technically is better

---
Remember to prioritize correctly, placing more emphasis on the domain model, which has greater business value and will be more enduring

---
Bounded Context

---
This makes Subdomains a very useful tool in assessing the problem space

---
Chapter 3: Context Maps

---
how do you capture this all-important Ubiquitous Language?

---
how to design domain-centric tests, how to implement Value types, and how to avoid the bad influence persistence mechanisms can have on our need to store them as part of an Aggregate

---
how does an organization justify tactical domain modeling?

---
Use Domain Events (8) to indicate the occurrence of significant happenings in the domain

---
We can conceptually divide a single, large Bounded Context using two or more Subdomains, or multiple Bounded Contexts as part of a single Subdomain

---
A refined, precise definition and understanding of the business

---
well

---
The team was now grasping that determining who can do something is the concern of a completely separate model, and the core collaboration model only needed to know that any question regarding who can do what had already been answered

---
New tools, both strategic and tactical

---
Bounded Contexts

---
The Bounded Context is used to realize a solution as software

---
But collaboration tools should be interested in the roles of users, rather than who they specifically are and each little action they are permitted to perform

---
That’s because the Bounded Context is a specific solution, a realization view, once developed

---
Does anyone remember its original intent, and all the motivations for changing it to support a wide variety of business goals?

---
The problem space

---
The Customer “domain object” isn’t really an object at all. It’s really just a dumb data holder.

---
even if we could produce completely bug-free software, that in itself does not necessarily mean that a quality software model is designed

---
when you should design a Service instead of an Entity or Value Object, and how Domain Services can be implemented to handle business domain logic as well as for technical integration purposes

---
Create the new domain objec

---
Just as any human language reflects the minds of those who speak it, the Ubiquitous Language reflects the mental model of the experts of the business domain you are working in

---
Chapter 13: Integrating Bounded Contexts

---
software that reflects the mental model of the business experts

---
we can reach higher for a well-designed software model that explicitly reflects the intended business objective