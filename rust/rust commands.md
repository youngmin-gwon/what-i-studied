---
aliases: []
date created: 2024-12-09 21:31:10 +09:00
date modified: 2024-12-16 12:20:57 +09:00
tags: [command, rust]
title: rust commands
---

```bash
rustup --version
rustc --version
cargo --version
```

- check version

```bash
rustc filename.rs
```

- build executable with rust compiler
- 간단한 프로그램의 경우 문제 없지만, 프로젝트가 커지면 cargo 사용

```bash
rustfmt filename.rs
```

- formatting 하기

```bash
cargo build
```

- build executable file in  `./target/debug/project-name`
- `--release`: with optimization

```bash
cargo run
```

- compile the code and then run the resulting executable all

```bash
cargo check
```

- check your code to make sure it compiles but doesn't produce an executable
- much faster than `cargo build`
