---
title: pure-function
tags: [computer-science, functional-programming, software-architecture]
aliases: [Pure Function, 순수 함수, Purity]
date modified: 2026-08-06 16:25:00 +09:00
date created: 2026-08-06 16:25:00 +09:00
---

## Pure Function (순수 함수) 란 무엇인가

소프트웨어 공학 및 함수형 프로그래밍(FP)에서 **Pure Function (순수 함수)** 이란 다음 두 가지 조건을 엄격하게 만족하는 함수를 말한다:

1. **동일 입력 - 동일 출력 (Deterministic)**: 동일한 인자(Argument)가 전달되면 매번 몇 번을 실행하더라도 항상 정확히 동일한 결과 값을 반환한다.
2. **부작용 없음 (Side-Effect Free)**: 함수가 평가(Evaluation)되는 과정에서 외부의 상태를 읽거나 변경하지 않으며, I/O 작업(파일, 네트워크, 콘솔 출력 등)을 일으키지 않는다.

```
[Pure Function]
Input: (x, y) ────────> [ f(x, y) = x + y ] ────────> Output: x + y
                        (외부 상태 접근 0)
                        (Side-effect 0)
```

---

## 순수 함수의 핵심 특성과 이점

1. **참조 투명성 (Referential Transparency)**:
   - 프로그램 내에서 함수 호출 표현식을 그 함수의 결과 값으로 언제든 대체하더라도 프로그램의 동작이 전혀 달라지지 않는다.
   - 예: `add(2, 3)` 표현식은 프로그램 어디서든 값 `5` 로 치환될 수 있다.

2. **안전한 병렬 및 동시성 처리 (Thread Safety)**:
   - 외부 가변 상태(Mutable State)에 접근하거나 수정하지 않으므로, 여러 스레드에서 동시에 이 함수를 호출해도 경쟁 상태(Race Condition)나 데이터 오염이 발생할 수 없다.

3. **쉬운 테스트 및 디버깅**:
   - 데이터베이스, 네트워크, 외부 환경(현재 시간, 전역 변수 등)을 묘사하기 위한 복잡한 Mocking / Stubbing 객체가 필요 없다. 단순히 입력값을 전달하고 반환값만 검증하면 된다.

4. **메모제이션 및 캐싱 (Memoization)**:
   - 입력값에 따른 결과가 100% 보장되므로, 비싼 연산 결과를 인자 값을 Key 로 하여 캐싱(Memoization)할 수 있다.

---

## 순수 함수 vs 비순수 함수 (Impure Function) 비교

| 항목 | 순수 함수 (Pure Function) | 비순수 함수 (Impure Function) |
| :--- | :--- | :--- |
| **결과 예측성** | 100% 결정론적 (Deterministic) | 매개변수 외 외부 환경에 따라 변할 수 있음 |
| **외부 상태 변이** | ❌ 절대 없음 | ⭕ 전역 변수 수정, DB/파일 변경 등 발생 |
| **I/O 작업** | ❌ 없음 | ⭕ Log 출력, 네트워크 API, 시간 조회 등 포함 |
| **예시 (Kotlin)** | `fun add(a: Int, b: Int) = a + b` | `fun addAndLog(a: Int, b: Int) = (a + b).also { println(it) }` |

---

## 선언적 UI 프레임워크에서의 의미 (Jetpack Compose, React)

Jetpack Compose 에서 `@Composable` 함수 본문(Composition)은 **"State 를 전달받아 UI Description 을 반환하는 순수 함수"** 개념을 지향한다.

Compose 런타임은 성능 최적화를 위해 Composable 함수를 비동기적/임의의 순서로 실행하거나 재실행(Recomposition)할 수 있다. 따라서 Composable 함수 내부가 순수 함수 조건을 위반(Side Effect 발생)하면, UI 렌더링 도중 데이터 오염 및 중복 로직 실행 버그가 발생한다.

---

## 연결 문서

- [Side Effect](../../02_references/computer-science/side-effect.md) - 순수 함수의 자격 요건 중 하나인 부작용(Side Effect) 부재에 관한 레퍼런스
- [Idempotency](../../02_references/computer-science/idempotency.md) - 순수성과 멱등성의 개념적 차이점 비교
- [Composable Body Must Be Fast, Idempotent and Side-Effect Free](../mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composable-body-must-be-fast-idempotent-and-side-effect-free.md) - Compose 런타임에서 Composable 본문이 순수해야 하는 이유
