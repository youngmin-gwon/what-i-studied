## Metadata
- Author: Alexander Tarlinder
- [Apple Books Link](ibooks://assetid/046F6C62A6AFA592543C930058488FAC)

## Highlights
It’s a test case that attempts to do something unusual and unexpected, especially from a developer’s point of view

---
Preconditions are short lived.

---
Level of Abstraction

---
Formal Methods

---
preconditions

---
if your code will be tested by someone else, do you want that person to find obvious and plainly stupid bugs in it? Do you want to waste that person’s time and your employer’s money by turning trivial checks that are easily automated into manual test cases or subjects of an exploratory testing session? Probably not

---
When computing a checksum for a given input, is the input’s format correct?

---
System testing is the activity of verifying that the entire system works

---
 If your program contains a fixed-size buffer for user input and that input isn’t truncated

---
ubiquitous language

---
Planning testing early and collaboratively within the team will help prevent this from happening, or at least reduce the likelihood.

---
Developers will most often encounter functional tests at the unit test level, simply because they create many more of such tests in comparison to other types of tests. However, functional testing applies to all test levels: unit, integration, system, and acceptance.

---
system’s responsiveness, throughput, and reliability given different loads

---
 a black box approach imposes an emotional distance from the target of the test

---
Based on the preceding logic, a test that opens a file to write “Hello world” to it or just outputs the same string on the screen isn’t a unit test. Because it’s definitively not a system test, it must be an integration test by analogy.

---
Small, Medium, and Large Tests

---
Developer Testing


---
it can have its advantages

---
When adding an element to a linked list, the new element becomes the list’s head and it points to the previous head of the list.

---
Little or no mind-numbing work

---
Black Box Development

---
Characterization testing is the kind of testing you’re forced to engage in when changing old code that supposedly works but it’s unclear what requirements it’s based on, and there are no tests around to explain what it’s supposed to be doing

---
ask the same questions

---
Test Levels

---
Nasty Test Cases

---
Preconditions are constraints that need to be met when calling the supplier

---
cross-site scripting (XSS)

---
No testing crunch

---
Observability

---
fast, low-level tests that target a small part of the system

---
Controllability

---
It Can Be Changed


---
White Box and Black Box Testing

---
Domain-Specific Languages


---
After all, running the main method of a program or poking around in the user interface after making some changes is nothing but ad hoc testing.

---
White box testing refers to testing where we do have access to the source code and are able to inspect it, either for verification or inspiration for new tests

---
to support

---
Black box testing is the opposite. We only have access to the tested artifact’s external interface, whatever that might be.

---
Ultimately, testable software is about money and happiness.

---
we can safely assume that too much state turns reproducibility, and hence controllability, into a real pain.

---
this model emphasizes the difference between business-facing and technology-facing tests

---
they have to write their code in a way that makes verification possible.

---
Its Functionality Can Be Verified

---
in larger projects where several teams are involved, being explicit about testing and quality assurance may help to avoid misunderstandings, omissions, blame, and potential conflicts

---
 How much, if any, testing should developers do?
 What kind of testing will give the best return on investment for this particular system?
 Why is testability important, and how can it be achieved?
 Why does a method/class/component seem untestable, and how can it be made testable?
 What’s “testable” code anyway?
 How “good” should test code be?
 When is a method/class/component sufficiently covered by tests?
 How should tests be named?
 When should a certain kind of test-double be used?
 What’s the best way to break this particular kind of dependency?
 Who checks the arguments to a method? The caller or the callee?
 How should test code be structured to avoid duplication, and is all duplication bad?
 In test-driven development, what’s the next test to write?
 How does one test-drive an enterprise system with many delegating layers?
 How does one avoid combinatorial explosions in test code and still feel confident?
 What factors determine the number of assertions in a test?
 Should tests target state or behavior?

---
Unit Test

---
Isolability, modularity, low coupling

---
From the perspective of testing and checking, developer testing is largely about making developers write code with automated checks constantly in mind, so that testing time needn’t be wasted on checking

---
Developers perform activities related to verification and quality assurance more often than they may realize

---
two cornerstones of testability

---
It Comes with Fewer Surprises

---
or sometimes all of these things

---
modeling the software as transactions between a client and supplier, who agree on a contract that forces them to uphold certain obligations to each other

---
they should keep the black box approach in mind

---
This is, by the way, the opposite of building quality in

---
Confidentiality

---
Testing to support is about safety, sustainable pace, and the team’s ability to work fast and without fear of introducing defects during development

---
Traditional Testing

---
sometimes a class

---
Patching and bug fixing

---
Too many observation points and working too far from production code may result in the appearance of Heisenbugs

---
we’ll take a quick look at what testing and quality assurance may look like in different settings and see how developer testing fits into the picture.

---
The mere presence of a tester tends to result in the team asking: “How do we test this?,” which in turn leads to testable software

---
Singularity

---
All three practices incorporate the following elements to a lesser or greater extent: Before starting to implement a story, the team makes sure that everybody is on the same page

---
Performance Testing

---
spike testing

---
 if the individual systems or components have been tested in isolation and have gone through integration testing, system testing will actually target the overall functionality of the system

---
to establish whether changes to the system have broken existing functionality or caused old defects to resurface

---
Testing to Critique

---
Isolability is a desirable property from both a developer’s and a tester’s point of view

---
Observability

---
Contracts Formalize Constraints

---
file system traversal vulnerabilitie

---
the major shift when employing them comes from having to think about the produced code in terms of clients and suppliers and the consequences of formalizing responsibilities

---
Testing Objectives, Styles, and Roles

---
The smaller the software, the better the testability, because there’s less to test.

---
Common phrases like “nobody would ever do that,” “works on my machine,” and “I didn’t even touch that bit of code” illustrate this quite well. This is why independent testing is in the critiquing testing vocabulary.

---
Local testing expertise

---
Programming by Contract

---
A safe way of working with legacy code is adding tests to it retroactively to pin down its behavior before making any changes. Such tests are called characterization tests

---
A unit test may exercise a function or method, a class, or even a cluster of collaborating classes that provide some specific functionality.

---
SQL injections

---
Putting Test Levels and Types to Work

---
supplier

---
Security Testing


---
Testing to critique means to test something that’s finished and needs evaluating

---
They apply only when returning to the calling client.

---
Class invariants are constraints that are always upheld for a class’s internal state.

---
Positive and Negative Testing

---
Reuse

---
sending sensitive data over the network is usually a bad idea

---
Efficiency

---
knowing at least the basics of how to make an application resilient to the most common attacks is something that a developer should know by profession.

---
 testers tend to work from the black box angle, which means that they have to resort to techniques

---
Testing

---
regardless of how the software is being developed, applying developer testing practices will result in better software

---
Functional Testing

---
DRY principle: Don’t Repeat Yourself

---
No handovers

---
Automating some repetitive tasks or tedious tests that have to be run over and over frees up testers to engage in more valuable and interesting work, like exploratory testing

---
Smoke tests are perfect candidates for automation and should be part of an automated build/deploy cycle

---
Nowadays the aforementioned activity is called user acceptance testing

---
One way of classifying them is in order of increasing intrusiveness.

---
The purpose of negative testing is to verify that the system behaves correctly if supplied with invalid values and that it doesn’t generate any unexpected results

---
Unit Testing

---
Integrity

---
Characterization Testing

---
Why Care about Testability

---
System Test

---
Smallness

---
Not only does it reduce coupling between test and production code, viewing the component or system as a black box helps when defining its contract and behavior

---
In this context, state simply refers to whatever data we need to provide in order to set the system up for testing

---
 accounts with easily guessed credentials, is a common practice among digital villain

---
These practices go by different names, and historically there are some minor differences between them. Behavior-driven development (BDD, North 2006), acceptance test-driven development (ATDD, Pugh 2011), and specification by example (Adzic 2011) all address the problem of different stakeholders using different vocabularies, which in turn results in incorrect interpretation of requirements and discrepancies between code, tests, and customer expectations

---
 functional security testing

---
class invariants

---
Sometimes it’s a function

---
Errors, Defects, Failures

---
testability

---
Developer testing is an umbrella term for all test-related activities a developer engages in

---
It refers to testing security as performed by a “regular” tester.

---
End-to-End Testing


---
load testing

---
Isolability

---
Its purpose is to provide feedback and help the team achieve immediate and constant confidence in the software it produces

---
The Agile Testing Quadrants

---
gray areas: size and scope of a unit of work, collaborator isolation, and execution speed

---
sometimes a component

---
In this section, we’ll explore what to take away from contract programming and how.

---
an activity performed by the end users to validate that the software they received conforms to the specifications and their expectations and is ready for use

---
targets a solution’s quality attributes such as usability, reliability, performance, maintainability, and portability

---
I

---
The previous alternatives clearly show that tests are better than the problems they address. That just means they’re the best thing we have, not the best we can do. Ultimately, we care about correctness, not tests.

---
The Testing Vocabulary

---
it can be put in a known state, acted on, and then observed

---
Although all of this is true, the root cause of the problem isn’t really information hiding or encapsulation, but poor design and implementation, which, in turn, forces us to ask the question of the decade: Should I test private methods?

---
Contract Building Blocks

---
Once a piece of software has been rolled out into production, it goes into maintenance, which falls into either of two categories:

---
Deployability

---
What’s important is that the developer has anticipated the scenario

---
 making the black box of testing

---
happy path tests

---
we shouldn’t neglect the usefulness of having a crystal-clear picture of what not to do

---
Having testing experts on the development team provides several immediate advantages:

---
How much work has been done? How much remains?

---
efficiency equals the ability to express intent in the programming language in an idiomatic way and making use of that language’s functionality to keep the code expressive and concise.

---
When

---
Generally, as the level of abstraction is raised, fewer tests that cover fundamental building blocks, or the “plumbing,” are needed, because such things are handled by the language or framework.

---
 Defects/bugs may lead to software failures.

---
Security for Developers 101

---
Smallness

---
Agile testing is testing that enables agile development. In essence, it’s about empowering the tester and increasing collaboration within the team and with external stakeholders

---
In addition to running their code to check that it seems to behave correctly, they

 Write unit tests
 Write integration tests
 Perform maintenance
 Implement continuous integration
 Provide the infrastructure for test automation

---
feeding it different inputs and comparing the results with the specification,3 and exploring it beyond the explicit specification to see if it violates any implicit expectations

---
Errors lead to defects in the software. A more frequently used term for defect is bug

---
 Tests are traditionally classified along two dimensions: test level and test type

---
Regression Testing

---
controllability

---
Types

---
Logging, by the way, is a double-edged sword. Although it’s certainly the easiest way to increase observability, it may also destroy readability.

---
 If there was a crack, the smoke would seep out through it

---
it’s easy to confirm that it supports a certain feature, behaves correctly given a certain input, adheres to a specific contract, or fulfills some nonfunctional constraint

---
Controllability

---
Benefits of Testability

---
Behavior

---
I strongly suggest that the following questions be raised for each method, class, component, or other artifact:
 What is its interface to the outside world?
 What inputs does it take? (Have all allowed values been specified?)
 How does it communicate success or failure?
 How does it react to bad input? (Does it recover or crash?)
 Does it surprise by doing something unexpected or unusual?

---
Establishing preconditions, postconditions, and maybe even invariants for the program elements that we create slows us down—but in a good way.

---
A critical element of such conversations is that the language of the customer be retained and used, and that it be done all the time and by everybody

---
Observability and information hiding are often at odds with each other.

---
we need to be able to observe it

---
why achieving it for software is an end in itself

---
Testability

---
Given

---
client

---
Agile Testing Quadrants, developer tests cover the whole of the lower left quadrant, large parts of the upper left quadrant, and a fair share of the lower right quadrant

---
Testability

---
 expressing the proximity to the source code and the footprint of the test

---
Classifying Tests

---
Maintenance

---
In short, white box testing is driven by the size of the codebase.

---
Testing Styles

---
Others

---
Their function is to provide a receipt of the new functionality being implemented, and they’re written ahead of the production code.

---
Agile testing—Proactive, integrated, collaborative

---
it’s about being able to isolate the program element under test—be it a function, class, web service, or an entire system.

---
Observability

---
Collaborator isolation, along with speed of execution, is subject to more intense debate.

---
Testing Objectives

---
sometimes a method

---
But what exactly about the software should be “small”? From a testability perspective, two properties matter the most: the number of features and the size of the codebase.

---
Postconditions are constraints on the supplier’s internal state and often the return value

---
postconditions

---
Thinking in terms of contracts and behavior is both a fundamental and very usable design technique, and it leads to software that can readily be tested

---
functional and nonfunctional testing

---
Testing to Support

---
By now it should be obvious that developer testing, as described in this book, is testing meant to support.

---
the team gets to talk about its combined skill set, as the various kinds of tests require different levels of effort, time, resources, training, and experience

---
Test Types

---
Program Elements

---
Postconditions are also short lived.

---
paramount importance to any kind of testing because it leads to reproducibility

---
Two common types of invariants are class invariants and loop invariants.

---
Availability

---
isolability can be described in terms of fan-out, that is, the number of outgoing dependencies on other classes

---
The vocabulary of testing to critique includes the tester mind-set and the developer mind-set, according to which developers want to build and testers want to break

---
Acceptance Test

---
Nonfunctional Testing


---
All developers sometimes make mistakes. These are known as errors

---
The ability to reproduce a given condition in a system, component, or class depends on the ability to isolate it and manipulate its internal state

---
cracking a simple password may take minutes or even seconds

---
it refers to making use of third-party components to avoid reinventing the wheel.

---
smoke testing refers to one or a few simple tests executed immediately after the system has been deployed

---
the outcome produced by its functionality under certain preconditions

---
Testing is the process of evaluating a product by learning about it through exploration and experimentation, which includes to some degree: questioning, study, modeling, observation, inference, etc

---
sometimes a module

---
Smoke Testing

---
stress testing

---
Maintenance of a system under development