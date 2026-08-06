---
title: exception-propagation-needs-supervision-boundary
tags: [android, android/async, android/coroutines, android/data]
aliases: ["Coroutine 예외 전파는 builder와 supervision boundary가 결정한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Coroutine 예외 전파는 builder와 supervision boundary가 결정한다

### 개념 (What)
Coroutine 체인 내에서 처리되지 않은 예외(Unhandled Exception)가 발생했을 때, 예외가 트리 상부의 부모 Coroutine으로 전파되어 **형제 Coroutine까지 함께 취소시킬 것인지**, 아니면 **해당 자식 노드 수준에서 실패를 격리(Supervision Boundary)할 것인지** 결정하는 규칙이다.

### 왜 필요한가 (Why)
1. **단일 실패의 전역 파급 방지**: 예를 들어 메인 화면에서 "사용자 프로필", "알림 목록", "광고 배너" 3개 데이터를 동시에 불러올 때, "광고 배너" 로딩 실패가 전체 화면 렌더링을 취소하거나 앱 프로세스를 크래시시키는 비합리성을 막아야 한다.
2. **Builder별 예외 처리 방식 이해**: `launch`는 발생 즉시 예외를 부모로 던지지만, `async`는 예외를 `Deferred` 객체 내부에 캡슐화하여 `await()` 호출 시점에 비로소 재전파한다. 두 빌더의 차이를 모르면 미처리 예외 크래시나 누락이 발생한다.

### 내부 메커니즘 (How)
1. **Job의 `childCancelled()` 전파 규칙**:
   - 일반 `JobImpl`: 자식 Coroutine에서 `CancellationException` 이외의 예외가 발생하면 `childCancelled(cause)`가 호출되고, 부모 `Job`에 `true`를 반환한다. 이에 따라 부모는 즉시 `Cancelling` 상태로 전환되어 나머지 모든 자식 Coroutine에 취소 명령을 내린다.
   - `SupervisorJobImpl`: `childCancelled(cause)` 메서드가 항상 `false`를 반환하도록 오버라이드되어 있다. 따라서 자식의 실패가 부모 `Job`을 취소시키지 않으며, 동형 형제(Sibling) Coroutine들은 계속 정상 동작한다.
2. **`supervisorScope` 대 `SupervisorJob` 주의사항**:
   - `SupervisorJob()`을 생성하여 `launch(SupervisorJob())` 처럼 자식의 CoroutineContext로 직접 전달하면, **자식이 또 다른 자식을 생성한 것이 아니므로 아무런 격리 효과가 없다** (새로 넘긴 SupervisorJob이 부모와의 연관 관계를 깨버리거나 전파를 막지 못함).
   - 따라서 안전한 예외 격리를 위해서는 반드시 `supervisorScope { ... }` 블록을 사용하거나, 최상위 Scope 자체를 `CoroutineScope(SupervisorJob() + Dispatchers.Main)` 형태로 생성해야 한다.
3. **`CoroutineExceptionHandler` (CEH)**:
   - 미처리 예외가 최상위(Root) Coroutine까지 도달했을 때 마지막 핸들러로 동작한다. 자식 Coroutine 내부의 `launch`에 붙인 CEH는 무시되며, 반드시 Root Scope에 등록되어야 효과를 발휘한다.

```mermaid
graph TD
    subgraph "Standard Job (Cancelled Together)"
        A1["Parent Job"] --> B1["Child Coroutine A (Failed!)"]
        A1 --> C1["Child Coroutine B (Cancelled by Parent)"]
        B1 -->|"childCancelled() = true"| A1
    end

    subgraph "SupervisorJob / supervisorScope (Isolated)"
        A2["Supervisor Parent Job"] --> B2["Child Coroutine A (Failed!)"]
        A2 --> C2["Child Coroutine B (Runs Normally)"]
        B2 -.->"childCancelled() = false"| A2
    end

    style B1 fill:#ffebee,stroke:#c62828,color:#b71c1c
    style C1 fill:#ffebee,stroke:#c62828,color:#b71c1c
    style B2 fill:#ffebee,stroke:#c62828,color:#b71c1c
    style C2 fill:#e8f5e9,stroke:#388e3c,color:#1b5e20
```

### 현대 표준 vs 레거시 비교

| 비교 항목 | 레거시 (RxJava / UncaughtExceptionHandler) | 현대 표준 (Kotlin Coroutines) |
| :--- | :--- | :--- |
| **실패 전파** | `onError` 미구현 시 RxJavaPlugins 전역 에러 훅으로 크래시 | [structured concurrency](../../../../../../computer-science/structured-concurrency.md) 트리를 따라 부모/형제 자동 취소 |
| **독립 격리** | `onErrorResumeNext()`로 개별 스트림 처리 | `supervisorScope` 또는 `SupervisorJob`으로 하부 트리 실패 격리 |
| **최종 예외 수집** | `Thread.setDefaultUncaughtExceptionHandler()` | `CoroutineExceptionHandler` (Root Scope 전용) |

### Idiomatic Kotlin 코드 예시

```kotlin
class DashboardViewModel(
    private val userRepository: UserRepository,
    private val adRepository: AdRepository
) : ViewModel() {

    private val exceptionHandler = CoroutineExceptionHandler { _, throwable ->
        Log.e("DashboardVM", "Root Supervisor Caught Unhandled Error: ${throwable.message}")
    }

    fun loadDashboardData() {
        // viewModelScope는 기본적으로 SupervisorJob을 포함하므로 각 launch 실패가 서로를 취소시키지 않음
        viewModelScope.launch(exceptionHandler) {
            // supervisorScope 내에서 두 개의 병렬 비동기 작업을 격리 실행
            supervisorScope {
                val userJob = launch {
                    fetchUserData()
                }
                
                val adJob = launch {
                    // 광고 서비스 실패 시 이 코루틴만 종료되고 userJob에는 영향을 주지 않음
                    fetchAdBannerData()
                }
            }
        }
    }

    private suspend fun fetchUserData() {
        // 사용자 정보 로딩
    }

    private suspend fun fetchAdBannerData() {
        throw IOException("Ad Server 500 Internal Error")
    }
}
```

공식 문서: [Coroutine exceptions handling](https://kotlinlang.org/docs/exception-handling.html)
