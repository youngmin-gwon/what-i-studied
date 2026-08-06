---
title: side-effect
tags: [computer-science, functional-programming, jetpack-compose, software-architecture]
aliases: [Side Effect, Side-effect, 부수 효과, 부작용]
date modified: 2026-08-06 16:20:20 +09:00
date created: 2026-08-06 16:20:00 +09:00
---

## Side Effect (부작용 / 부수 효과) 란 무엇인가

소프트웨어 공학에서 **Side Effect (부수 효과 / 부작용)** 란 **"함수 또는 연산이 자신의 반환값(Return Value)을 생성하는 주된 목적(Main Effect) 이외에, 함수 외부의 상태를 변경하거나 외부 세계와 상호작용하는 모든 행위"** 를 의미한다.

의학 용어인 '부작용'에서 유래했지만, 컴퓨터 과학에서는 "해로운 버그"만을 뜻하는 것이 아니라 **"주 목적을 벗어나는 모든 상태 변화 및 I/O 동작"** 을 가리키는 중립적인 용어다.

```
[Pure Function / Main Effect Only]
Input (x) ───────> [ Function f ] ───────> Output f(x)
                   (외부 상호작용 없음)

[Function with Side Effect]
Input (x) ───────> [ Function f ] ───────> Output f(x)
                        │
                        ▼ (Side Effect 발생!)
               - 전역 변수 / 외부 객체 수정
               - DB / 파일 / 네트워크 I/O
               - 화면 출력 (log, Toast)
               - 비동기 코루틴 시작
```

---

## 핵심 특징과 구분 (Pure Function vs Side Effect)

### 순수 함수 (Pure Function)

- 동일한 입력에 대해 항상 동일한 출력을 반환한다.
- **Side Effect 가 완전히 없다 (Side-Effect Free).**
- 외부 상태를 읽거나 쓰지 않으며, 평가(Evaluation) 시점이나 횟수에 의존하지 않는다.

### Side Effect 를 유발하는 동작들

1. **외부 상태 변이 (State Mutation)**: 전역 변수, 싱글톤 객체, 클래스 인스턴스 멤버 변수 수정
2. **I/O 작업**: 파일 읽기/쓰기, 네트워크 API 호출, 데이터베이스 Query/Mutation, 콘솔/로그 출력 (`println`, `Log.d`)
3. **비동기 및 동시성 작업 트리거**: 코루틴/스레드 시작 (`CoroutineScope.launch`), 비동기 작업 등록
4. **시간/비결정적 요소 의존**: `System.currentTimeMillis()`, `Random.nextInt()` 등 매 실행 시 달라지는 외부 데이터 조회
5. **UI Framework Side Effect**: UI 렌더링 파이프라인 외부에서의 Toast/Snackbar 표시, Navigation 전환

---

## 프로그래밍 맥락별 Side Effect 의 역할과 관리

### 1. 함수형 프로그래밍 (FP)

FP 에서는 Side Effect 가 코드의 예측 가능성(Reasoning), 메모제이션, 캐싱, 병렬 처리를 방해한다고 본다.

따라서 비즈니스 로직을 순수 함수로 작성하고, Side Effect 는 프로그램의 극히 일부(최외각 경계/모나드 등)로 **격리(Isolation)** 하는 것을 목표로 한다.

### 2. UI 프레임워크 (Jetpack Compose, React 등)

Jetpack Compose 나 React 같은 선언적 UI 프레임워크에서 **Side Effect 의 정의는 매우 구체적**이다:

>**"Composable 함수 본문(Composition) 실행 영역 밖에서 일어나는 모든 앱 상태의 변경 및 외부 상호작용"**

Composable 함수는 **"State 를 받아 UI Description 을 반환하는 순수 함수"** 처럼 동작해야 한다.

Compose 런타임은 성능 최적화를 위해 Composable 함수를 비동기적으로 취소, 재시도, 임의의 순서로 실행(Parallel/Preempted Recomposition)할 수 있다.

만약 Composable 함수 본문 내에 Side Effect(네트워크 호출, analytics 발송 등)가 직접 위치하면 다음과 같은 참사가 일어난다:

- 화면이 1 번 그려질 때 analytics 이벤트가 10 번 중복 발송됨
- Recomposition 중간에 취소되면서 데이터베이스 오염 발생
- UI Jank(버벅임) 발생

따라서 Compose 는 이러한 부작용을 Composition 완료 후 안전한 라이프사이클 단계로 미루기 위해 `LaunchedEffect`, `DisposableEffect`, `SideEffect` 같은 **Effect APIs** 를 제공한다.

---

## 연관 개념 비교 Matrix

| 개념 | 정의 | Side Effect 허용 여부 | 핵심 보장 성질 |
| :--- | :--- | :--- | :--- |
| **순수 함수 (Pure Function)** | 입력값만으로 출력을 만들고 외부 상태 미변경 | ❌ 절대 금지 | 입력이 같으면 항상 출력 동일 |
| **멱등성 (Idempotency)** | N 번 실행해도 최종 결과 상태가 1 번 실행과 동일 | ⭕ 허용 (단, 상태 변화가 중복 누적되면 안 됨) | `f(f(x)) = f(x)` (반복 실행 안전성) |
| **Side Effect** | 반환값 생성 외의 모든 외부 상태 변경 및 I/O 행위 | N/A (개념 자체) | 프로그램 외부 세계와의 상호작용 |

---

## 실제 예시 코드 (Kotlin / Compose)

```kotlin
// ❌ Side Effect 가 포함된 비순수 함수 및 Composable (안티패턴)
var globalCounter = 0 // 외부 상태

fun addAndLog(a: Int, b: Int): Int {
    globalCounter++ // Side Effect 1: 외부 상태 변이
    println("Adding $a and $b") // Side Effect 2: I/O (콘솔 출력)
    return a + b
}

@Composable
fun BadProfileScreen(userId: String, analytics: Analytics) {
    // ❌ Composition 파이프라인 내부에서 직접 Side Effect 실행
    analytics.sendViewEvent(userId) // Recomposition 마다 중복 실행됨!
    Text("User: $userId")
}

// ✅ Side Effect 가 격리된 올바른 작성법
fun pureAdd(a: Int, b: Int): Int = a + b // 순수 함수

@Composable
fun GoodProfileScreen(userId: String, analytics: Analytics) {
    // ✅ Composition 완료 후 1회 또는 userId 변경 시에만 격리되어 실행됨
    LaunchedEffect(userId) {
        analytics.sendViewEvent(userId)
    }
    Text("User: $userId")
}
```

---

## 연결 문서

- [[idempotency]] - Side Effect 가 존재하더라도 최종 상태를 동일하게 보장하는 멱등성에 관한 레퍼런스
- [[composable-body-must-be-fast-idempotent-and-side-effect-free]] - Compose 런타임의 3 대 규약과 Side Effect 격리 원칙
- [[launched-effect-owns-composable-cancellable-work]] - LaunchedEffect 를 통한 Side Effect 라이프사이클 제어
