---
title: immutability
tags: [computer-science, software-architecture, functional-programming, concurrency]
aliases: [Immutability, Immutable, 불변성, 불변 객체]
date modified: 2026-08-06 16:25:00 +09:00
date created: 2026-08-06 16:25:00 +09:00
---

## Immutability (불변성) 이란 무엇인가

소프트웨어 공학에서 **Immutability (불변성)** 란 **"객체 또는 데이터 구조가 생성(Initialization)된 이후에는 그 내부의 상태(State)를 변경할 수 없는 성질"** 을 의미한다.

반대로 상태를 자유롭게 변경할 수 있는 성질은 **Mutability (가변성)** 라고 한다.

```
[Mutable Object]
var user = User("Alice") ───(수정 가능)───> user.name = "Bob" (동일 참조, 상태 오염 가능)

[Immutable Object]
val user1 = User("Alice") ───(수정 불가)───> val user2 = user1.copy(name = "Bob") (새 객체 생성)
```

---

## 불변성(Immutability)이 제공하는 핵심 이점

1. **스레드 안전성 (Thread Safety) 보장**:
   - 가변 상태를 여러 스레드가 동시에 읽고 쓸 때 발생하는 경쟁 상태(Race Condition)와 데이터 오염을 예방한다.
   - 불변 객체는 읽기(Read-only) 전용이므로 복잡한 Mutex, Lock, Synchronization 기법 없이도 동시성 환경에서 100% 안전하다.

2. **예측 가능성과 부작용(Side-Effect) 방지**:
   - 함수나 컴포넌트로 객체를 전달할 때, 외부에서 이 객체를 몰래 수정(Mutation)할 위험이 없다.

3. **고성능 동등성 비교 (Reference Equality Optimization)**:
   - 객체의 내부 필드를 일일이 비교(Structural Equality)하지 않고, 객체의 **메모리 주소 참조(Reference Equality, `===`)** 만으로 빠르게 변경 여부를 감지할 수 있다.

---

## Jetpack Compose / React 선언적 UI에서의 불변성

Jetpack Compose 런타임은 상태(State) 변경을 감지하고 UI를 재구성(Recomposition)할 때 **불변 객체(Immutable Objects)** 에 강하게 의존한다.

- **Recomposition Skip (스킵 최적화)**:
  - Composable 함수의 입력 파라미터가 불변(Immutable) 상태이고 이전 렌더링 때와 동일한 참조/값이면, Compose 런타임은 해당 Composable의 재구성을 안전하게 건너뛸(Skip) 수 있다.
- **State Mutation 주의점**:
  - `List` 내부 요소를 `list.add()` 로 변경하면 객체 참조 자체가 바뀌지 않아 Compose 가 상태 변경을 감지하지 못할 수 있다. 대신 `toPersistentList()` 나 `copy()` 를 이용해 새로운 불변 객체를 생성해야 한다.

---

## 연결 문서

- [Pure Function](pure-function.md) - 불변 데이터를 기반으로 동작하는 순수 함수 레퍼런스
- [Side Effect](../../02_references/computer-science/side-effect.md) - 불변성이 차단하는 상태 변이와 부작용
- [Composable Body Must Be Fast, Idempotent and Side-Effect Free](../mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composable-body-must-be-fast-idempotent-and-side-effect-free.md) - Compose 본문 규약
