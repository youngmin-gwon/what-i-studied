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
- packages of code are referred to as _crates_