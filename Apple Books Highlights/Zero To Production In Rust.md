## Metadata
- Author: Luca Palmieri
- [Apple Books Link](ibooks://assetid/3F4317391D555EA46B33D23846F42C2D)

## Highlights
tarpaulin

---
The key line is this:
actix_web::rt::System::new("main").block_on(async move { ... })

---
toolchain management.

---
We need main to be asynchronous because HttpServer::run is an asynchronous method but main

---
continuous integration

---
It forces you to engage with your teammates earlier than when it feels comfortable, course-correcting if necessary when it is still easy to do so (and nobody is likely to get offended).

---
where all your application logic lives: routing, middlewares, request handlers, etc.

---
handling their requests

---
Embedded test modules

---
clippy

---
as part of your public documentation (doc tests)

---
macros is code generation.

---
black box testing

---
rustup

---
To handle dynamic workloads (e.g. request volumes).

---
Rust gives you three options

---
All futures expose a poll method which has to be called to allow the future to make progress and eventually resolve to its final value

---
expands

---
handles all transport level concerns

---
The main function that gets passed to the Rust compiler after #[actix_web::main] has been expanded is indeed synchronous, which explain why it compiles without any issue.

---
There is no special configuration syntax that tells the Rust compiler that one of your dependencies is an asynchronous runtime (e.g. as we do for allocators) and, to be fair, there is not even a standardised definition of what a runtime is (e.g. an Executor trait).

---
Why is that?

---
You are therefore expected to launch your asynchronous runtime at the top of your main function and then use it to drive your futures to completion.

---
route

---
you are supposed to bring one into your project as a dependency

---
Although it is working, our Cargo.toml file now does not give you at a glance the full picture: you see a library, but you don’t see our binary there

---
you can then leverage embedded test modules to write unit tests for private sub-components to increase your overall confidence in the correctness of the whole project

---
Continuous Integration tightens the feedback loop

---
Rust macros operate at the token level: they take in a stream of symbols

---
pecify conditions that a request must satisfy in order to “match” and be passed over to the handle

---
How Do You Test An Endpoint?

---
They are therefore used mostly for integration testing, i.e. testing your code by calling it in the same exact way a user would.

---
In other words, the job of #[actix_web::main] is to give us the illusion of being able to define an asynchronous main while, under the hood, it just takes our main asynchronous body and writes the necessary boilerplate to make it run on top of actix’s runtime.

---
Continuous Integration

---
more than a Rust installer

---
two parameters

---
Security Vulnerabilities

---
HttpServer

---
Tests

---
This approach is extremely versatile: you are free to implement your own runtime, optimised to cater for the specific requirements of your usecase

---
trunk-based development

---
configuration line in clippy.toml

---
Linting

---
CI pipeline

---
Guard

---
and output a stream of new symbols which then gets passed to the compiler

---
external tests folder and doc tests

---
To allow us to continuously release new versions with zero downtime

---
A toolchain is the combination of a compilation target and a release channel

---
the component whose job is to take an incoming request as input and spit out a response

---
Cloud-native applications

---
actix_web::main is a procedural macro

---
How do we debug or inspect what is happening with a particular macro? You inspect the tokens it outputs!

---
test-driven development

---
To achieve high-availability while running in fault-prone environments

---
App

---
in an embedded test module, e.g.

---
#[actix_web::main]

---
Responder is nothing more than a conversion trait into a HttpResponse

---
Formatting

---
iceberg projects

---
Rust’s standard library, by design, does not include an asynchronous runtime

---
We are starting actix’s async runtime (rt = runtime) and we are using it to drive the future returned by HttpServer::run to completion

---
CI pipeline checks

---
cargo, Rust’s build tool

---
path

---
we verify the behaviour of a system by examining its output given a set of inputs without having access to the details of its internal implementation

---
HTTP mocking

---
web::get() is a short-cut for Route::new().guard(guard::Get())

---
 Rust compiler itself, rustc

---
Code Coverage

---
a pull request review

---
This has often been described as a pull model compared to the push model adopted by other languages

---
route

---
black-box testing for APIs

---
Port 0 is special-cased at the OS level: trying to bind port 0 will trigger an OS scan for an available port which will then be bound to the application

---
Most organizations have more than one line of defence for the main branch

---
Do all our handlers need to have the same function signature of greet?
No!

---
in an external tests folder