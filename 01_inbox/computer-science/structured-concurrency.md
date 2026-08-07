---
title: structured-concurrency
tags: [async, cancellation-propagation, computer-science, concurrency, coroutines, structured-concurrency]
aliases: [Structured Concurrency, 구조화된 동시성, 비구조화 동시성 비교]
date modified: 2026-08-07 13:53:25 +09:00
date created: 2026-08-07 13:53:00 +09:00
---

## Structured Concurrency (구조화된 동시성 & 비구조화 동시성 비교)

### 1. 개요 (Overview)

**Structured Concurrency (구조화된 동시성)** 는 비동기(Asynchronous) 동시성 작업의 수명주기(Lifecycle)를 명확한 부모 - 자식 계층 구조(Parent-Child Hierarchy)로 묶어 관리하는 **컴퓨터 공학 동시성 프로그래밍 패러다임**이다.

과거의 **Unstructured Concurrency (비구조화된 동시성)** 에서는 스레드나 백그라운드 작업(`GlobalScope`, `Thread`)이 통제 없이 산발적으로 생성되어 부모가 종료되어도 자식 작업이 고아(Orphan Task)로 남아 메모리 누수(Memory Leak)나 자원 낭비를 유발했다. Structured Concurrency 는 **"부모 스코프는 모든 자식 작업이 완료될 때까지 종료되지 않으며, 부모가 취소되면 자식도 함께 취소된다"**는 엄격한 약속을 보장한다.

---

#### 초보자를 위한 쉽게 이해하는 비유

- **Structured vs Unstructured Concurrency (직속 상사 팀 구조 vs 무책임한 용역 기사)**:
  - **Unstructured Concurrency (무책임한 용역 기사)**: 작업 반장(부모)이 일을 시키고 집으로 퇴근(종료)해 버려도, 혼자 남아 밤새도록 엔진을 켜두고 전기를 낭비하는 고아 기사.
  - **Structured Concurrency (직속 상사 팀 구조)**: 부모 팀장이 모든 부하 팀원(자식 작업)이 일을 끝낼 때까지 곁을 지키며, 팀장이 작업 중단 명령(취소)을 내리면 모든 팀원이 즉시 도구를 놓고 함께 퇴근하는 엄격한 수명주기 팀 모델.

```mermaid
graph TD
    subgraph "Structured Concurrency (부모-자식 트리 수명주기)"
        ParentScope["Parent CoroutineScope"] -->|"1. Child Launch"| ChildA["Child Job A"]
        ParentScope -->|"2. Child Launch"| ChildB["Child Job B"]
        ParentScope -->|"3. Cancel Signal"| CancelProp["취소 신호 자식으로 일괄 자동 전파"]
        CancelProp --> ChildA
        CancelProp --> ChildB
    end
```

---

### 2. Structured vs Unstructured Concurrency 비교

| 구분 | Unstructured Concurrency (비구조화) | Structured Concurrency (구조화) |
| :--- | :--- | :--- |
| **수명주기 결합** | 독립적 (부모 종료와 자식 실행이 따로 돎) | **명확한 계층적 결합 (Parent-Child Hierarchy)** |
| **고아 작업 (Orphan Task)** | 발생 가능 (`GlobalScope`, 독립 Thread) | **원천 차단 (부모 스코프 범위 내 캡슐화)** |
| **취소 전파 (Cancellation)** | 수동으로 일일이 취소 제어해야 함 | **부모 취소 시 자식으로 자동 전파 (Propagation)** |
| **예외 처리 (Exception)** | 자식의 에외가 허공으로 사라지거나 미처리 크래시 | **자식의 예외가 부모로 전파되어 안전 수집** |
| **실제 대표 예시** | `Thread.start()`, `GlobalScope.launch` | `coroutineScope {}`, `viewModelScope` |

---

### 3. 실전 코드 예시 (Kotlin Coroutines)

```kotlin
// 1. Unstructured Concurrency (위험: 부모가 끝나도 GlobalScope 작업은 죽지 않음)
fun runUnstructured() {
    GlobalScope.launch {
        delay(5000)
        println("부모가 죽어도 혼자 계속 실행됨 (메모리 누수 위험)")
    }
}

// 2. Structured Concurrency (안전: coroutineScope 가 자식 완료를 보장)
suspend fun runStructured() = coroutineScope {
    launch {
        delay(1000)
        println("자식 작업 1 완료")
    }
    launch {
        delay(2000)
        println("자식 작업 2 완료")
    }
    // 두 자식이 모두 끝날 때까지 runStructured() 는 종료되지 않음
}
```

---

### 4. 연결 문서 (Related Links)

- [Kotlin Coroutines](../mobile/android/02_app_framework/kotlin-coroutines.md) - Structured Concurrency 기반 안드로이드 비동기 엔진
- [Compose SSOT](../mobile/android/02_app_framework/compose-ssot.md) - ViewModel / StateScope 수명주기 연동
- [Race Condition & Deadlock](race-condition-and-deadlock.md) - 동시성 레이스 조건 및 교착 상태
- [Pure Function](pure-function.md) - Side-Effect 없는 [부수 효과](side-effect.md) 통제
