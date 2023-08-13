## Rust is ahead-of-time compiled language

you can compile a program and give the executable to someone else, and they can run it even without having Rust installed

not like python, javascript, ruby

## Rust is expression-based language

## `rustc` is compiler itself 

not directly used
 
## `cargo` is Rust’s build system and package manager

what cargo does

	- building your code
	- downloading the libraries your code depends on
	- building those libraries

## `rust-analyzer` is implementation of LSP for Rust

setting for terminal tools
```bash
rustup component add rust-analyzer
```

## `clippy` is official rust linter

(default) added

if not added in some environment like minimal CI tools, use this command

 ```bash
rustup component add clippy
```

linter setup can be declared in `clippy.toml` file in the project

## `rustfmt` is official rust formatter

(default) added

if not added in some environment like minimal CI tools, use this command

 ```bash
rustup component add rustfmt
```
## TOML

- Tom's Obvious, Minimal Language
```toml
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]

```
- `[package]`
	- a section heading that indicates that the following statements are configuring a package
- `[dependencies]`
	- the start of a section for you to list any of your project’s dependencies
 
## Crates

- a collection of Rust source code files

## Prelude

- = standard library

## &

- a _reference_, which gives you a way to let multiple parts of your code access one piece of data without needing to copy that data into memory multiple times
- immutable by default

## Placeholder

- `{}`

```rust
let x = 5; 
let y = 10; 
println!("x = {x} and y + 2 = {}", y + 2);
```

## Cargo.lock

- a mechanism that ensures you can rebuild the same artifact every time you or anyone else builds your code:
	- Cargo will use only the versions of the dependencies you specified until you indicate otherwise.

## rustup

a command line tool for managing Rust versions and associated tools

## naming convention

`variable` : camel_case_with_ 
`constant` : CAMEL_CASE_WITH_UPPER_CASE

## Shadow?

An old variable with name "a" is replaced by a new variable with name "a"
=> The second variable overshadows the first variable

### Difference between mut and shadowing
1. we'll get compile-time error if we accidentally try to reassign to this variable without using the let keyword
2. because we’re effectively creating a new variable when we use the `let` keyword again, we can change the type of the value but reuse the same name.

# Ownership

It works to prevent from `double free error` 
## double free error

A bug happening when a program tries to free memory twice