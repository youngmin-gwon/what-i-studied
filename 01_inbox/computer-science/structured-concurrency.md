---
title: structured-concurrency
tags: [computer-science, concurrency, coroutines, async]
aliases: [Structured Concurrency, 구조적 동시성, CoroutineScope, Parent-Child Cancellation]
date modified: 2026-08-06 16:25:00 +09:00
date created: 2026-08-06 16:25:00 +09:00
---

## Structured Concurrency (구조적 동시성) 이란 무엇인가

**Structured Concurrency (구조적 동시성)** 는 비동기(Asynchronous) 작업의 생명주기(Lifetime)를 단일 스레드 코드의 블록 범위(Block Scope)처럼 **명확한 부모-자식(Parent-Child) 계층 구조**로 묶어서 관리하는 비동기 프로그래밍 패러다임이다.

구조적 프로그래밍(Structured Programming)에서 `if`, `for`, `try-catch` 블록이 실행 흐름의 시작과 끝을 명확히 제한하여 `goto` 문의 난잡함을 해결했듯, Structured Concurrency는 비동기 스레드/코루틴의 **"시작된 위치와 끝나는 위치를 제어할 수 없는 난잡함(Unstructured Async)"** 을 해결한다.

```
[Unstructured Async (GlobalScope / Fire-and-Forget)]
Caller ───> Launch Child 1 (어디서 끝나는지, 언제 죽는지 모름 - Orphan Task)
       ───> Launch Child 2 (에러 발생해도 Parent 가 알 수 없음 - Silent Failure)

[Structured Concurrency (CoroutineScope / Parent-Child Hierarchy)]
Parent Scope (Job)
 ├──> Child Task 1 (Job)
 └──> Child Task 2 (Job) ──(Exception 발생)──> Parent 에게 예외 전파 ──> 모든 Child 취소 (Cancellation Propagation)
 Parent는 모든 자식이 완료될 때까지 기다렸다가 종료됨.
```

---

## 핵심 원칙 및 작동 메커니즘

### 1. 부모-자식 생명주기 계층 구조 (Parent-Child Hierarchy)
- 모든 동시성 작업(코루틴)은 특정 `Scope` 또는 부모 `Job` 내에서만 생성될 수 있다.
- 부모 작업은 자신 내부에서 새로 생성된 모든 자식 작업의 참조(Child Jobs)를 추적 관리한다.
- **완료 보장**: 부모 작업은 자신의 모든 자식 작업이 완료(Completed)되거나 취소(Cancelled)될 때까지 스스로의 완료를 미룬다.

### 2. 취소 및 예외 전파 (Cancellation & Exception Propagation)
- **부모 ➔ 자식 (Downwards Cancellation)**: 부모 작업이 취소되면 모든 자식 작업에게 취소 신호가 즉시 하향 전파된다.
- **자식 ➔ 부모 (Upwards Exception Propagation)**: 자식 작업 중 하나에서 비정상 예외(Unhandled Exception)가 발생하면:
  1. 부모 작업에게 예외가 즉시 상향 전파된다.
  2. 부모 작업은 다른 모든 형제(Sibling) 자식 작업들을 취소한다.
  3. 부모 작업 자신도 예외 상태로 종료된다. (`SupervisorJob`을 사용할 경우 예외의 상향 전파를 억제하여 형제 작업을 유지할 수 있음).

---

## Unstructured Async vs Structured Concurrency 비교

비구조적 비동기(GlobalScope, `Thread.start()`, `CompletableFuture`, `async/await` 무단 사용)와 구조적 동시성의 차이는 다음과 같다:

| 항목 | Unstructured Async (비구조적) | Structured Concurrency (구조적) |
| :--- | :--- | :--- |
| **생명주기 관리** | 백그라운드에서 고아(Orphan) 상태로 실행됨 | 부모 Scope 의 생명주기에 종속됨 |
| **자원 누수 (Leak)** | 고아 스레드/작업이 메모리와 자원을 무한 점유 가능 | 부모 Scope 파괴 시 모든 자식 작업 즉시 취소 |
| **예외 처리** | 예외가 유실(Silent Fail)되거나 전역 어플리케이션 크래시 | 부모 계층을 타고 안전하게 전파되어 캡처 가능 |
| **완료 수집** | `join()` 또는 `Future.get()`을 일일이 수동 호출 | 부모 작업이 자식들의 완료를 자동 대기 및 취합 |
| **예시 (Kotlin)** | `GlobalScope.launch { ... }` | `coroutineScope { launch { ... } }` |

---

## 자원 누수(Resource Leak) 방지 효과

1. **화면/컴포넌트 파괴 시 백그라운드 작업 자동 정지**:
   - Android 의 `viewModelScope`나 `lifecycleScope` 등과 결합하면, 화면(Activity/Fragment/ViewModel)이 파괴(Destroy)될 때 Scope 가 cancel 되며 진행 중이던 네트워크 요청, DB 쿼리, 파일 I/O 작업이 즉시 취소된다.
2. **고아 작업(Orphan Task) 생성 억제**:
   - 비구조적 비동기에서는 함수가 종료된 후에도 백그라운드 스레드가 멈추지 않고 메모리를 점유할 위험이 크지만, 구조적 동시성에서는 범위(Scope)를 벗어나기 전에 모든 비동기 작업이 정리된다.
3. **[Context](context.md) 의 안전한 계층 상속**:
   - 자식 작업은 부모의 `CoroutineContext` (Dispatcher, ExceptionHandler 등)를 자동으로 상속받으면서 독립적인 `Job`을 구성한다.

---

## 관련 노트
- [Context](context.md)
- [Race Condition and Deadlock](race-condition-and-deadlock.md)
- [Immutability](immutability.md)
