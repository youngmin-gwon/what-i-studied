---
title: composable-body-must-be-fast-idempotent-and-side-effect-free
tags: [android, compose/runtime, jetpack-compose]
aliases: [Fast, Idempotent, Side-effect-free]
date modified: 2026-08-05 13:50:47 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Composable body 는 빠르고 idempotent 하며 side-effect free 해야 한다

### 1. 핵심 원칙 용어 서술 (What)

Composable 함수의 본문(Body)은 다음 세 가지 정밀한 규약을 반드시 준수해야 한다:

1. **빠름 (Fast)**: 16.6ms(60fps) 또는 8.3ms(120fps) 프레임 타임 내에 완료될 수 있도록 본문 내에 I/O, 디스크 읽기/쓰기, 정렬/복잡한 연산 등의 무거운 동작이 없어야 한다.
2. **멱등성 (Idempotent)**: 동일한 입력 파라미터가 전달되면 항상 동일한 UI 트리를 생성해야 하며, 몇 번을 실행하더라도 동일한 결과를 보장해야 한다.
3. **부작용 없음 (Side-Effect Free)**: 함수 본문 직접 실행 과정에서 외부 상태를 변경하거나(전역 변수 수정, 파일 쓰기, 분석 이벤트 전송), 비동기 코루틴 작업을 시작하는 등의 **부작용(Side Effect)** 이 일어난다.

---

### 2. 제약의 필요성 (Why)

Compose Runtime 은 성능 및 동시성 최적화를 위해 다음과 같은 비결정론적 실행 특성을 가질 수 있다:

- **실행 순서 미보장**: 하위 Composable 함수들이 코드에 작성된 순서대로 실행되지 않고 컴파일러 최적화에 의해 병렬 또는 임의의 순서로 실행될 수 있다.
- **병렬 실행 (Parallel Recomposition)**: 런타임은 여러 코어에서 Composable 함수를 동시에 실행할 수 있다.
- **취소 및 재시도 (Cancellation & Preemption)**: Composition 도중 새로운 State 변경이 들어오면, 진행 중이던 Composition 작업을 중간에 취소하고 새 State 로 처음부터 다시 계산을 시작한다.

따라서 함수 본문 내에 Side Effect 나 무거운 작업이 포함되어 있으면 데이터 오염, 예기치 않은 재실행 횟수 폭증, UI 멈춤 현상(Jank)이 발생한다.

---

### 3. 내부 동작 및 이펙트 격리 메커니즘 (How)

```
[Composition Phase: Composable Body 실행]
  |-- 순수 함수 연산 (UI Description 계산만 수행)
  |-- Side Effect 실행 금지!
  |-- Effect 람다는 등록만 진행 (LaunchedEffect, DisposableEffect)
  |
  v
[Composition 완료 및 Slot Table 커밋]
  |
  v
[Effect Execution Phase: 등록된 Side Effect 실행]
```

- **Effect APIs 에 격리**: 데이터 로딩, 네트워크 요청, 분석 이벤트 전송 등 부작용이 수반되는 모든 동작은 `LaunchedEffect`, `DisposableEffect`, 또는 `SideEffect` 블록으로 감싸서 Composition 파이프라인 외부로 격리해야 한다.
- **연산 메모제이션**: 계산 비용이 큰 로직은 `remember { … }` 나 `derivedStateOf { … }` 로 메모제이션하거나 ViewModel 등의 영역으로 이관한다.

---

### 4. 올바른 패턴과 안티패턴 코드 비교

```kotlin
// ❌ 안티패턴: Composable Body 내에서 직접 Side Effect 및 무거운 연산 수행
@Composable
fun BadUserProfile(userId: String, analytics: Analytics) {
    // 1. 순수성 위반: Recomposition 때마다 이벤트가 이중/삼중으로 중복 발송됨
    analytics.logEvent("view_profile", mapOf("user_id" to userId))

    // 2. Fast 규약 위반: Composition 도중 I/O 읽기로 인한 UI Jank 발생
    val rawJson = File("/sdcard/user_$userId.json").readText()

    Text("User Profile: $rawJson")
}

// ✅ 올바른 패턴: Side Effect 격리 및 State 선언
@Composable
fun GoodUserProfile(userId: String, analytics: Analytics) {
    // Composition이 성공적으로 완료된 후 1회/userId 변경 시에만 안전하게 실행됨
    LaunchedEffect(userId) {
        analytics.logEvent("view_profile", mapOf("user_id" to userId))
    }

    // 파일 로딩 등 무거운 작업은 ViewModel/Coroutines 영역에서 처리하고 State로 관찰
    Text("User Profile Screen: $userId")
}
```

---

상위 문서: [Jetpack Compose 런타임과 상태 모델의 기본 개념](../compose-runtime-and-state-model.md)

관련 노트: [Composable과 함께 취소되어야 하는 작업은 LaunchedEffect로 시작한다](../../state-and-lifecycle/compose-state-and-effect-contracts/launched-effect-owns-composable-cancellable-work.md), [무거운 작업은 composition 안에 두지 않는다](../../performance/compose-performance-contracts/heavy-work-does-not-belong-in-composition.md)

출처: [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model), [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)

검증일: 2026-08-05. Compose 공식 가이드의 "Side-effects in Compose" 및 "Thinking in Compose" 문서 원문을 대조하여 순수 함수, 멱등성, Recomposition 건너뛰기/취소 메커니즘과 Effect API 격리 서술을 정밀 보강했다.
