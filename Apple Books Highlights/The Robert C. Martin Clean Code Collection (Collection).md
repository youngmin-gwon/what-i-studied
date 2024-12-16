## Metadata
- Author: Martin, Robert C.
- [Apple Books Link](ibooks://assetid/955CF6F276092431100C32D5D32097BF)

## Highlights
Classes and objects should have noun or noun phrase names

---
checked exceptions break encapsulation

---
One Assert per Test

---
TEST DOUBLE1 or MOCK OBJECT

---
we are advising you not to pass Maps (or any other interface at a boundary) around your system

---
We are unprofessional.

---
Mandated Comments

---
Get Your Nonthreaded Code Working First

---
better to throw an exception when you encounter an error

---
You might complain that this increases the complexity of the functions, and you’d be right. But that extra syntactic complexity exposes the true temporal complexity of the situation.

---
Misleading Comments

---
The name AccountVisitor means a great deal to a programmer who is familiar with the VISITOR pattern

---
responderBeingTested.

---
A team of developers should agree upon a single formatting style, and then every member of that team should use that style

---
Data structures expose data and have no significant behavior

---
How big should a source file be

---
 we need to make sure that the statements within our function are all at the same level of abstraction

---
someone reading this code has no need for the arcane information contained in the comment

---
Extract Try/Catch Blocks

---
most are very small. Some are a bit larger. Very few contain as much text as a page can hold

---
proxies don’t provide a mechanism for specifying system-wide execution “points” of interest

---
structure is not the only motive for adopting concurrency

---
Duplication may be the root of all evil in software.

---
Testing can be a problem

---
Rather than spend your time writing the comments that explain the mess you’ve made, spend it cleaning that mess.

---
A good way to avoid shared data is to avoid sharing the data in the first place

---
Concurrency can sometimes improve performance, but only when there is a lot of wait time that can be shared between multiple threads or multiple processors. Neither situation is trivial.

---
Objects are abstractions of processing. Threads are abstractions of schedule

---
Each exception that you throw should provide enough context to determine the source and location of an error

---
Patterns

---
Don’t Pass Null

---
Dummy Scopes

---
Position Markers

---
Avoid Transitive Navigation

---
vertical separation should be a measure of how important each is to the understandability of the other

---
TODO Comments

---
Fast

---
Merging them all together into the same function forces the reader to figure out why each section is there and what is being tested by that section

---
aspect-like mechanisms

---
Do not ignore system failures as one-offs

---
If you don’t keep your tests clean, you will lose them. And without them, you lose the very thing that keeps your production code flexible

---
the more tests we write, the more we use principles like DIP and tools like dependency injection, interfaces, and abstraction to minimize coupling

---
we might create too many tiny classes and methods

---
addrFirstName, addrLastName, addrState

---
we often find that developers try to treat these data structures as though they were objects by putting business rule methods in them

---
no other benefit

---
Understand the Algorithm

---
// spaces that could cause the item to be recognized

---
assertEquals(“HBchL”, hw.getState());

---
You should choose names that make the distinction clear, and always use the two forms in a consistent context

---
We’ll put it in a function that’s convenient for us, but not necessarily intuitive to the reader.

---
Objects hide their data behind abstractions and expose functions that operate on that data

---
The functionality that you create today has a good chance of changing in the next release, but the readability of your code will have a profound effect on all the changes that will ever be made

---
How Do You Write Functions Like This

---
choosing good names

---
Structured Programming

---
Tests Enable the -ilities

---
hybrids make it hard to add new functions but also make it hard to add new data structures

---
Go through the previous example and see how difficult it is to verify that they are correct. This explains both why the clarification is necessary and why it’s risky

---
The important thing is for the instance variables to be declared in one well-known place

---
The agility provided by a POJO system with modularized concerns allows us to make optimal, just-in-time decisions, based on the most recent knowledge. The complexity of these decisions is also reduced

---
The ideal is for a source file to contain one, and only one, language.

---
What makes tests readable

---
This isn’t just a matter of aesthetics. The code is better because two concerns that were tangled, the algorithm for device shutdown and error handling, are now separated

---
Avoid using more than one method on a shared object.

---
it should explicitly ask that module for all the information it depends upon

---
the most important way to be expressive is to try

---
Control variables for loops should usually be declared within the loop statement

---
A Dual Standard

---
efficiency

---
Horizontal Openness and Density

---
Gradient gradient = saturateGradient();       List<Spline> splines = reticulateSplines(gradient);       diveForMoog(splines, reason);

---
a module that started well but did not scale.

---
The smaller and more focused a function is, the easier it is to choose a descriptive name

---
authoritative mechanism will usually be either the “main” routine or a special-purpose container

---
We can narrow the type of the exception we catch to match the type that is actually thrown from the FileInputStream constructor:

---
Private functions should be defined just below their first usage

---
Why, then, do so many programmers automatically add getters and setters to their objects

---
Professionalism and craftsmanship come from values that drive disciplines.

---
Hybrids

---
Client-Based Locking

---
comments are, at best, a necessary evil

---
Common problems involve deadlock,15 with threads waiting for a signal to continue that never comes

---
Use Searchable Names

---
all developers feel the pressure to make messes in order to meet deadlines

---
heuristic

---
How small

---
JobQueue

---
many different levels of abstraction

---
The method should not invoke methods on objects that are returned by any of the allowed functions

---
You should take care that your code is nicely formatted

---
Even if you are coding a hypotenuse and hp looks like a good abbreviation, it could be disinformative

---
The problem is that tests must change as the production code evolves

---
Indentation

---
Data structure expose their data and have no meaningful functions

---
We should avoid letting too much of our code know about the third-party particulars

---
Functions Should Descend Only One Level of Abstraction

---
remember you are an author

---
fundamental dichotomy between objects and data structures

---
Enforce design decisions with structure over convention

---
Rather than using the APIs that programmers use to manipulate the system, we build up a set of functions and utilities that make use of those APIs and that make the tests more convenient to write and easier to read

---
It must still be simple, succinct, and expressive, but it need not be as efficient as production code

---
accessors and mutators

---
Avoid creating them

---
The information sent with the exception can distinguish the errors

---
Pick one word for one abstract concept and stick with it

---
Treat Spurious Failures as Candidate Threading Issues

---
You wrap external APIs so that you can throw your own exceptions

---
We want the code to read like a top-down narrative

---
there are frameworks and standards (e.g., “beans”) that demand that even simple data structures have accessors and mutators.

---
Write Your Try-Catch-Finally Statement First

---
Choose clarity over entertainment value

---
How do I write clean code?

---
So if I add a new shape, none of the existing functions are affected, but if I add a new function all of the shapes must be changed

---
Unit tests should be written just before the production code that makes them pass

---
Data Abstraction

---
Prefer Exceptions to Returning Error Codes

---
Encapsulate Boundary Conditions

---
Test code is just as important as production code

---
When classes lose cohesion, split them

---
Systems that aren’t testable aren’t verifiable

---
operating on that argument, transforming it into something else and returning it

---
crisp abstraction

---
it exposes abstract interfaces that allow its users to manipulate the essence of the data, without having to know its implementation

---
Prefer Polymorphism to If/Else or Switch/Case

---
Vertical Openness Between Concepts

---
It is a pity when a comment needs its own explanation

---
take a little pride in your workmanship

---
The name should be simple but explanatory. The name, by itself, should be sufficient to tell us whether we are in the right module or not. The topmost parts of the source file should provide the high-level concepts and algorithms. Detail should increase as we move downward, until at the end we find the lowest level functions and details in the source file

---
Often the best way to gain this knowledge and understanding is to refactor the function into something that is so clean and expressive that it is obvious how it works.

---
we should implement only today’s stories, then refactor and expand the system to implement new stories tomorrow

---
Dependency Injection

---
If a function does only those steps that are one level below the stated name of the function, then the function is doing one thing

---
It is unit tests that keep our code flexible, maintainable, and reusable

---
Javadocs in Public APIs

---
it look like a bunch of coupled train cars

---
Delete it from the system

---
Threads Should Be as Independent as Possible

---
Inaccurate comments are far worse than no comments at all. They delude and mislead

---
Output Arguments

---
Don’t ignore a failure just because the tests pass on a subsequent run

---
expressive and succinct

---
It’s better to depend on something you control than on something you don’t control, lest it end up controlling you

---
it should pass this responsibility to another “authoritative” mechanism, thereby inverting the control

---
Mumbling

---
Let’s say you want to extract one small part of that function into a separate function. However, the code you want to extract uses four of the variables declared in the function. Must you pass all four of those variables into the new function as arguments?Not at all! If we promoted those four variables to instance variables of the class, then we could extract the code without passing any variables at all

---
Affinity might be caused because a group of functions perform a similar operation

---
Mixing levels of abstraction within a function is always confusing

---
it might have been better, and clearer, if this code had been moved to a special class that converted the formats of dates and times.

---
The quasi-encapsulation of beans

---
niladic

---
The strategy of keeping functions small and keeping parameter lists short can sometimes lead to a proliferation of instance variables that are used by a subset of methods. When this happens, it almost always means that there is at least one other class trying to get out of the larger class. You should try to separate the variables and methods into two or more classes such that the new classes are more cohesive

---
Clean code is readable, but it must also be robust

---
 The methods enforce an access policy. You can read the individual coordinates independently, but you must set the coordinates together as an atomic operation

---
Too Much Information

---
TEMPLATE METHOD

---
Use Standard Nomenclature Where Possible

---
The higher your test coverage, the less your fear

---
Your style and discipline survives, even though your code does not

---
The price of checked exceptions is an Open/Closed Principle1 violation

---
it may be in our best interest to write tests for the third-party code we use

---
in most other contexts a single-letter name is a poor choice; it’s just a place holder that the reader must mentally map to the actual concept

---
Before you consider yourself to be done with a function, make sure you understand how it works

---
Beware of using names which vary in small ways

---
Passing a boolean into a function is a truly terrible practice

---
the rational approach is to forbid passing null by default

---
You may not write production code until you have written a failing unit test

---
Create informative error messages and pass them along with your exceptions

---
Coverage tools reports gaps in your testing strategy. They make it easy to find modules, classes, and functions that are insufficiently tested

---
clarity, simplicity, and density of expression

---
Small!

---
think it through and see whether there isn’t some way to turn the tables and express yourself in code

---
The challenge is to balance the needs of both readers and writers to satisfy correct operation, provide reasonable throughput and avoiding starvation

---
Provide Context with Exceptions

---
Server-Based Locking

---
Make Your Threaded Code Pluggable

---
It’s hard to make a small switch statement

---
TDD

---
DSLs, when used effectively, raise the abstraction level above code idioms and design patterns

---
when the Error
enum changes, all those other classes need to be recompiled and redeployed

---
We do this, of course, with polymorphism

---
If you have tests, you do not fear making changes to the code

---
In the context of dependency management, an object should not take responsibility for instantiating dependencies itself

---
Independent

---
most important rules in this book

---
breaking a large function into many smaller functions often gives us the opportunity to split several smaller classes out as well

---
Such dogma should be resisted and a more pragmatic approach adopted

---
Ad infinitum

---
Factories

---
Mature programmers know that the idea that everything is an object is a myth

---
Cohesion

---
we should never let little, convenient idioms lead to modularity breakdown

---
Anything that forces you to check the function signature is equivalent to a double-take. It’s a cognitive break and should be avoided.

---
Command Query Separation

---
We often get the middle of an algorithm right but misjudge the boundaries.

---
unit tests were short bits of throw-away code that we wrote to make sure our programs “worked.”

---
Classes should have a small number of instance variables

---
Even though this is close to a violation of the rule about mental mapping,3 it seems appropriate in this case

---
Run on Different Platforms

---
Single Concept per Test

---
The second presumes that getScratchDirectoryOption() returns a data structure, not an object

---
the refactored program uses function and class declarations as a way to add commentary to the code

---
So accountGroup or bunchOfAccounts or just plain accounts would be better

---
class names including weasel words like Processor or Manager or Super often hint at unfortunate aggregation of responsibilities

---
Make Meaningful Distinctions

---
a book about good programming

---
higher levels of abstraction, the system level

---
Writing Shy Code

---
means that there should only be one return statement in a function, no break or continue statements in a loop, and never, ever, any goto statements.

---
Using Code That Does Not Yet Exist

---
ubiquitous language

---
Lots of very funny code is written because people don’t take the time to understand the algorithm

---
The sheer bulk of those tests, which can rival the size of the production code itself, can present a daunting management problem

---
Optimize Decision Making

---
They confuse the structure of the code and mix error processing with normal processing.

---
minimal

---
IShapeFactory and ShapeFactory?

---
Standards make it easier to reuse ideas and components, recruit people with relevant experience, encapsulate good ideas, and wire components together. However, the process of creating standards can sometimes take too long for industry to wait, and some standards lose touch with the real needs of the adopters they are intended to serve

---
DTOs are very useful structures, especially when communicating with databases or parsing messages from sockets, and so on

---
The client believes it is invoking getAccounts() on a Bank object, but it is actually talking to the outermost of a set of nested DECORATOR14 objects that extend the basic behavior of the Bank POJO

---
Getting software to work and making software clean are two very different activities

---
similar algorithms, but that don’t share similar lines of code

---
Use Unchecked Exceptions

---
In short, they don’t take the time to go fast

---
toString

---
Truth can only be found in one place: the code

---
The first rule of functions is that they should be small. The second rule of functions is that they should be smaller than that

---
F.I.R.S.T

---
One way to separate construction from use is simply to move all aspects of construction to main, or modules called by main, and to design the rest of the system assuming that all objects have been constructed and wired up appropriately

---
We will never be rid of code, because code represents the details of the requirements.

---
Avoid using the same word for two purposes

---
Our goal is to keep our overall system small while we are also keeping our functions and classes small

---
An optimal system architecture consists of modularized domains of concern, each of which is implemented with Plain Old Java (or other) Objects. The different domains are integrated together with minimally invasive Aspects or Aspect-like tools. This architecture can be test-driven, just like the code

---
Functions should either do something or answer something, but not both

---
when its part of the standard library, or in code that you cannot alter, then a helpful clarifying comment can be useful.

---
Rather than venting in a worthless and noisy comment, the programmer should have recognized that his frustration could be resolved by improving the structure of his code

---
So too it is unprofessional for programmers to bend to the will of managers who don’t understand the risks of making messes

---
if (set(”username”, ”unclebob”))

---
by each method is maximally cohesive

---
Do you want your tools organized into tool

---
Structured programming, Aspect Oriented Programming, Component Oriented Programming, are all, in part, strategies for eliminating duplication

---
Unfortunately, most applications don’t separate this concern. The code for the startup process is ad hoc and it is mixed in with the runtime logic

---
Public classes that are not utilities of some other class should not be scoped inside another class. The convention is to make them public at the top level of their package.

---
You will forget to protect one or more of those places—effectively breaking all code that modifies that shared data.

---
TEMPLATE METHOD,4 or STRATEGY5 pattern.

---
restrict the number of such critical sections

---
Clearly, the reportHours method envies the HourlyEmployee class. On the other hand, we don’t want HourlyEmployee to have to know about the format of the report. Moving that format string into the HourlyEmployee class would violate several principles of object oriented design.

---
Producer-Consumer

---
Comments Do Not Make Up for Bad Code

---
Attributions and Bylines

---
Names in software are 90 percent of what make software readable. You need to take the time to choose them wisely and keep them relevant. Names are too important to treat carelessly.

---
little benefit when functions are very small

---
Learning tests verify that the third-party packages we are using work the way we expect them to

---
A client class depending upon concrete details is at risk when those details change

---
because objects are supposed to hide their internal structure, we should not be able to navigate through them

---
once details are mixed with essential concepts, more and more details tend to accrete within the function

---
The relative simplicity makes it easier to ensure that you are implementing the corresponding user stories correctly and to maintain and evolve the code for future stories.

---
Concurrency bugs aren’t usually repeatable, so they are often ignored as one-offs2 instead of the true defects they are.

---
No Duplication

---
Use jiggling strategies to ferret out errors

---
Repeatable

---
here is almost no chance that we’d want Math.max to be polymorphic

---
Error handling is important, but if it obscures logic, it’s wrong

---
the dependency costs outweigh the benefits

---
containers provide mechanisms for invoking factories or for constructing proxies, which could be used for LAZY-EVALUATION and similar optimizations.

---
the professional understands that clarity is king

---
This implies that the blocks within if statements, else statements, while statements, and so on should be one line long. Probably that line should be a function call

---
a lot of conceptual power

---
if you keep your functions small, then the occasional multiple return, break, or continue statement does no harm and can sometimes even be more expressive than the single-entry, single-exit rule.

---
The fact that PAGE_SIZE is declared in HourlyReporter represents a misplaced responsibility [G17] that causes HourlyReporter to assume that it knows what the page size ought to be. Such an assumption is a logical dependency. HourlyReporter depends on the fact that HourlyReportFormatter can deal with page sizes of 55.

---
Clean Tests

---
Well-written unit tests

---
Use Copies of Data

---
clean and robust—code that handles errors with grace and style

---
selectors need not be boolean. They can be enums, integers, or any other type of argument that is used to select the behavior of the function.

---
Method Names

---
Methods should have verb or verb phrase names

---
The problem with these approaches is that they clutter the caller. The caller must check for errors immediately after the call. Unfortunately, it’s easy to forget

---
A source file is a hierarchy rather like an outline

---
//SimpleDateFormat is not thread safe,

---
Things happen when the system switches between tasks

---
beauty

---
switch/case or if/else chain

---
If you are calling a null-returning method from a third-party API, consider wrapping that method with a method that either throws an exception or returns a special case object

---
At all levels of abstraction, the intent should be clear

---
what about the virtues of LAZY-INITIALIZATION? This idiom is still sometimes useful with DI.

---
• Runs all the tests• Contains no duplication• Expresses the intent of the programmer• Minimizes the number of classes and methods

---
you get your thoughts down first, then you massage it until it reads well. The first draft might be clumsy and disorganized, so you wordsmith it and restructure it and refine it until it reads the way you want it to read.

---
Because so few lines of Spring-specific Java code are required, the application is almost completely decoupled from Spring, eliminating all the tight-coupling problems of systems like EJB2

---
HTML Comments

---
most DI containers won’t construct an object until needed

---
polymorphism

---
It might be a request for someone else to think of a better name or a reminder to make a change that is dependent on a planned event

---
Execute with test doubles that run quickly, slowly, variable.

---
I am not afraid to put more than one assert in a test. I think the best thing we can say is that the number of asserts in a test ought to be minimized

---
Don’t Pun

---
To drive this point home, what if you were a doctor and had a patient who demanded that you stop all the silly hand-washing in preparation for surgery because it was taking too much time

---
One way to make this decision is to look at the names of the functions.

---
Journal Comments

---
the intent of getting the absolute path of the scratch directory was to create a scratch file of a given name

---
Conceptual Affinity

---
Keep Synchronized Sections Small

---
Using Third-Party Code

---
If we cannot derive a concise name for a class, then it’s likely too large

---
it is wise to do an exhaustive test of that function. You’ll probably find that the bug was not alone.

---
go ahead and use computer science (CS) terms, algorithm names, pattern names, math terms, and so forth

---
The solution, of course, is to treat the Active Record as a data structure and to create separate objects that contain the business rules and that hide their internal data

---
Because we have construction logic mixed in with normal runtime processing, we should test all execution paths (for example, the null test and its block). Having both of these responsibilities means that the method is doing more than one thing, so we are breaking the Single Responsibility Principle in a small way

---
Exploring and Learning Boundaries

---
Readability

---
conventions

---
so we started our work far away from the unknown part of the code.

---
More precisely, the Law of Demeter says that a method f of a class C should only call the methods of these:• C• An object created by f• An object passed as an argument to f

---
how to write good code. And we’ll know how to transform bad code into good code

---
Temporal couplings are often necessary, but you should not hide the coupling.

---
Notice the complimentary nature of the two definitions. They are virtual opposites

---
Nonlocal Information

---
Spring

---
If you have been a programmer for more than two or three years, you have probably been significantly slowed down by someone else’s messy code

---
The coding style and readability set precedents that continue to affect maintainability and extensibility long after the original code has been changed beyond recognition

---
Keeping Tests Clean

---
We’re essentially doing controlled experiments that check our understanding of that API. The tests focus on what we want out of the API

---
standard nomenclature

---
It will be difficult to determine the source of failures, which are already hard enough to find

---
Unfortunately, most tools for reformatting code are blind to the precedence of operators and impose the same spacing throughout

---
Because of this coupling to the heavyweight container, isolated unit testing is difficult

---
Variables should be declared as close to their usage as possible

---
Inobvious Connection

---
Isolating from Change

---
Avoid Disinformation

---
Single-letter names and numeric constants have a particular problem in that they are not easy to locate across a body of text

---
Calling it ShapeFactoryImp, or even the hideous CShapeFactory, is preferable to encoding the interface

---
This means producers must wait for free space in the queue before writing and consumers must wait until there is something in the queue to consume

---
TODOs are jobs that the programmer thinks should be done, but for some reason can’t do at the moment. It might be a reminder to delete a deprecated feature or a plea for someone else to look at a problem

---
Find and eliminate duplication wherever you can.

---
The startup process is a concern that any application must address. It is the first concern that we will examine in this chapter. The separation of concerns is one of the oldest and most important design techniques in our craft

---
The word list means something specific to programmers

---
elegant

---
We don’t want swarms of +1s and -1s scattered hither and yon.

---
When there is no “programmer-eese” for what you’re doing, use the name from the problem domain

---
Names Should Describe Side-Effects

---
good testing can minimize risk

---
Separate Constructing a System from Using It

---
should be avoided

---
One of the more powerful ways to make a program readable is to break the calculations up into intermediate values that are held in variables with meaningful names.

---
Emphasizing throughput can cause starvation and the accumulation of stale information

---
Inversion of Control moves secondary responsibilities from an object to other objects that are dedicated to the purpose, thereby supporting the Single Responsibility Principle

---
Object-oriented programmers might wrinkle their noses at this and complain that it is procedural

---
Amplification

---
The fewer methods a class has, the better

---
if the keyword try exists in a function, it should be the very first word in the function and that there should be nothing after the catch/finally blocks.

---
The safeties were making it inconvenient to run an experiment.

---
Horizontal Alignment

---
the best rule is that you should minimize the number of asserts per concept and test just one concept per test function

---
One good thing about writing the interface we wish we had is that it’s under our control. This helps keep client code more readable and focused on what it is trying to accomplish

---
they aren’t necessary for the production of robust software

---
Test Drive the System Architecture

---
Design patterns, for example, are largely about communication and expressiveness

---
better than a long descriptive comment

---
When you use exceptions rather than error codes, then new exceptions are derivatives of the exception class. They can be added without forcing any recompilation or redeployment

---
talk to friends, not to strangers

---
being able to recognize good art from bad does not mean that we know how to paint

---
Where do we start when we want to utilize some third-party package

---
the program got a lot longer

---
learning tests

---
Extract functions that explain the intent of the conditional.

---
Follow Standard Conventions

---
Expressive

---
The majority of the cost of a software project is in long-term maintenance

---
should be declared at the top of the class

---
The problem comes in when you decide to call a variable theZork because you already have another variable named zork

---
BUILD-OPERATE-CHECK2 pattern

---
Run-on expressions, Hungarian notation, and magic numbers

---
better programmer

---
Readers-Writers

---
Class Names

---
SRP is often the most abused class design principle

---
any function or class should implement the behaviors that another programmer could reasonably expect.

---
Side effects are lies

---
clean code does one thing

---
Short functions don’t need much description. A well-chosen name for a small function that does one thing is usually better than a comment header

---
If many modules used some form of the statement a.getB().getC(), then it would be difficult to change the design and architecture to interpose a Q between B and C. You’d have to find every instance of a.getB().getC() and convert it to a.getB().getQ().getC()

---
Write tests that have the potential to expose problems and then run them frequently, with different programatic configurations and system configurations and load

---
The fewer variables a function knows about, the better. The fewer instance variables a class has, the better.

---
clean

---
concurrency is hard

---
half object and half data structure

---
Minimal Classes and Methods

---
The code within the testing API does have a different set of engineering standards than production code

---
If you have a constant such as a default or configuration value that is known and expected at a high level of abstraction, do not bury it in a low-level function. Expose it as an argument to that low-level function called from the high-level function

---
different operating systems have different threading policies, each of which impacts the code’s execution

---
It is important to create abstractions that separate higher level general concepts from lower level detailed concepts

---
Run with More Threads Than Processors

---
Use Pronounceable Names

---
Readability is perhaps even more important in unit tests than it is in production code

---
Use Explanatory Variables

---
Bad code tempts the mess to grow

---
many programmers have missed some of the more subtle, and important, points of writing good tests

---
many of these

---
Yet, in practice, you have to spread essentially the same code that implements the persistence strategy across many objects.

---
Then we encoded those rules into the code formatter of our IDE and have stuck with them ever since

---
On the other hand, if I add a new shape, I must change all the functions in Geometry to deal with it

---
Correct concurrency is complex, even for simple problems

---
very convenient seam3 in the code for testing

---
We would like a source file to be like a newspaper article

---
cross-cutting concerns

---
Explanation of Intent

---
Avoid Encodings

---
LeBlanc’s law: Later equals never

---
// format matched kk:mm:ss EEE, MMM dd, yyyy

---
This means that the application is decoupled from the details of how to build a LineItem

---
 ABSTRACT FACTORY

---
POJOs

---
be able to tell the difference between good code and bad code

---
One thread, several threads, varied as it executes

---
The Law of Demeter

---
At the same time, many developers fear that a large number of small, single-purpose classes makes it more difficult to understand the bigger picture

---
given-when-then5 convention

---
Exerting manual control over serialVersionUID may be necessary, but it is always risky. Turning off certain compiler warnings (or all warnings!) may help you get the build to succeed, but at the risk of endless debugging sessions. Turning off failing tests and telling yourself you’ll get them to pass later is as bad as pretending your credit cards are free money.

---
A test suite should test everything that could possibly break. The tests are insufficient so long as there are conditions that have not been explored by the tests or calculations that have not been validated.

---
A long descriptive name

---
Cities also work because they have evolved appropriate levels of abstraction and modularity that make it possible for individuals and the “components” they manage to work effectively, even without understanding the big picture.

---
Hence, the global setup strategy (if there is one) is scattered across the application, with little modularity and often significant duplication

---
t’s bad enough that you must remember what calculateWeeklyPay(false) means whenever you happen to stumble across it

---
Have No Side Effects

---
this kind of alignment is not useful

---
The first “and” is a

---
Use Standards Wisely, When They Add Demonstrable Value

---
a module should not know about the innards of the objects it manipulates

---
Use Intention-Revealing Names

---
Good Comments

---
Class Organization

---
easy to name, easy to write, and easy to understand

---
needs clear separation and tests that define expectations

---
Keep your concurrency-related code separate from other code.

---
Either way our code speaks to us better, promotes internally consistent usage across the boundary, and has fewer maintenance points when the third-party code changes

---
code is really the language in which we ultimately express the requirements

---
Use Exceptions Rather Than Return Codes

---
Where did the constants TENTHS_PER_WEEK and OVERTIME_RATE come from?

---
After all, it runs in a test environment, not a production environment, and those two environment have very different needs

---
A function with two arguments is harder to understand than a monadic function

---
It is a myth that we can get systems “right the first time.”

---
The clearer the author can make the code, the less time others will have to spend understanding it

---
we have to decide—really—whether checked exceptions are worth their price

---
If the tests aren’t self-validating, then failure can become subjective and running the tests can require a long manual evaluation

---
We count responsibilities

---
Encoded names are seldom pronounceable and are easy to mis-type

---
naming is probably the first way of helping determine class

---
Complete test cases, ordered in a reasonable way, expose patterns.

---
Scary Noise

---
Breaking Indentation

---
ad hoc code

---
Use a Coverage Tool

---
The principle of least surprise

---
In principle, each servlet execution lives in its own little world and is decoupled from all the other servlet executions

---
Learning Tests Are Better Than Free

---
The more of your system you can place in such POJOs, the better.

---
Function Headers

---
One or more producer threads create some work and place it in a buffer or queue. One or more consumer threads acquire that work from the queue and complete it

---
The dirtier the tests, the harder they are to change. The more tangled the test code, the more likely it is that you will spend more time cramming new tests into the suite than it takes to write the new production code

---
A programmer without “code-sense” can look at a messy module and recognize the mess but will have no idea what to do about it

---
Use Solution Domain Names

---
Don’t Return Null

---
Whether you are designing systems or individual modules, never forget to use the simplest thing that can possibly work

---
The methods of a class should be interested in the variables and functions of the class they belong to, and not the variables and functions of other classes

---
excruciatingly

---
Programmers must avoid leaving false clues that obscure the meaning of code

---
Hiding Structure

---
a case study

---
Variable Declarations

---
Define Exception Classes in Terms of a Caller’s Needs

---
You may not write more of a unit test than is sufficient to fail, and not compiling is failing

---
Clean Boundaries

---
// the trim is real important.  It removes the starting

---
aborted

---
The changed modules must be rebuilt and redeployed, even though nothing they care about changed

---
From a structural point of view the application looks like many little collaborating computers rather than one big main loop

---
Unfortunately, many programmers have taken this to mean that code is seldom, if ever, a good means for explanation. This is patently false

---
Simple Design Rules 2–4: Refactoring

---
Classes should have one responsibility—one reason to change

---
We had a pretty good idea of where our world ended and the new world began

---
So, like the team I was coaching, you might decide that having dirty tests is better than having no tests

---
Clean code is focused

---
another kind of boundary, one that separates the known from the unknown

---
What this team did not realize was that having dirty tests is equivalent to, if not worse than, having no tests

---
If one module depends upon another, that dependency should be physical, not just logical.

---
Notice that the three steps of the function are one level of abstraction below the stated name of the function

---
Decoupling what from when can dramatically improve both the throughput and structures of an application

---
The learning tests end up costing nothing

---
When tests depend on each other, then the first one to fail causes a cascade of downstream failures, making diagnosis difficult and hiding downstream defects

---
Javadocs in Nonpublic Code

---
“reuse in the small” can cause system complexity to shrink dramatically. Understanding how to achieve reuse in the small is essential to achieving reuse in the large.

---
Don’t Repeat Yourself

---
code should clearly express the intent of its author

---
So it’s our responsibility to make the language look simple

---
Using an output argument instead of a return value for a transformation is confusing

---
the principle of least surprise

---
the refactored program uses longer, more descriptive variable names

---
Although XML can be verbose and hard to read,15 the “policy” specified in these configuration files is simpler than the complicated proxy and aspect logic that is hidden from view and created automatically

---
Self-Validating

---
Add Meaningful Context

---
Limit the Scope of Data

---
So lines of code that are tightly related should appear vertically dense

---
Threaded code interacts with something that can be both real or a test double.

---
Not only does this keep the enclosing function small, but it also adds documentary value because the function called within the block can have a nicely descriptive name

---
If our programming languages were expressive enough, or if we had the talent to subtly wield those languages to express our intent, we would not need comments very much—perhaps not at all

---
They allow the developer to reveal the intent of the code at the appropriate level of abstraction

---
Procedural code (code using data structures) makes it easy to add new functions without changing the existing data structures. OO code, on the other hand, makes it easy to add new classes without changing existing functions

---
There will be times when you must use more than one method on a shared object

---
If your tests aren’t repeatable in any environment, then you’ll always have an excuse for why they fail

---
Note that concerns like persistence tend to cut across the natural object boundaries of a domain

---
Dining Philosophers

---
act as domain-specific language that helps you write the tests

---
Classes Should Be Small

---
How might you increase your chances of catching such rare occurrences

---
 horizontal white space

---
it is a bad idea to prefix every class with GSD

---
Learn these basic algorithms and understand their solutions

---
a cycle that is perhaps thirty seconds long

---
The decoupling of what from when usually has a huge effect on the structure of the system

---
Don’t Skip Trivial Tests

---
We are deeply complicit in the planning of the project and share a great deal of the responsibility for any failures; especially if those failures have to do with bad code

---
Redundant Comments

---
Take data encapsulation to heart; severely limit the access of any data that may be shared

---
Choosing names that reveal intent can make it much easier to understand and change code

---
This is not merely accomplished by using interfaces and/or getters and setters. Serious thought needs to be put into the best way to represent the data that an object contains

---
Data Transfer Objects

---
tests come to a single conclusion that is quick and easy to understand

---
We don’t incur the overhead of construction unless we actually use the object, and our startup times can be faster as a result. We also ensure that null is never returned.

---
Customer and another named CustomerObject

---
writing for readers who will judge your effort

---
Small files are usually easier to understand than large files are

---
separate, small scripting languages or APIs in standard languages that permit code to be written so that it reads like a structured form of prose that a domain expert might write

---
One Level of Abstraction per Function

---
separation of concerns and levels of abstraction

---
their documentary value is higher than the cost to produce them.

---
The Single Responsibility Principle

---
Consider what would happen if a perimeter() function were added to Geometry. The shape classes would be unaffected

---
we would like cohesion to be high

---
it is best to give responsibilities to the most qualified persons

---
However, we’ll first look for a way to maintain privacy

---
Dependencies upon concrete details create challenges for testing our system.

---
Don’t pick names that communicate implementation; choose names the reflect the level of abstraction of the class or function you are working in.

---
Usually they are crutches or excuses for poor code or justifications for insufficient decisions, amounting to little more than the programmer talking to himself

---
Testing Threaded Code

---
It’s certainly not more informative than the code. It does not justify the code, or provide intent or rationale. It is not easier to read than the code

---
we keep our variables private

---
Number-series naming (a1, a2, .. aN) is the opposite of intentional naming

---
the level of abstraction of our languages will continue to increase

---
So having an automated suite of unit tests that cover the production code is the key to keeping your design and architecture as clean as possible

---
Wildcard imports can sometimes cause name conflicts and ambiguities

---
if using copies of objects allows the code to avoid synchronizing, the savings in avoiding the intrinsic lock will likely make up for the additional creation and garbage collection overhead

---
Attempt to partition data into independent subsets than can be operated on by independent threads, possibly in different processors

---
a system with many small classes has no more moving parts than a system with a few large classes

---
The test environment, however, is not likely to be constrained at all

---
all the lower level concepts to be in the derivatives and all the higher level concepts to be in the base class.

---
Active Records are direct translations from database tables, or other data sources

---
our classes lose cohesion because they accumulate more and more instance variables that exist solely to allow a few functions to share them

---
There will be duplication of effort required to make sure everything is effectively guarded (violation of DRY7)

---
Function Arguments

---
Arguments are hard

---
Sometimes, however, we write static functions that should not be static.

---
One might argue that a book about code is somehow behind the times—that code is no longer the issue

---
Spelling similar concepts similarly is information

---
Comments are always failures

---
Loosening encapsulation is always a last resort

---
function is divided into sections such as declarations, initializations, and sieve. This is an obvious symptom of doing more than one thing

---
Commented-Out Code

---
Simple Design Rule 1: Runs All the Tests

---
Good software designs accommodate change without huge investments and rework

---
A powerful mechanism for separating construction from use is Dependency Injection (DI), the application of Inversion of Control (IoC) to dependency management

---
very difficult for programmers to learn to follow this rule and write functions that stay at a single level of abstraction. But learning this trick is also very important

---
Procedural code makes it hard to add new data structures because all the functions must change. OO code makes it hard to add new functions because all the classes must change

---
Horizontal Formatting

---
a design is “simple” if it follows these rules:

---
If you are tempted to return null from a method, consider throwing an exception or returning a SPECIAL CASE object instead

---
This allows ctxt to hide its internals and prevents the current function from having to violate the Law of Demeter by navigating through objects it shouldn’t know about

---
 construction is a very different process from use

---
Explain Yourself in Code

---
Vertical Ordering

---
The Three Laws of TDD

---
A class in which each variable is used

---
Objects expose behavior and hide data

---
The ephemeral nature of software systems makes this possible

---
Switch Statements

---
ABSTRACT FACTORY

---
tests enable change

---
Test-driven development, refactoring, and the clean code

---
Creating a clean system requires the will to eliminate duplication, even in just a few lines of code

---
Leave the campground cleaner than you found it

---
The fact that we have these tests eliminates the fear that cleaning up the code will break it!

---
a change at a low level of the software can force signature changes on many higher levels

---
Care is a precious resource.

---
Don’t rely on your intuition. Look for every boundary condition and write a test for it.

---
The stronger that affinity, the less vertical distance there should be between them

---
Feature Envy

---
what readers expect when they see a function

---
LAZY INITIALIZATION/EVALUATION idiom, and it has several merits

---
 I avoid collapsing scopes down to one line

---
Data/Object Anti-Symmetry

---
objects hide their data and expose operations.

---
making our systems testable pushes us toward a design where our classes are small and single purpose

---
We don’t want lower and higher level concepts mixed together.

---
output arguments should be avoided

---
cut-paste error

---
so too will disciplined developers refactor their test code into more succinct and expressive forms

---
each of which is describing the current level of abstraction and referencing subsequent TO paragraphs at the next level down

---
This code “volume”and complexity are two of the drawbacks of proxies

---
In a clean system we organize our classes so as to reduce the risk of change

---
//so we need to create each instance independently.

---
The class takes no direct steps to resolve its dependencies; it is completely passive

---
 leads to odd statements

---
Whether you need the learning provided by the learning tests or not, a clean boundary should be supported by a set of outbound tests that exercise the interface the same way the production code does.

---
If you can’t pronounce it, you can’t discuss it without sounding like an idiot

---
Concurrency Defense Principles

---
Pure Java AOP Frameworks

---
to accentuate the precedence of operators

---
In order to minimize the potential for defects as we introduce change, it’s critical for us to be able to understand what a system does

---
Output arguments are harder to understand than input arguments

---
Not only are learning tests free, they have a positive return on investment

---
We do not want to expose the details of our data

---
code to be as expressive as possible

---
Single Responsibility Principle

---
Organizing for Change

---
Good software developers understand these issues without prejudice and choose the approach that is best for the job at hand

---
dependency magnet; many other classes must import and use them

---
Pick One Word per Concept

---
a function that is called should be below a function that does the calling

---
expected

---
Separating levels of abstraction is one of the most important functions of refactoring, and it’s one of the hardest to do well.

---
As the mess builds, the productivity of the team continues to decrease, asymptotically approaching zero

---
Know Your Library

---
Avoid Mental Mapping

---
But the real shame of a function like this is that the author missed the opportunity to write the following

---
The primary goal in managing such complexity is to organize it so that a developer knows where to look to find things and need only understand the directly affected complexity at any given time

---
they lie

---
a brief description of the class in about 25 words, without using the words “if,” “and,” “or,” or “but

---
So no true dependency is created by such imports, and they therefore serve to keep our modules less coupled.

---
Use Problem Domain Names

---
Concurrency incurs some overhead

---
the number of domain-specific languages will continue to grow

---
This makes each of those threads behave as if it were the only thread in the world and there were no synchronization requirements.

---
better than a short enigmatic name

---
ADAPTER2

---
Noise Comments

---
Trying to identify responsibilities (reasons to change) often helps us recognize and create better abstractions in our code

---
Vertical Distance

---
Dyads aren’t evil, and you will certainly have to write them

---
Java Proxies

---
Use Descriptive Names

---
it is not sufficient to leave the quotation marks around the word “work.”

---
That’s a lot of knowledge for one function to know. The calling function knows how to navigate through a lot of different objects

---
Every time you see duplication in the code, it represents a missed opportunity for abstraction. That duplication could probably become a subroutine or perhaps another class outright.

---
the essence of iterative and incremental agility

---
How do you know it “works”? Because it passes the test cases you can think of.There is nothing wrong with this approach

---
We can eliminate the duplication by using the TEMPLATE METHOD6 pattern and putting the given/when parts in the base class, and the then parts in different derivatives

---
Proving that code is correct is impractical. Testing does not guarantee correctness

---
Why does this happen to code

---
it is good practice to start with a try-catch-finally statement when you are writing code that could throw exceptions

---
Systems must be clean

---
keeping your functions and classes small

---
readability

---
Noise words are redundant

---
error handing

---
still very useful form for a single argument function, is an event

---
The problem is that too many of us think that we are done once the program works

---
If you use a boundary interface like Map, keep it inside the class, or close family of classes, where it is used

---
the probability that a failing pathway is taken can be star-tlingly low. This makes detection and debugging very difficult

---
The ideal number of arguments for a function is zero

---
Beware Dependencies Between Synchronized Methods

---
you are stating that execution can abort at any point and then resume at the catch

---
Instance variables

---
It’s your job to defend the code with equal passion

---
Good software developers learn to limit what they expose at the interfaces of their classes and modules.

---
base classes should know nothing about their derivatives.

---
the application is in complete control of when the LineItem instances get built and can even provide application-specific constructor arguments

---
All else being equal, we want to eliminate Feature Envy because it exposes the internals of one class to another. Sometimes, however, Feature Envy is a necessary evil.

---
Code changes and evolves. Chunks of it move from here to there. Those chunks bifurcate and reproduce and come together again to form chimeras

---
we used whitespace and formatting techniques to keep the program readable

---
Blocks and Indenting

---
Domain-Specific Testing Language

---
wrapping third-party APIs is a best practice

---
better to extract the bodies of the try and catch blocks out into functions of their own.

---
Bad Comments

---
Team Rules

---
Whether this is a violation of Demeter depends on whether or not ctxt, Options, and ScratchDir are objects or data structures

---
A good DSL minimizes the “communication gap” between a domain concept and the code that implements it, just as agile practices optimize the communications within a team and with the project’s stakeholders

---
You should be able to run all the unit tests with just one command

---
The only way to make the deadline—the only way to go fast—is to keep the code as clean as possible at all times

---
Vertical Formatting

---
There are two very common reasons to pass a single argument into a function

---
every function, and every block within a function, should have one entry and one exit.

---
Vertical Density

---
Imagine that you have a Product class. If you have another called ProductInfo or ProductData, you have made the names different without making them mean anything different

---
 architectures can grow incrementally,
ifwe maintain the proper separation of concerns

---
The first option could lead to an explosion of methods in the ctxt object

---
if you want to go fast, if you want to get done quickly, if you want your code to be easy to write, make it easy to read

---
Concurrency often requires a fundamental change in design strategy.

---
We like to keep our variables and utility functions private, but we’re not fanatic about it

---
A system might have a perfect design on paper, but if there is no simple way to verify that the system actually works as intended, then all the paper effort is questionable.

---
My personal preference is that single-letter names can ONLY be used as local variables inside short methods

---
draconian

---
we could write some tests to explore our understanding of the third-party code

---
It was the bad code that brought the company down

---
Adapted Server

---
Error Handling Is One Thing

---
But don’t make the mistake of thinking that we are somehow “right” in any absolute sense

---
Define the Normal Flow

---
Writing Correct Shut-Down Code Is Hard

---
care

---
There are blank lines that separate the package declaration, the import(s), and each of the functions

---
Concepts that are closely related should be kept vertically close to each other

---
The Agile and TDD movements have encouraged many programmers to write automated unit tests, and more are joining their ranks every day

---
We want our systems to be composed of many small classes, not a few large ones

---
it is better to have many functions than to pass some code into a function to select the behavior.

---
a function that handles errors should do nothing else

---
Our test passes now because we’ve caught the exception. At this point, we can refactor.

---
Each function produces a result that the next function needs, so there is no reasonable way to call them out of order.

---
Closing Brace Comments

---
If the third-party package changes in some way incompatible with our tests, we will find out right away

---
every function that calls our modified function must also be modified either to catch the new exception or to append the appropriate throws clause to its signature

---
This means that the application has no knowledge of main or of the construction process

---
Spring Framework

---
Software systems should separate the startup process, when the application objects are constructed and the dependencies are “wired” together, from the runtime logic that takes over after startup.

---
// as another list.

---
you’d better know just what your container is doing and how to guard against the issues of concurrent update and deadlock described later in this chapter

---
represents additional work, additional risk, and additional unnecessary complexity

---
a hard-coded dependency on MyServiceImpl and everything its constructor requires

---
here is a triad that is not quite so insidious: assertEquals(1.0, amount, .001)

---
If you aren’t very careful, you can create some very nasty situations

---
Clearly it meant something to the author, but the meaning does not come through all that well

---
Notice the direction of the dependency arrows crossing the barrier between main and the application.

---
following a simple and obvious rule that says we need to have tests and run them continuously impacts our system’s adherence to the primary OO goals of low coupling and high cohesion

---
“ONE SWITCH” rule: There may be no more than one switch statement for a given type of selection. The cases in that switch statement must create polymorphic objects that take the place of other such switch statements in the rest of the system.

---
Returning null from methods is bad, but passing null into methods is worse

---
POJOs

---
If you can write your application’s domain logic using POJOs, decoupled from any architecture concerns at the code level, then it is possible to truly test drive your architecture

---
 you need to place names in context for your reader by enclosing them in well-named classes, functions, or namespaces

---
SRP violation

---
Anyone who reads these tests should be able to work out what they do very quickly, without being misled or overwhelmed by details

---
you are tempted to read down the list of variable names without looking at their types

---
tests

---
a class or module should have one, and only one, reason to change

---
some of those arguments ought to be wrapped into a class of their own

---
Replace Magic Numbers with Named Constants

---
How wide should a line be

---
, both in performance as well as writing additional code.

---
Configure tests so they can run for a number of iterations.

---
Kent Beck’s four rules of Simple Design

---
If one function calls another, they should be vertically close, and the caller should be above the callee, if at all possible

---
We can introduce interfaces and abstract classes to help isolate the impact of those details

---
 what this list does do is imply a value system.

---
// Returns an instance of the Responder being tested.   protected abstract Responder responderInstance();

---
It is rather like a gladhanding used-car salesman assuring you that you don’t need to look under the hood

---
Choose Names at the Appropriate Level of Abstraction

---
it is less precise than the code and entices the reader to accept that lack of precision in lieu of true understanding

---
I threw the test code away

---
asking a question about that argument

---
So all the same rules apply. Functions that take variable arguments can be monads, dyads, or even triads. But it would be a mistake to give them more arguments than that

---
TDD asks us to write unit tests first, before we write production code

---
You may not write more production code than is sufficient to pass the currently failing test

---
the more variables a method manipulates the more cohesive that method is to its class

---
Scaling Up

---
The term “Magic Number” does not apply only to numbers.

---
Train Wrecks

---
the things that are hard for OO are easy for procedures, and the things that are hard for procedures are easy for OO

---
Systems Need Domain-Specific Languages

---
So use them very sparingly, and only when the benefit is significant. If you overuse banners, they’ll fall into the background noise and be ignored.

---
without a network

---
When tests run slow, you won’t want to run them frequently

---
Be Precise

---
Hiding implementation is about abstractions

---
Don’t Add Gratuitous Context

---
To include the setups and teardowns, we include setups, then we include the test page content, and then we include the teardowns.To include the setups, we include the suite setup if this is a suite, then we include the regular setup.To include the suite setup, we search the parent hierarchy for the “SuiteSetUp” page and add an include statement with the path of that page.To search the parent…

---
Arguments are even harder from a testing point of view

---
Make Your Threaded Code Tunable

---
One final advantage of wrapping is that you aren’t tied to a particular vendor’s API design choices

---
aspect-like approaches

---
That is the nature of the dual standard. There are things that you might never do in a production environment that are perfectly fine in a test environment

---
Informative Comments

---
Legal Comments

---
It helps us decouple what gets done from when it gets done

---
Make sure your code works outside of threads

---
 Think about shut-down early and get it working early. It’s going to take longer than you expect. Review existing algorithms because this is probably harder than you think

---
Others who see that commented-out code won’t have the courage to delete it

---
Timely

---
The techniques and teachings within are the way that we practice our art

---
Law of Demeter

---
The bad news is that writing clean code is a lot like painting a picture

---
And yet the interface still unmistakably represents a data structure

---
Concurrency is a decoupling strategy

---
This is how architectures become rigid

---
Not only is the purpose of a selector argument difficult to remember, each selector argument combines many functions into one.

---
this rule is the lowest priority of the four rules of Simple Design

---
Do One Thing

---
it is also best to postpone decisions until the last possible moment

---
protected or package scope

---
Warning of Consequences

---
Fortunately, most of the proxy boilerplate can be handled automatically by tools

---
This function does a bit more than get an “oos”; it creates the “oos” if it hasn’t been created already. Thus, a better name might be createOrReturnOos.

---
Variables and function should be defined close to where they are used. Local variables should be declared just above their first usage and should have a small vertical scope. We don’t want local variables declared hundreds of lines distant from their usages.

---
we should strive to keep our lines short

---
difference between objects and data structures

---
A truly awful example of disinformative names would be the use of lower-case L or uppercase O as variable names, especially in combination

---
If you decide to write a comment, then spend the time necessary to make sure it is the best comment you can write