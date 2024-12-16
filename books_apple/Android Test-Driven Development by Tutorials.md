## Metadata
- Author: By Victoria Gonda
- [Apple Books Link](ibooks://assetid/FF9FA924C3AE19C2227DB303D5E1AF05)

## Highlights
Why should you test?

---
Teardown

---
Interact with device sensors

---
Exposes streams of data ready to be displayed, but it doesn’t know and doesn’t care about who is subscribed to the streams

---
assertEquals

---
With JUnit you can do state verification, also called black-box testing.

---
The intent of the Composite design pattern is to construct complex objects composed of individual parts, and to treat the individual parts and the composition uniformly

---
A class that has lots of responsibilities is sometimes called a god class and should be avoided

---
@Test

---
Code spikes

---
Testing the Network Layer

---
those decisions may be difficult to modify once they’re implemented

---
high cohesion

---
Testing ViewModel and LiveData



---
Learn the characteristics of a testable architecture

---
One of the reasons why MVVM, MVP and MVI are popular is because they tend to drive a structure that is easier to test

---
you want to test that your logic, your queries, and the code that depends on them are working correctly.

---
an app that uses an object of a base class should be able to use objects of derived classes without knowing about that and continue working. Therefore, your code should not be checking the subtype

---
you shouldn't test functionality of external libraries because the goal is to test things that you control, not a third party tool created by someone else.




---
The doAnswer closure returns an InvocationOnMock type, with which you can spy on its arguments

---
UI Tests: 10%



Integration Tests: 20%



Unit Tests: 70%

---
it’s not only testing that matters

---
UI testing generally verifies two things:



That the user sees what you expect them to see.



That the correct events happen when the user interacts with the screen.

---
when running your automated tests, you don't actually want to make a network call.

---
Testing the Persistence Layer



---
Check the following references to know more about the topic:



Test Double Patterns by Gerard Meszaros: http://xunitpatterns.com/Test%20Double%20Patterns.html



Mocks Aren't Stubs by Martin Fowlder: https://martinfowler.com/articles/mocksArentStubs.html

---
Dagger2 and Koin

---
Adapter (or Wrapper)

---
Reusable abstraction

---
Persist data

---
When using TDD, you’ll write a new test to check the new feature or change an existing test to verify some behavior that now has to deal with more use cases. While writing the test you may notice that it starts to become too complex. That may be a sign you need to introduce a new class that inherits from the old one or use composition to handle each use case

---
large tests.



---
Function/method coverage

---
the Presenter could grow a lot, converting it into another anti-pattern called God-class

---
Facade design pattern defines a high-level interface object which hides the complexity of underlying objects

---
 Using TDD will also make you think on how the classes will collaborate

---
Dependency Injection

---
External dependencies

---
 Observer design pattern gives you a way to communicate between objects where one object informs others about changes or actions

---
UI tests

---
a concrete class A should not depend on a concrete class B, but an abstraction of B instead

---
Code you don't have time to test

---
Change/refactor confidence

---
When you have a class A that depends on a class B, and the tests of A start to require you to stub many methods of B, B is turning into a god class

---
If instead, for example, an implementation removes a contact and then returns it, it would be violating the principle because you wouldn’t be maintaining the expected behavior

---
you should perform your tests with unit and integration tests as much as you can

---
The System Under Test (SUT) is one class and you focus only on it

---
What should you test?

---
Espresso

---
dependency injection

---
Bear in mind that not following the correct pyramid shape could affect productivity

---
Early design decisions

---
No matter which way you're saving it, you need to be confident it is always working. If a user takes the time to put together content and then loses it because your persistence code broke, both you and your user will have a sad day.

---
Using a spy is similar to using a mock, but on real instances

---
Builder design pattern abstracts the construction of a complex object, joining several parts

---
Spying

---
Set Up

---
To write a test, you need to understand the feature, specification or requirement of the component you are implementing

---
A test is a manual or automatic procedure used to evaluate if the System Under Test (SUT) behaves correctly

---
 observer

---
you avoid searching for solutions that other developers have already solved

---
 design patterns and the SOLID principles

---
Interface segregation

This principle encourages you to create fine grained interfaces that are client specific

---
software elements and their relations

---
you should avoid the following anti-patterns

---
Creational

---
One of the challenges that make writing persistence tests difficult is managing the state before and after the tests run

---
can help speed up your development process

---
A Telescoping Constructor consists of a constructor with many parameters where some of them are optional

---
 at some point someone or something needs to instantiate the class. Usually, it's the entity that creates objects and provides their dependencies. This entity is known as the injector, assembler, provider, container or factory

---
make sure you test the most common scenarios and use this metric to find untested code that should be tested.

---
you should at least write those that cover the most common scenarios.

---
 the encapsulation of an operation without knowing the real content of the operation or the receiver

---
This is sometimes called a Service Locator because you ask a locator object

---
Composite

---
write an additional test similar to the one you've just previously run, but change the check

---
single purpose.

---
Check one single thing

---
Stubbing callbacks

---
 crucial to having a testable architecture

---
Remember the TDD procedure: write a test, see it fail, write the minimum amount of code to make it pass and refactor if needed.



---
in-memory database

---
Communication

---
medium tests

---
Statement coverage

---
It just exposes streams of data (Observables), it could be the Model or a transformed-displayable Model

---
Automatically document

---
Documentation

---
focusing on one section of the app and working through the others over time.

---
How can you save data while your tests are running, but ensure that test data is gone when the tests finish? 

---
Branch coverage

---
Unit tests

---
When to use integration tests



---
What should you not test?

---
naming of each variable or method used

---
Throwaway/prototype code

---
These may come in different forms, such as user stories, use cases or some other kind of documentation

---
With Mockito you can perform behavior verification or white-box testing

---
Robolectric

---
it will be easy to change it to a SharedPreferencesDataFetcher or a RoomDataFetcher class as long as those classes implement the DataFetcher interface

---
meaningful name

---
what is the purpose of the test

---
 lots of small unit tests, some integration and fewer UI tests

---
Single responsibility (SRP)

---
verify the behavior of how classes work together within your app, with the Android framework, and with external libraries

---
Autogenerated code

---
"Should you be testing this?" The answer to this question is important.

---
Using white-box testing allows you to be more precise in your tests, but often results in having make more changes to your tests when you change your production code

---
Liskov substitution

---
the quickest, easiest to write and cheapest to run

---
Readable

---
The Activities have to start observing (subscribe) these LiveData objects in the onCreate() method and doesn’t need to stop observing (unsubscribe) because the base LiveData class from Android Architecture Components is aware of the Activity lifecycle

---
Keep maintainable code

---
UI and navigate

---
RxKotlin/Android libraries

---
 ease the design to establish relationships between objects

---
 ViewModel doesn’t have a reference to the View, not even an interface

---
Apps that are architected for testing separate their code into groups of logic using multiple methods and classes to collaborate

---
one large class with too many responsibilities

---
network requests to an API

---
If you combine the Builder design pattern with the dependency injection design pattern, you end up with something like this:

---
You write these type of tests when you need to check how your code interacts with other parts of the Android framework or external libraries

---
Observer

---
View: Notifies the ViewModel about user actions. Subscribes to streams of data exposed by the ViewModel

---
JUnit

---
Rewriting a legacy application should generally be considered as a last resort option.

---
How would you like to learn another way to generate test data?

---
When to use unit tests

---
Espresso

---
a template or blueprint that you can use when building new apps

---
you'll need to integrate with a database, filesystem, network calls, device sensors, etc.

---
In the context of TDD, you should first create this test, and afterward, the corresponding implementation.

---
Facade

---
Behavioral

---
Open-closed

---
LiveData+ViewModel from Android Architecture Components

---
Short and simple

---
If your ViewModel classes extend a ViewModel class from the Android framework, bear in mind that this class has nothing to do with UI, so it’s still unit testable

---
 Mockito

---
logic sequence of the test

---
Software architecture

---
A code spike is a throwaway piece of untested code that explores possible solutions to a problem

---
It often doesn't add value to test all methods, of all the classes, all of the time.

---
how objects interact and how a task can be divided into sub-tasks among different objects

---
Higher test coverage

---
When setting up spies, you need to use doReturn/whenever/method to stub a method

---
 be mindful of how expensive the test is to perform

---
When should you not test?

---
everything that you verified for your base class should also be verified for your new child class

---
Integration

---
Integration tests

---
Discover good practices to create a testable architecture

---
how do you handle it when you're using something other than Room for your persistence?

Unfortunately, many libraries don't have these convenient, built-in testing helpers

---
The Builder design pattern is useful to avoid an anti-pattern known as a Telescoping Constructor

---
Dependency inversion

---
Thanks to TDD, you may realize a class is becoming a god class when you spot some of the following signs

---
this is an event based approach, where the ViewModel produces data and the View consumes it

---
When to use integration tests

---
behavior verification or white-box testing

---
solutions related to object creation

---
Develop faster

---
Assertion

---
Faker

---
design by contract

---
Model your domain

---
Each class should have a unique objective or should be useful for a specific case

---
Adapter (or Wrapper) design pattern describes how to let two incompatible classes work together

---
Structural

---
observable

---
How to write a test

---
A poorly architected app

---
 They usually test if the data is shown correctly to the user, if the UI reacts correctly when the user inputs something, etc.

---
While creational patterns explain a specific moment of time (the creation of an instance), and structural patterns describe a static structure, behavioral patterns describe a dynamic flow

---
The software entities of your app: classes, methods, etc. should be open for extension but closed for modification

---
Have confidence in your code

---
Ice cream cone or Inverted pyramid

---
Command

---
Working Effectively With Legacy Code by Michael Feathers

---
state verification or black-box testing

---
Builder

---
Condition coverage

---
Before adding new functionality for an existing class, you need to add new tests to an existing test suite. If the new tests are not related or don’t follow the essence of the existing ones, the functionality violates SRP

---
This is one of the difficulties of network tests: How do you make your tests reliable and maintainable? Do you keep a file of your responses and swap it whenever there's a change? Do you dynamically create your responses? This will differ depending on your needs and may change as you figure out what's right for your app.

---
Write intentionally

---
It's a balance to test that your interactions with the framework or library are correct without testing the library itself.

---
To complement TDD, the S.O.L.I.D principles are a list of principles to build software following good practices

---
Naming

---
Better testing

---
all of its logic contained within a single method

---
This can be accomplished by:



Using class inheritance or interfaces and overriding methods.



Delegating to other classes (dependencies) by using composition and allowing to easily exchange those classes.

---
Lean/XP

---
 Architectural design patterns, or UI Architecture design patterns.

---
ViewModel: Retrieves data from the Model and updates it accordingly

---
Why is TDD important?

---
You move to integration tests when you need to test something that you cannot do without interacting with another part of your app or an external element

---
the endpoint is correct

---
Design patterns

---
Robolectric

---
 Using a spy will let you call the methods of a real object, while also tracking every interaction, just as you would do with a mock

---
Activity objects know about the Application object, so another way to inject dependencies is to ask them from the Application objec