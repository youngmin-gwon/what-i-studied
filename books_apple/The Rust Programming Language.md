## Metadata
- Author: Steve Klabnik
- [Apple Books Link](ibooks://assetid/5F1556DE8EAA81852AB6FDC626DFC1AE)

## Highlights
a value can be either something or nothing

---
deref coercions

---
A reference is like a pointer in that it’s an address we can follow to access the data stored at that address

---
the arms’ patterns must cover all possibilities

---
struct AlwaysEqual;

---
enumerating its possible variants

---
match

---
Tuple structs have the added meaning the struct name provides but don’t have names associated with their fields

---
Rust’s .. range syntax

---
when we want a catch-all but don’t want to use the value in the catch-all pattern

---
a race condition and happens when these three behaviors occur:

Two or more pointers access the same data at the same time.
At least one of the pointers is being used to write to the data.
There’s no mechanism being used to synchronize access to the data.

---
Recall that we talked about string literals being stored inside the binary

---
what types implement the Copy trait

---
struct

---
The problem with null values is that if you try to use a null value as a not-null value, you’ll get an error of some kind

---
References must always be valid.



---
The primitive types we’ve seen so far implement Display by default because there’s only one way you’d want to show

---
Option

---
define functions that are associated with your type

---
Rust has a solution to this problem: string slices.

---
The opposite of referencing by using & is dereferencing

---
This was a deliberate design decision for Rust to limit null’s pervasiveness and increase the safety of Rust code.

---
String Slices as Parameters


---
data race

---
Structs are similar to tuples

---
pattern matching

---
{

---
we can put data directly into each enum variant.

---
Putting the specifier :? inside the curly brackets tells println! we want to use an output format called Debug

---
you don’t have to rely on the order of the data to specify or access the values of an instance

---
 useful when you need to implement a trait on some type but don’t have any data that you want to store in the type itself

---
Derived Traits

---
enum

---
Field Init Shorthand

---
&str

---
enums

---
If we tried to use s after the call to takes_ownership, Rust would throw a compile-time error

---
the action of creating a reference borrowing

---
If we put the catch-all arm earlier, the other arms would never run

---
}

---
where we discuss generic types and traits.

---
for testing purposes

---
generic

---
*

---
Associated Functions

---
Rust does include functionality to print out debugging information, but we have to explicitly opt in to make that functionality available for our struct

---
References and Borrowing

---
 This tells Rust we aren’t going to use the value, so Rust won’t warn us about an unused variable

---
Rust knows that we didn’t cover every possible case, and even knows which pattern we forgot

---
 No need for curly brackets or parentheses

---
Users of an immutable reference don’t expect the value to suddenly change out from under them

---
Structs

---
Rust requires us to annotate the overall Option type: the compiler can’t infer the type that the corresponding Some variant will hold by looking only at a None value.

---
 first parameter is always self

---
a special annotation called the Copy trait

---
we cannot borrow s as mutable more than once at a time

---
More Parameters

---
each variant can have different types and amounts of associated data.

---
s: &String

---
we’re able to define methods on structs using impl, we’re also able to define methods on enums

---
Ownership and Functions

---
Self keywords

---
Option Enum

---
_ Placeholder

---
 representing the same concept using just an enum is more concise

---
Mutable References

---
Mutable references have one big restriction: if you have a mutable reference to a value, you can have no other references to that value

---
username,

---
enumerations

---
 the compiler can tell that the reference is no longer being used at a point before the end of the scope

---
Patterns can be made up of literal values, variable names, wildcards, and many other things

---
tuple structs

---
String slice range indices must occur at valid UTF-8 character boundaries

---
Unit-Like Structs Without Any Fields

---
A more experienced Rustacean would write the signature shown in Listing 4-9 instead because it allows us to use the same function on both &String values and &str values.

---
Recall from the borrowing rules that if we have an immutable reference to something, we cannot also take a mutable reference.

---
a struct is like an object’s data attributes

---
you have to convert an Option<T> to a T before you can perform T operations with it. Generally, this helps catch one of the most common issues with null: assuming that something isn’t null when it actually is.

---
Unlike with tuples, in a struct you’ll name each piece of data so it’s clear what the values mean

---
a custom data type that lets you package together and name multiple related values that make up a meaningful group

---
why is having Option<T> any better than having null?

---
Returning values can also transfer ownership

---
impl

---
active: true,

---
&str

---
This catch-all pattern meets the requirement that match must be exhaustive

---
Unlike a pointer, a reference is guaranteed to point to a valid value of a particular type for the life of that reference.

---
both hold multiple related values

---
 But with structs, the way println! should format the output is less clear because there are more display possibilities

---
At any given time, you can have either one mutable reference or any number of immutable references.


---
very common scenario in which a value could be something or it could be nothing

---
#[derive(Debug)]

---
To call this associated function, we use the :: syntax with the struct name

---
Multiple impl Blocks

---
match

---
traits

---
if let

---
A string slice is a reference

---
structs

---
_ => reroll(),

---
enum IpAddr {
    V4(String),
    V6(String),
}

---
a dangling pointer—a pointer that references a location in memory that may have been given to someone else—by freeing some memory while preserving a pointer to that memory.

---
The println! macro can do many kinds of formatting, and by default, the curly brackets tell println! to use formatting known as Display: output intended for direct end user consumption

---
they allow you to refer to some value without taking ownership of it

---
double free error

---
In other words, because it’s a separate value from the String, there’s no guarantee that it will still be valid in the future

---
Tuple Structs Without Named Fields

---
Self

---
_

---
ampersands represent references

---
 another advantage

---
 Rust does not have nulls, but it does have an enum that can encode the concept of a value being present or absent. This enum is Option<T>

---
&mut s

---
Matches Are Exhaustive

---
If a type implements the Copy trait, variables that use it do not move, but rather are trivially copied, making them still valid after assignment to another variable

---
Note that a reference’s scope starts from where it is introduced and continues through the last time that reference is used

---
Struct Update Syntax

---
lifetimes

---
Enums and Pattern Matching

---
In short, because Option<T> and T (where T can be any type) are different types, the compiler won’t let us use an Option<T> value as if it were definitely a valid value

---
Here, s goes out of scope and is dropped, so its memory goes away.

---
String Slices


---

The concepts of ownership, borrowing, and slices ensure memory safety in Rust programs at compile time

---
 ..user1

---
Catch-All

---
=>

---
multiple immutable references are allowed because no one who is just reading the data has the ability to affect anyone else’s reading of the data.


---
Patterns That Bind to Values

---
how to define and instantiate structs

---
 we must exhaust every last possibility in order for the code to be valid

---
you can keep associated pieces of data connected to each other and name each piece to make your code clear

---
some_string: &mut String

---
Rust doesn’t have the null feature that many other languages have

---
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

---
s: &str

---
String Literals as Slices

---
lifetimes

---
As in real life, if a person owns something, you can borrow it from them. When you’re done, you have to give it back. You don’t own it.

---
 The benefit of having this restriction is that Rust can prevent data races at compile time

---
A slice is a kind of reference, so it does not have ownership.

---
there’s a design choice that’s implied by this: Rust will never automatically create “deep” copies of your data

---
the last pattern will match all values not specifically listed

---
useful when you want to give the whole tuple a name and make the tuple a different type from other tuples, and when naming each field as in a regular struct would be verbose or redundant.

---
What if we want to let a function use a value but not take ownership?

---
Stack-Only Data: Copy

---
we use a double colon to separate the two

---
&self, other: &Rectangle

---
The Rules of References


---
Method Syntax

---
Self

---
 any group of simple scalar values can implement Copy

---
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

---
There’s no reason to separate these methods into multiple impl blocks here, but this is valid syntax

---
Return Values and Scope

---
Note that we have to put the catch-all arm last

---
the compiler guarantees that references will never be dangling references

---
Dangling References

---
types such as integers that have a known size at compile time are stored entirely on the stack, so copies of the actual values are quick to make

---
 aliases for the type that appears after the impl keyword, which in this case is Rectangle.