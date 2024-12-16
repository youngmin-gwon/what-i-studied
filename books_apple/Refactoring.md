## Metadata
- Author: Martin Fowler,Kent Beck,John Brant,William Opdyke,Don Roberts
- [Apple Books Link](ibooks://assetid/02C5F22164A1ED4450B26FF7A20CE7D7)

## Highlights
We easily forget that extra user of the code, yet that user is actually the most important

---
a technique for cleaning up code in a more efficient and controlled manner

---
switch statement by using polymorphism

---
To explain intention and implementation separately.

---
Identify a place where it is missing one or more of the benefits of indirection. Put in that indirection without changing the existing behavior.

---
The second thing I want to highlight is that refactoring does not change the observable behavior of the software

---
divide your time between two distinct activities: adding function and refactoring

---
a bad idea to do a switch based on an attribute of another object

---
This is partly for the next time I pass by here, but mostly it’s because I can understand more things if I clarify the code as I’m going along.

---
the first reason to refactor here is to help me understand some code I need to modify

---
Is this not just an aesthetic judgment, a dislike of ugly code? It is until we want to change the system

---
Removing Temps

---
Refactor When You Need to Fix a Bug

---
Any fool can write code that a computer can understand. Good programmers write code that humans can understand.

---
Of these each is not modified by the code but thisAmount is modified

---
Programs that require additional behavior that requires you to change running code are hard to modify.

---
Refactoring Makes Software Easier to Understand

---
I like to get rid of temporary variables such as this as much as possible

---
Pull Up Field (320)

---
Kent Beck’s metaphor of two hats

---
if you do get a bug report, it’s a sign you need refactoring, because the code was not clear enough for you to see there was a bug.

---
Refactoring is one way out of the bind.

---
As I look at amountFor, I can see that it uses information from the rental, but does not use information from the customer.

---
look in the fragment for any variables that are local in scope to the method we are looking at, the local variables and parameters

---
Whenever I have to think to understand what the code is doing, I ask myself if I can refactor the code to make that understanding more immediately apparent.

---
reuse all of the calculation code that was in the original statement method

---
Refactoring is risky

---
insidious in long methods

---
I know which refactorings to use, I know how to use them in a manner that minimizes bugs, and I test at every possible opportunity

---
changing the database schema forces you to migrate the data, which can be a long and fraught task.

---
Design Changes That Are Difficult to Refactor

---
renaming

---
if the code I’m showing you is part of a larger system, then the refactoring soon becomes important

---
I actually change the code to better reflect my understanding, and then I test that understanding by rerunning the code to see if it still works.

---
a sense of the process of refactoring

---
you will then be in a much better position to do something about it, and you will have more options to optimize effectively

---
The other driver of refactoring here is a design that does not help me add a feature easily

---
By clarifying the structure of the program, I clarify certain assumptions I’ve made, to the point at which even I can’t avoid spotting the bugs.

---
Only changes made to make the software easier to understand are refactorings

---
Programs with complex conditional logic are hard to modify.

---
Again each is used and can be passed in as a parameter. The other temp used is frequentRenterPoints. In this case frequentRenterPoints does have a value beforehand. The body of the extracted method doesn’t read the value, however, so we don’t need to pass it in as a parameter as long as we use an appending assignment.


---
one reviewer and the original author

---
easier to work with and move around

---
It’s worth spending the time to build the tests, because the tests give you the security you need to change the program later

---
You can easily lose track of what they are there for

---
I do design reviews with groups and code reviews with individual reviewers.

---
A good contrast is performance optimization

---
Replace Temp with Query (120)

---
To enable sharing of logic.

---
The most important lesson from this example is the rhythm of refactoring: test, small change, test, small change, test, small change

---
When Should You Refactor?

---
temporary variables can be a problem

---
Why do I prefer to pass the length of rental to the movie rather than the movie type to the rental? It’s because the proposed changes are all about adding new types

---
Without a good design, you can progress quickly for a while, but soon the poor design starts to slow you down.

---
Indirection is a two-edged sword, however.

---
thisAmount is now redundant

---
The higher-level classes made certain assumptions about how the classes would work, assumptions that were embodied in inherited code

---
Move Method (142)

---
Move Field (146)

---
Replace Conditional with Polymorphism (255)

---
At this stage the choice of pattern (and name) reflects how you want to think about the structure

---
I’m still human and still make mistakes

---
not object oriented

---
before I do the refactoring I need to figure out how to do it safely

---
the method is on the wrong object

---
simple, even simplistic

---
Was it worth it?

---
My first step is to find a logical clump of code and use Extract Method (110)

---
makes programs hard to work with?

---
Refactoring tends to break big objects into several smaller ones and big methods into several smaller ones.


---
As you develop software, you probably find yourself swapping hats frequently

---
refactoring helps me review someone else’s code

---
key principles of refactoring

---
Extract Class (149)

---
slight flaw

---
Smaller pieces of code tend to make things more manageable

---
switch statement

---
Refactor As You Do a Code Review

---
Refactoring Helps You Find Bugs

---
The First Step in Refactoring

---
Refactoring helps you to make your code more readable.

---
least ripple effect

---
an example of refactoring

---
In a more complex system with a dozen or so price-dependent methods, this would make a big difference

---
By eliminating the duplicates, you ensure that the code says everything once and only once, which is the essence of good design.

---
To encode conditional logic.

---
Any non

---
the purpose of refactoring is to make the software easier to understand and modify

---
to restructure software by applying a series of refactorings without changing its observable behavior

---
Refactoring also helps the code review have more concrete results

---
It is no “silver bullet.” Yet it is a valuable tool, a pair of silver pliers that helps you keep a good grip on your code.

---
Modified variables need more care

---
we haven’t had broad enough experience to see where the limitations apply.

---
State pattern

---
Refactoring changes the programs in small steps. If you make a mistake, it is easy to find the bug.

---
move a field from one class to another, pull some code out of a method to make into its own method, and push some code up or down a hierarchy

---
use Self Encapsulate Field (171)

---
The key to keeping code readable and modifiable

---
Replacing the Conditional Logic on Price Code with Polymorphism

---
Showing code often is not the best device for this. I prefer UML diagrams and walking through scenarios with CRC cards

---
decompose the method into smaller pieces

---
But if I only work for today, I won’t be able to work tomorrow at all.

---
becomes riskier when practiced informally or ad hoc

---
Refactor When You Add Function

---
The other concern with this refactoring lies in performance

---
a framework won’t be right the first time around—it must evolve as they gain experience.

---
To make this process work, you have to have small review groups.

---
 cumulative effect of these small changes

---
verb

---
some of the issues you need to think about in using refactoring

---
Refactoring is the process of taking a running program and adding to its value, not by changing its behavior but by giving it more of these qualities that enable us to continue developing at speed.

---
two definitions

---
same. I need to build a solid set of tests for that section of code

---
With larger design reviews

---
you first copy the code over to rental, adjust it to fit in its new home, and compile

---
Code that communicates its purpose is very important

---
refactoring must be done systematically

---
there is a performance price to pay; here the charge is now calculated twice

---
Changing Interfaces

---
Never be afraid to change the names of things to improve clarity

---
Programs have two kinds of value: what they can do for you today and what they can do for you tomorrow.

---
Extract Method (110)

---
Don’t worry about this while refactoring

---
The harder it is to see the design in the code, the harder it is to preserve it, and the more rapidly it decays

---
a change made to the internal structure of software to make it easier to understand and cheaper to modify without changing its observable behavior

---
usually a small change

---
Refactoring Improves the Design of Software

---
renamed

---
Often this future developer is me

---
Once I’ve refactored, adding the feature can go much more quickly and smoothly.

---
a disciplined way to clean up code that minimizes the chances of introducing bugs

---
The Rule of Three

---
variable names

---
problem?

---
the code will be read and modified more frequently than it will be written

---
Hard because it is hard to figure out where the changes are needed

---
Decomposing and Redistributing the Statement Method

---
We have several types of movie that have different ways of answering the same question. This sounds like a job for subclasses

---
Performance optimization often makes code harder to understand, but you need to do it to get the performance you need

---
the process of changing a software system in such a way that it does not alter the external behavior of the code yet improves its internal structure

---
how refactoring works

---
Queries are accessible to any method in the class and thus encourage a cleaner design without long, complex methods

---
Move Method (142)

---
how to do refactoring in a controlled and efficient manner

---
I’m not a great programmer; I’m just a good programmer with great habits.

---
All these lead to better-distributed responsibilities and code that is easier to maintain

---
When you add function, you shouldn’t be changing existing code

---
Problems with Refactoring

---
When Shouldn’t You Refactor?

---
a tool

---
Programs that have duplicated logic are hard to modify.


---
Databases

---
The users want to make changes to the way they classify movies, but they haven’t yet decided on the change they are going to make

---
he opposite of this practice

---
Refactoring is something you do all the time in little bursts.

---
Refactoring Helps You Program Faster

---
do a similar thing for the frequent renter points

---
Move Method (142)

---
The problem with copying and pasting code comes when you have to change it later.

---
replace totalAmount and frequentRentalPoints with query methods

---
I do this partly to make future enhancements easy, but mostly I do it because I’ve found it’s the fastest way.

---
can set you back days, even weeks

---
Reducing the amount of code does, however, make a big difference in modification of the code. The more code there is, the harder it is to modify correctly.

---
what happens when the charging rules change

---
Programs that are hard to read are hard to modify.

---
An important part of the tests is the way they report their results

---
These changes will affect both the way renters are charged for movies and the way that frequent renter points are calculated

---
New features need more coding as you patch over a patch that patches a patch on the original code base.

---
Given software engineers’ infatuation with indirection, it may not surprise you to learn that most refactoring introduces more indirection into a program.

---
It requires changes to working code that can introduce subtle bugs

---
You can see the difference immediately with the htmlStatement

---
Refactoring is rather like tidying up the code

---
duplicated

---
If you must use a switch statement, it should be on your own data, not on someone else’s.

---
Most refactorings reduce the amount of code, but this one increases it

---
Example

---
locally scoped variables

---
A good design is essential to maintaining speed in software development

---
Is renaming worth the effort? Absolutely. Good code should communicate what it is doing clearly, and variable names are a key to clear code

---
The tests are thus self-checking. It is vital to make tests self-checking

---
tightly coupled to the database schema

---
removing the parameter

---
noun

---
A movie can change its classification during its lifetime. An object cannot change its class during its lifetime

---
the switch statement

---
When you find you have to add a feature to a program, and the program’s code is not structured in a convenient way to add the feature, first refactor the program to make it easy to add the feature, then add the feature

---
Understanding the mechanics of such refactorings is the key to refactoring in a disciplined way.

---
In fixing bugs much of the use of refactoring comes from making code more understandable.

---
Temps are often a problem in that they cause a lot of parameters to be passed around when they don’t have to be

---
Replace Type Code with State/Strategy (227)

---
Is this a state, or is it a strategy?

---
Before you start refactoring, check that you have a solid suite of tests. These tests must be self-checking.

---
The first time you do something, you just do it. The second time you do something similar, you wince at the duplication, but you do the duplicate thing anyway. The third time you do something similar, you refactor.

---
one of the most important was to insist on continuous cleaning up of the code using refactoring

---
To isolate change.

---
intention of the superclass had not been properly understood

---
As the code gets clearer, I find I can see things about the design that I could not see before.

---
polymorphic

---
it is easy to optimize that in the rental class, and you can optimize much more effectively when the code is properly factored

---
although one refactoring can involve others