---
title: dsl-syntax-does-not-change-ownership-lifetime-contracts
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:28:45 +09:00
---

## DSL 문법은 ownership 과 lifetime 계약을 바꾸지 않는다
배경 지식: [의존성 역전 원칙](../../../../../../02_references/oop/solid/DIP%28Dependency%20Inversion%20Principle%29.md), [독립 수명 모델](../../../00_foundations/learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)

Compose, Gradle Kotlin DSL, Koin DSL, Navigation DSL은 선언을 읽기 쉽게 만들지만 owner와 lifetime을 자동으로 올바르게 만들어 주지는 않는다. DSL 안에 쓰였다는 이유만으로 state, graph, route, build configuration의 책임이 사라지지 않는다. Koin도 classic runtime DSL과 compiler plugin 사용 여부를 구분해서 본다.

DI/Navigation 관련 DSL 을 볼 때는 문법보다 "무엇을 선언하는가", "누가 실행하는가", "언제 생성되고 언제 사라지는가", "어느 모듈이 이 이름을 알 수 있는가"를 먼저 본다.

### 같은 DSL, 다른 lifetime

```kotlin
val appModule = module {
    single<UserRepository> { RealUserRepository(get()) }
    factory { LoadUser(get()) }
}
```

`single`과 `factory`는 생성·재사용 규칙을 표현하지만 Android owner를 자동으로 선택하지 않는다. 누가 Koin application을 시작·종료하는지, 화면 scope를 누가 close하는지, `UserRepository`가 어떤 Context를 잡는지를 별도로 결정해야 한다. 같은 원칙은 declarative navigation이나 Compose의 `remember`에도 적용된다.

### 실패와 관찰 신호

- 화면 종료 뒤 scoped instance가 사라지지 않으면 scope close 지점과 owner callback을 확인한다.
- classic Koin DSL의 graph 연결은 test에서 `module.verify()`로 앞당겨 검증한다. `checkModules()`는 Koin 4.0부터 deprecated이다.
- DSL block 안의 `get()` 연쇄가 길어지면 constructor signature에서 dependency가 보이는지 다시 확인한다.

관련 노트: [Navigation contracts](../../navigation/navigation-contracts/navigation-contracts.md)

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Koin module verification](https://insert-koin.io/docs/reference/koin-test/verify/), [Koin Android scopes](https://insert-koin.io/docs/4.1/reference/koin-android/scope/)
