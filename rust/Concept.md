## Rust is ahead-of-time compiled language
- you can compile a program and give the executable to someone else, and they can run it even without having Rust installed
- not like python, javascript, ruby

## Cargo is Rust’s build system and package manager
- what cargo does
	- building your code
	- downloading the libraries your code depends on
	- building those libraries
 
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

## Traits