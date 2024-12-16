## Metadata
- Author: Kent Beck
- [Apple Books Link](ibooks://assetid/A4846BE6BE578C359B254DD7DEBE933F)

## Highlights
Value Object

---
The test above is not one I would expect to live a long time. It is deeply concerned with the implementation of our operation, rather than its externally visible behavior.

---
Factory Method

---
How do you create an object when you want flexibility in creating new objects? Create the object in a method instead of using a constructor.

---
Refactor— Eliminate all of the duplication created in merely getting the test to work

---
External Fixture

---
Clean code that works

---
a leap-of-faith refactoring is exactly what we're trying to avoid with our strategy of small steps and concrete feedback.

---
Template Method

        How do you represent the invariant sequence of a computation while providing for future refinement? Write a method that is implemented entirely in terms of other methods.

---
Test List

---
can write reliable, bug-free code no matter what its level of complexity

---
don't have a list of ten items as the input data if a list of three items will lead you to the same design and implementation decisions.

---
if we need to have a direction in our metaphor, then known-to-unknown is a helpful description

---
fear in the legitimate, this-is-a-hard-problem-and-I-can't-see-the-end-from-the-beginning sense

---
Tested for that operation

---
Dependency is the key problem in software development at all scales

---
Do we want to make this change now, or will we wait?

---
Inline Method

        How do you simplify control flows that have become too twisted or scattered? Replace a method invocation with the method itself.

---
Fake It ('Til You Make It)

---
If you only take larger steps, you'll never know if smaller steps are appropriate

---
Made a list of the tests we knew we needed to have working
          

          
            Told a story with a snippet of code about how we wanted to view one operation
          

          
            Ignored the details of JUnit for the moment
          

          
            Made the test compile with stubs
          

          
            Made the test run by committing horrible sins
          

          
            Gradually generalized the working code, replacing constants with variables
          

          
            Added items to our to-do list rather than addressing them all at once

---
Triangulate

---
Fear makes you shy away from feedback

---
Reconcile Differences

        How do you unify two similar looking pieces of code? Gradually bring them closer. Unify them only when they are absolutely identical.

---
How do you represent special cases using objects? Create an object representing the special case. Give it the same protocol as the regular objects.

---
 when we triangulate, we only generalize code when we have two examples or more

---
Migrate Data

        How do you move from one representation? Temporarily duplicate the data.

---
Create tests using xUnit, the architecture at the heart of many programmer-oriented testing tools.

---
Starting with one concrete example and generalizing from there prevents you from prematurely confusing yourself with extraneous concerns

---
No client code knows that there is a subclass called Dollar

---
Test-driven development is a set of techniques that any software engineer can follow, which encourages simple designs and test suites that inspire confidence

---
Another implication is that Value Objects should implement equals()

---
Isolating tests encourages you to compose solutions out of many highly cohesive, loosely coupled objects

---
Even worse, made the test work by copying and editing model code wholesale
          

          
            

---
Grow a design organically by refactoring to add design decisions one at a time

---
it's best to stay on track

---
the problem with the test and code as it sits is not duplication

---
When do you write tests for externally produced software? Before the first time you are going to use a new facility in the package.

---
Couldn't tackle a big test, so we invented a small test that represented progress

---
Solving "clean code" at the same time that you solve "that works" can be too much to do at once. As soon as it is, go back to solving "that works," and then "clean code" at leisure.

---
TDD is an awareness of the gap between decision and feedback during programming, and techniques to control that gap

---
How do you introduce a new variation into a computation? Introduce a new object with the same protocol as an existing object but a different implementation.

---
What do we mean by testing?
          

          
            When do we test?
          

          
            How do we choose what logic to test?
          

          
            How do we choose what data to test?

---
you don't have to worry about aliasing problems

---
Green— Make the test work quickly, committing whatever sins necessary in the process

---
Why

---
 testing changes is not the same as having tests

---
"What is the right answer?" and "How am I going to check?"

        

---
Unless you have reason to distrust it, don't test code from others

---
Instead of being tentative, begin learning concretely as quickly as possible

---
Testing Patterns

---
What physical setup should you use for TDD? Get a really nice chair, skimping on the rest of the furniture if necessary.

---
Be prepared to downshift if your brain starts writing checks your fingers can't cash.

---
The problem is the dependency between the code and the test

---
By decoupling the tests from the existence of the subclasses, we have given ourselves freedom to change inheritance without affecting any model code

---
Template methods are best found through experience instead of designed that way from the beginning. Whenever I say to myself, "Ah, this is the sequence and here are the details," I always find myself inlining the detail methods later and re-extracting the truly variant parts.

---
One solution is never to give out the objects that you rely on, but instead always make copies.

---
Fear makes you want to communicate less

---
How do you implement an operation that works with collections of objects? Implement it without the collections first, then make it work with collections.

        

---
Promised ourselves we wouldn't go home until the duplication was gone
          
        

---
When implementing a Value Object, every operation has to return a fresh object, leaving the original unchanged. Users have to be aware that they are using a Value Object and store the result (as in the preceding above.) All of these object allocations can create performance problems, which should be handled like all performance problems, when you have realistic data sets, realistic usage patterns, profiling data, and complaints about performance.

---
Log Strings are particularly useful when you are implementing Observer and you expect notifications to come in a certain order

---
Removing duplication between test and code as a way to drive the design

---
Use Obvious Implementation

---
Red— Write a little test that doesn't work, and perhaps doesn't even compile at first

---
How do you most conservatively drive abstraction with tests? Abstract only when you have two or more examples.

        

---
Not so fast, hacker boy (or girl). The cycle isn't complete. There are very few inputs in the world that will cause such a limited, such a smelly, such a naïve implementation to pass. We need to generalize before we move on. Remember, the cycle is as follows.

        
          
            

---
If the tests didn't run, then there was no sense running the application because it certainly wouldn't run. Once the tests ran, the application ran every time.

---
How do you implement simple operations? Just implement them.

---
We aren't striving for perfection. By saying everything two ways—both as code and as tests—we hope to reduce our defects enough to move forward with confidence

---
There is no need to test third party code or code generated by external tools

---
Command

---
Test is also a noun, "a procedure leading to acceptance or rejection."

---
Collecting Parameter

        How do you collect the results of an operation that is spread over several objects? Add a parameter to the operation in which the results will be collected.

---
You will occasionally find a test broken in the integration suite when you try to check in. What to do?

        The simplest rule is to just throw away your work and start over.

---
The output should be the same as the input. Some configurations of polygons are already normalized, incapable of further reduction.
          

          
            The input should be as small as possible, like a single polygon, or even an empty list of polygons.

---
I've been working with "outlines" in practically everything I do lately

---
Once you have the test running, gradually transform the constant into an expression using variables.

---
How do you get a test case running that turns out to be too big? Write a smaller test case that represents the broken part of the bigger test case. Get the smaller test case running. Reintroduce the larger test case.

---
Include expected and actual results in the test itself, and try to make their relationship apparent.

---
What if we adopted the rule that we would always test first?

---
An alternative is to notice that we are about to use a new method of a new class. Instead of just using it, we write a little test that verifies that the API works as expected. 

---
make it bold

---
Test Data

---
Write automated tests

---
I find that my Starter Test is often at a higher level, more like an application test, than the following tests.

---
Isolate Change

        How do you change one part of a multi-part method or object? First, isolate the part that has to change.

---
Scope control

---
If dependency is the problem, duplication is the symptom

---
a predictable way to develop

---
Assertion

---
an order to the tasks of programming

---
Extract Object

---
How do you spread the use of automated testing? Ask for and give explanations in terms of tests.

        

---
Another solution is to treat the object as less than an object

---
All Value Objects have to implement equality

---
The second time you see a conditional, it is time to pull out the most basic of object design moves, the Pluggable Object.

---
The tests in test-driven development are the teeth of the ratchet

---
Used functionality just developed to improve a test
          

          
            Noticed that if two tests fail at once we're sunk
          

          
            Proceeded in spite of the risk
          

          
            Used new functionality in the object under test to reduce coupling between the tests and the code
          
        

---
Unlike most problems in life, where eliminating the symptoms only makes the problem pop up elsewhere in worse form, eliminating duplication in programs eliminates dependency

---
Start simply

---
Design Patterns

---
One alternative is to have a single class with a switch statement. Depending on the value of a field, you invoke different methods. However, the name of the method appears in three places:

        
          
            The creation of the instance
          

          
            The switch statement
          

          
            The method itself

---
Our designs must consist of many highly cohesive, loosely coupled components, just to make testing easy

---
Courage

---
Make it right

---
If the defect density can be reduced enough, then quality assurance (QA) can shift from reactive work to proactive work

---
We are about to see the results on the screen.
          

          
            Because toString() is used only for debug output, the risk of it failing is low.
          

          
            We already have a red bar, and we'd prefer not to write a test when we have a red bar.
          
        

        

---
We must write our own tests, because we can't wait 20 times per day for someone else to write a test

---
What should you test

---
When I write tests, I first create a short outline of the tests I want to write

---
What do you do when you have ten subclasses of a class, each implementing only one method? Subclassing is a heavyweight mechanism for capturing such a small amount of variation.
        

---
Red Bar Patterns

        These patterns are about when you write tests, where you write tests, and when you stop writing tests.

---
XP says, "Here are things you must be able to do to be prepared to evolve further.

---
We must design organically, with running code providing feedback between decisions

---
How do you test for expected exceptions? Catch expected exceptions and ignore them, failing only if the exception isn't thrown.

---
If the number of nasty surprises can be reduced enough, then project managers can estimate accurately enough to involve real customers in daily development

---
How do you release external resources in the fixture? Override tearDown() and release the resources.

---
Test-driven development is a way of managing fear during programming

---
factory method in Money

---
When I test assert-first, I find it has a powerful simplifying effect.

---
Our goal is to be able to write another test that "makes sense" to us, without having to change the code, something that is not possible with the current implementation.

              

---
confidence-giving tests and carefully factored code give us preparation for insight, and preparation for applying that insight when it comes

---
 Sometimes you are sure you know how to implement an operation. Go ahead

---
it further might be possible to dramatically reduce the defect density of code and make the subject of work crystal clear to all involved

---
when the design thoughts just aren't coming, Triangulation provides a chance to think about the problem from a slightly different direction

---
It lets your teammates count on you, and you on them

---
tests should be able to ignore one another completely

---
Fixture

---
How do you test that the sequence in which messages are called is correct? Keep a log in a string, and append to the string when a message is called.

---
Evident Data

---
What if I got to rewrite everything I ever wrote 20 times? Would I keep finding insight and surprise every time? Is there some way to be more mindful as I program so I can squeeze all the insight out of the first three times? The first time?
      
    
  

---
What data do you use for test-first tests?

---
Log String

---
Our development environment must provide rapid response to small changes

---
Fake It

---
Eliminate duplication

---
You have an obvious, concrete bookmark to help you remember what you were thinking; and making that test work should be quick work, so you'll quickly get your feet back on that victory road.

---
Implemented it simply

---
Where does the functionality belong? Is it a modification of an existing method, a new method on an existing class, an existing method name implemented in a new place, or a new class?
          

          
            What should the names be called?
          

          
            How are you going to check for the right answer?
          

          
            What is the right answer?
          

          
            What other tests does this test suggest?

---
How do you test an object that relies on an expensive or complicated resource? Create a fake version of the resource that answers constants.

        

---
Another value of mocks, aside from performance and reliability, is readability

---
write a list of all the tests you know you will have to write

---
 a proven set of techniques that encourage simple designs and test suites that inspire confidence

---
What is your first implementation once you have a broken test? Return a constant.

---
I really didn't expect the metaphor to be so powerful.

---
As soon as I get an unexpected red bar, I back up, shift to faking implementations, and refactor to the right code

---
What do you do when you are feeling lost? Throw away the code and start over.

---
If I noticed I was getting surprised by red bars, then I would go to smaller steps.

---
Write new code only if an automated test has failed

---
It gives you a chance to learn all of the lessons that the code has to teach you

---
Code without a test? Can you do that?

---
Imposter

---
Realistic Data is useful when:

        
          
            You are testing real-time systems using traces of external events gathered from the actual execution
          

          
            You are matching the output of the current system with the output of a previous system (parallel testing)
          

          
            You are refactoring a simulation and expect precisely the same answers when you are finished, particularly if floating point accuracy may be a problem

---
Learning Test

---
How do you create common objects needed by several tests? Convert the local variables in the tests into instance variables. Override setUp() and initialize those variables.

---
You need to start from a place of confidence and certainty. Therefore, always make sure that all of the tests are running before you check in your code.

---
When I write a test that is too big, I first try to learn the lesson. Why was it too big? What could I have done differently that would have made it smaller? How am I feeling right now?

---
When should you write the asserts? Try writing them first.

---
Don't expect them to replace the other types of testing:

        
          
            Performance
          

          
            Stress
          

          
            Usability

---
Fear makes you tentative

---
Command— Represent the invocation of a computation as an object, not just as a message.
          

          
            Value Object— Avoid aliasing problems by making objects whose values never change once created.
          

          
            Null Object— Represent the base case of a computation by an object.
          

          
            Template Method— Represent invariant sequences of computation with an abstract method intended to be specialized through inheritance.
          

          
            Pluggable Object— Represent variation by invoking another object with two or more implementations.
          

          
            Pluggable Selector— Avoid gratuitous subclasses by dynamically invoking different methods for different instances.
          

          
            Factory Method— Create an object by calling a method instead of a constructor.
          

          
            Imposter— Introduce variation by introducing a new implementation of existing protocol.
          

          
            Composite— Represent the composition of the behavior of a list of objects with an object.
          

          
            Collecting Parameter— Pass around a parameter to be used to aggregate the results of computation in many different objects.

---
an automated test.

        

---
Do Over

---
If our knowledge of the implementation gives us confidence even without a test, then we will not write that test

---
the tougher the programming problem, the less ground that each test should cover

---
Are the teeny-tiny steps feeling restrictive? Take bigger steps. Are you feeling a little unsure? Take smaller steps. TDD is a steering process—a little this way, a little that way. There is no right step size, now and forever

---
I think about Mean Time Between Failures (MTBF) when I think about how many tests to write

---
Method Object.

---
If you expected certain notifications but you didn't care about the order, then you could keep a set of strings and use set comparison in the assertion.

---
If there isn't a conceptual difference between 1 and 2, use 1.

        

---
Regression Test

---
a trickier example of TDD—three for the price of one.

---
Make it run, make it right.

---
Triangulation

---
Use patterns to decide what tests to write

---
Instead of avoiding feedback, search out helpful, concrete feedback

---
Part of the effect certainly comes from reducing defects

---
However, by using only Obvious Implementation, you are demanding perfection of yourself.[2] Psychologically, this can be a devastating move.

---
Extract Method (the most common)

---
How do you represent the intent of the data?

---
We have a Template Method, which we expect to call setUp(), a testing method, and tearDown(), in that order

---
"I'll ruin my health, alienate my family, and kill myself if necessary"—that I don't feel compelled to give any advice along these lines. If you find yourself caffeine-addicted and making no progress whatsoever, then perhaps you shouldn't take quite so many breaks. In the meantime, take a walk.

---
TDD's view of testing is pragmatic. In TDD, the tests are a means to an end—the end being code in which we have great confidence

---
By eliminating duplication before we go on to the next test, we maximize our chance of being able to get the next test running with one and only one change

---
Null Object

---
There certainly are programming tasks that can't be driven solely by tests

---
Finding Imposters during refactoring is driven by eliminating duplication, just as all refactoring is driven by eliminating duplication

---
What's the first thing you do when a defect is reported? Write the smallest possible test that fails and that, once run, will be repaired.

        

---
Pluggable Object

---
what's my motivation

---
Didn't refactor immediately, but instead tested further

---
Child Test

---
Pick a test that will teach you something and that you are confident you can implement.

---
How do you leave a programming session when you're programming alone? Leave the last test broken.

---
Starter Test

---
Whether a test makes sense to write depends on how carefully you measure MTBF

---
 Get cheap/slow/old machines for individual e-mail and surfing, and the hottest possible machines for shared development.

---
If you know what to type, type the Obvious Implementation. If you don't know what to type, then Fake It. If the right design still isn't clear, then Triangulate. If you still don't know what to type, then you can take that shower.

        

---
our cycle has different phases

---
Mock Object

---
How do you check that tests worked correctly? Write boolean expressions that automate your judgment about whether the code worked.

---
Objects are excellent for abstracting away the duplication of logic

---
I use Extract Method when I'm trying to understand complicated code.

---
Refactor to add design decisions one at a time

---
What test do we need first

---
The first four steps of the cycle won't work without the fifth

---
The first three phases need to go by quickly, so we get to a known state with the new functionality. We can commit any number of sins to get there, because speed trumps design, just for that brief moment

---
First we'll solve the "that works" part of the problem. Then we'll solve the "clean code" part

---
The smell of Composite is illustrated by the above. Transactions don't have balances, not in the real world. Applying Composite is a programmer's trick, not generally appreciated by the rest of the world. However, the benefits to program design are enormous, so the conceptual disconnect is often worth it

---
Where does the operation belong?
          

          
            What are the correct inputs?
          

          
            What is the correct output given those inputs?

---
one huge advantage

---
Write automated tests before coding

---
Metaphor

---
cross it off

---
You can refactor from there with confidence

---
also appear to be written bottom-up

---
We don't start with objects, we start with tests

---
How do you test error code that is unlikely to be invoked? Invoke it anyway with a special object that throws an exception instead of doing real work.

---
a to-do list to remind us what we need to do, to keep us focused, and to tell us when we are finished

---
Obvious Implementation

        

---
Then comes the interesting part. A customer has a bunch of accounts and would like to see an overall balance.

---
Method Object

        How do you represent a complicated method that requires several parameters and local variables? Make an object out of the method.

---
You should test:

        
          
            Conditionals
          

          
            Loops
          

          
            Operations
          

          
            Polymorphism
          
        

        But only those that you write

---
Which test should you pick next from the list?

---
Suggested an experiment comparing TDD with your current programming style

---
list all of the refactorings that you think you will have to do in order to have clean code at the end of this session

---
How do you leave a programming session when you're programming in a team? Leave all of the tests running.

        
          

---
Be specific. If the area should be 50, then say that it should be 50: assertTrue(rectangle.area() == 50)

---
When my confidence returns, I go back to Obvious Implementations

---
Psychological

---
Courage

---
Test is a verb meaning "to evaluate."

---
What do you do when you need the invocation of a computation to be more complicated than a simple method call? Make an object for the computation and invoke it.

---
As Bill Wake says, "An n2 problem is not a problem if n is always 1."

---
Why does test the noun, a procedure that runs automatically, feel different from test the verb, such as poking a few buttons and looking at answers on the screen?

---
Were a little stuck on big design ideas, so we worked on something small we noticed earlier
          

          
            

---
for those operations that don't already exist, put the null version of that operation on the list

---
automated tests

---
the immediate payoff for testing—a design and scope control tool—suggests that we will be able to start doing it, and keep doing it even under moderate stress.

---
When should you write your tests? Before you write the code that is to be tested.

---
Noticed that our design pattern (Value Object) implied an operation

---
put on the list examples of every operation that you know you need to implement

---
the tests are order independent

---
How do you test that one object communicates correctly with another? Have the object under test communicate with the test case instead of with the object it expects.

---
The three approaches to making a test work cleanly—fake it, triangulation, and obvious implementation

---
One beneficial side effect of Evident Data is that it makes programming easier

---
writing only that code which is demanded by failing tests also has social implications

---
Conservative mountain climbers have a rule that of your four hands and feet, three of them must be attached at any one time. Dynamic moves where you let go of two at once are much more dangerous. The pure form of TDD, wherein you are never more than one change away from a green bar, is like that three-out-of-four rule.

---
Evident Data seems to be an exception to the rule that you don't want magic numbers in your code

---
When we test first, we reduce the stress, which makes us more likely to test

---
TDD is not about taking teeny-tiny steps, it's about being able to take teeny-tiny steps

---
I only use Triangulation when I'm really, really unsure about the correct abstraction for the calculation. Otherwise I rely on either Obvious Implementation or Fake It.

---
programming culture is so infected with macho spirit

---
Create tests for more complicated logic, including reflection and exceptions

---
I use Extract Method to eliminate duplication when I see that two methods have some parts the same and some parts different.

---
How do you keep a technical discussion from straying off topic? When a tangential idea arises, add a test to the list and go back to the topic.

        

---
more-detailed techniques for writing tests.

---
Cheap Desk, Nice Chair

        

---
How much feedback do you need?

---
The good news is, since you're getting good at refactoring, the moment the duplication appears, you can introduce Composite and watch program complexity disappear.

---
habit of writing down everything I wanted to accomplish over the next few hours on a slip of paper next to my computer.

---
Wrote the test by shamelessly duplicating and editing
          

          
            

---
Write a test

---
How do you design objects that will be widely shared, but for whom identity is unimportant? Set their state when they are created and never change it. Operations on the object always return a new object.

---
Refactored to capture the two cases at once

---
Make it run

---
Test (noun)

        

---
If you can make steps too small, you can certainly make steps the right size

---
Mock Objects encourage you down the path of carefully considering the visibility of every object, reducing the coupling in your designs

---
This test speaks to us more clearly, as if it were an assertion of truth, not a sequence of operations

---
If two receiving stations at a known distance from each other can both measure the direction of a radio signal, then there is enough information to calculate the range and bearing of the signal

---
Some of the nastiest bugs in my career have come when changing the first check's value inadvertently changed the second check's value. This is aliasing

---
There are a couple of effects that make Fake It powerful.

        
          
            

---
Fear makes you grumpy

---
Stepwise moved common code from one class (Dollar) to a superclass (Money)
          

          
            Made a second class (Franc) a subclass also
          

          
            Reconciled two implementations—equals()—before eliminating the redundant one

---
Each test should represent one step toward your overall goal

---
How do you invoke different behavior for different instances? Store the name of a method, and dynamically invoke the method.

---
If the topics of technical conversations can be made clear enough, then software engineers can work in minute-by-minute collaboration instead of daily or weekly collaboration

---
Red/green/refactor—the TDD mantra

---
If you have discovered larger refactorings that are out of scope for the moment, then move them to the "later" list

---
One implication of Value Objects is that all operations must return a new object

---
Applying objects to organizing computation is one of the best examples of common internally generated subproblems being solved in common, predictable ways. The enormous success of design patterns is a testimonial to the commonality seen by object programmers.[2] The success of the book Design Patterns, however, has stifled any diversity in expressing these patterns. The book seems to have a subtle bias toward design as a phase. It certainly makes no nod toward refactoring as a design activity. Design in TDD requires a slightly different look at design patterns.

---
How do you implement an operation that works with collections of objects? Implement it without the collections first, then make it work with collections

---
The dogmatic answer is that we'll wait, not interrupting what we're doing.

---
Another solution is Observer,

---
appear to be written top-down

---
Composite

        How do you implement an object whose behavior is the composition of the behavior of a list of other objects? Make it an Imposter for the component objects.

---
Value Object

---
Instead of clamming up, communicate more clearly

---
Extract Method

        How do you make a long, complicated method easier to read? Turn a small part of it into a separate method and call the new method.

---
Security software and concurrency

---
Which test should you start with? Start by testing a variant of an operation that doesn't do anything.

---
The more stress you feel, the less likely you are to test enough.

---
At the scale of hours, keep a water bottle by your keyboard so that biology provides the motivation for regular breaks.
          

          
            At the scale of a day, commitments after regular work hours can help you to stop when you need sleep before progress.
          

          
            At the scale of a week, weekend commitments help get your conscious, energy-sucking thoughts off work. (My wife swears I get my best ideas on Friday evening.)

---
I use it only when I am completely unsure of how to refactor

---
two simple rules, but they generate complex individual and group behavior with technical implications

---
Broken Test

---
At the scale of a year, mandatory vacation policies help you refresh yourself completely. The French do this right—two contiguous weeks of vacation aren't enough. You spend the first week decompressing, and the second week getting ready to go back to work. Therefore, three weeks, or better four, are necessary for you to be your most effective the rest of the year.

---
A Crash Test Dummy is like a Mock Object, except you don't need to mock up the whole object

---
 TDD can't guarantee that we will have flashes of insight at the right moment.

---
We could have used Triangulation to drive the generalization of times() also. If we had $5 x 2 = $10 and $5 x 3 = $15, then we would no longer have been able to return a constant

---
What axes of variability are you trying to support in your design? Make some of them vary, and the answer may become clearer

---
Wrote a test with future readers in mind

---
The downside of using Factory Method is precisely its indirection. You have to remember that the method is really creating an object, even though it doesn't look like a constructor. Use Factory Method only when you need the flexibility it creates. Otherwise, constructors work just fine for creating objects.

---
Following are two examples of Imposters that come up during refactoring:

        
          
            Null Object— You can treat the absence of data the same as the presence of data.
          

          
            Composite— You can treat a collection of objects the same as a single object.

---
What do you do when you feel tired or stuck? Take a break.

---
We'd prefer not to write a test when we have a red bar

---
Pick a Starter Test that will teach you something but that you are certain you can quickly get to work.

---
That will let us make "amount" private, as all good instance variables should be

---
Solve complicated tasks, beginning with the simple and proceeding to the more complex

---
Another advantage of TDD that may explain its effect is the way it shortens the feedback loop on design decisions

---
Test methods should be easy to read, pretty much straightline code

---
When everything is going smoothly and I know what to type, I put in Obvious Implementation after Obvious Implementation

---
When you are writing a test, you are solving several problems at once, even if you no longer have to think about the implementation.

        
          
            

---
How many tests should you write?

---
The ability to control the gap between tests to increase traction when the road gets slippery and cruise faster when conditions are clear

---
TDD isn't an absolute the way that XP is

---
Use data that makes the tests easy to read and follow.

---
Copy-and-paste reuse? The death of abstraction? The killer of clean design?

---
two of the three strategies I know for quickly getting to green

---
As a result of using Self Shunt, you will see tests in Java that implement all sorts of bizarre interfaces

---
Assert First

---
One of the constraints on Value Objects is that the values of the instance variables of the object never change once they have been set in the constructor

---
TDD rests on a charmingly naïve geekoid assumption that if you write better code, you'll be more successful

---
eliminating duplication

---
Wishing for white box testing is not a testing problem, it is a design problem. Anytime I want to use a variable as a way of checking to see whether code ran correctly or not, I have an opportunity to improve the design. If I give in to my fear and just check the variable, then I lose that opportunity. That said, if the design idea doesn't come, it doesn't come.