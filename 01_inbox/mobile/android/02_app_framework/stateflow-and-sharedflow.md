---
title: stateflow-and-sharedflow
tags: [android, kotlin, coroutines, flow, reactive]
aliases:
  - StateFlow & SharedFlow
  - StateFlow
  - SharedFlow
  - Coroutines Flow
date created: 2026-08-06
date modified: 2026-08-06
---

# StateFlow & SharedFlow

## 1. 개요 (Overview)

Kotlin Coroutines의 **`StateFlow`**와 **`SharedFlow`**는 수집기(Collector)의 존재 여부와 무관하게 데이터를 생산하고 브로드캐스팅할 수 있는 **Hot Stream** 기반의 셰어드 파이프라인이다.

Cold Stream인 일반 `Flow`가 `collect` 시점에 새로 실행되는 것과 달리, Hot Stream은 메모리상에 활성화되어 여러 수집자(Subscribers/Collectors)에게 동일한 데이터를 공유(Multicast)할 수 있으며, Android의 [single-source-of-truth](single-source-of-truth.md) 아키텍처에서 UI State 및 Event를 다루는 핵심 도구로 활용된다.

---

## 2. StateFlow 상세 (StateFlow Details)

`StateFlow`는 **상태(State)를 보관하고 전달하기 위해 특화된 Hot Stream**이다.

### 주요 특징 및 동적 메커니즘
- **상태 보관 (State-holding)**: 항상 최신 상태 값을 내부 필드(`value`)에 저장하고 유지한다.
- **초기값 필수**: 생성 시점에 반드시 초기 상태값(Initial Value)이 지정되어야 한다.
- **Replay 버퍼 크기 = 1**: 항상 가장 최신의 마지막 발행 값 1개만을 저장하여 새로운 수집기가 등록되면 그 즉시 최신 상태를 전달받는다.
- **`distinctUntilChanged` 자동 적용**: 이전 값과 `equals` 비교하여 동일한 데이터가 재발행될 경우 컬렉터에게 중복 통지하지 않는다.
- **사용 목적**: 화면의 상태 표현 (예: UI State, 폼 데이터, 네트워크 상태 등 연속적인 상태 보관).

```kotlin
private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
val uiState: StateFlow<UiState> = _uiState.asStateFlow()
```

---

## 3. SharedFlow 상세 (SharedFlow Details)

`SharedFlow`는 상태를 보관하는 데 얽매이지 않고 **이벤트(Event)를 발행하고 여러 수집기에게 방송(Multicast)하는 범용적인 Hot Stream**이다.

### 주요 특징 및 동적 메커니즘
- **유연한 버퍼 및 Replay 설정**: `replay`, `extraBufferCapacity`, `onBufferOverflow` 등 다양한 정책을 정의할 수 있다.
- **초기값 불필요**: 초기 상태 없이 생성 가능하며 `replay = 0` 설정 시 이벤트를 수신자가 수집 중일 때만 전달한다.
- **Equality 비교 없음**: 동일한 값이나 동일 객체가 연속 발행되더라도 배제하지 않고 매번 통지한다.
- **사용 목적**: 사건/이벤트 스트림 브로드캐스트 (예: 푸시 알림, 도메인 이벤트 처리 등).

```kotlin
private val _eventFlow = MutableSharedFlow<UserEvent>(
    replay = 0,
    extraBufferCapacity = 1,
    onBufferOverflow = BufferOverflow.DROP_OLDEST
)
val eventFlow: SharedFlow<UserEvent> = _eventFlow.asSharedFlow()
```

---

## 4. StateFlow vs SharedFlow 비교 (Comparison)

| 비교 속성 | `StateFlow` | `SharedFlow` |
| :--- | :--- | :--- |
| **개념적 역할** | 상태(State) 보유 및 표현 | 이벤트(Event) 배출 및 통지 |
| **초기값 (Initial Value)** | **필수** (`StateFlow(initialValue)`) | **불필요** |
| **최신 값 접근** | `flow.value` 프로퍼티 지원 | 지원하지 않음 (`replayCache` 참조만 가능) |
| **Replay 크기** | 고정값 `1` | 사용자 지정 가능 (`0` 이상) |
| **중복 값 동등성 검사** | **자동 적용** (`distinctUntilChanged`) | **적용되지 않음** (동일 값도 계속 발행) |
| **인터페이스 관계** | `SharedFlow`의 특수화 형태 (`interface StateFlow : SharedFlow`) | 최상위 공유 Flow 인터페이스 |

---

## 5. UI 이벤트 유실(Event Loss) 위험성 분석

과거에는 Toast 메시지, Snackbar 출력, 화면 이동(Navigation) 등 일회성(One-off) UI 이벤트를 처리하기 위해 `SharedFlow(replay = 0)`나 `SingleLiveEvent` 등을 주로 사용하는 패턴이 확산되었으나, **Android 공식 아키텍처 가이드라인에서는 일회성 UI 이벤트에 SharedFlow 사용을 지양**하도록 권장한다.

### SharedFlow / LiveData를 UI 이벤트에 쓸 때 발생하는 원인 및 위험

```
               [ViewModel] -- (SharedFlow Event) --> X (이벤트 유실!)
                                                     |
                                         Lifecycle STARTED 이전
                                         (화면 회전 / 백그라운드)
                                                     |
                                              [UI Collector]
```

1. **Lifecycle 감지와 이벤트 유실 (Event Loss)**
   - UI 계층에서는 안전한 수집을 위해 `repeatOnLifecycle(Lifecycle.State.STARTED)` 등을 활용한다.
   - 앱이 백그라운드 상태이거나 화면 구성 변경(Configuration Change, 기기 회전 등) 중에는 Lifecycle이 `STOPPED` 상태가 되어 수집(Collection)이 중지된다.
   - 이때 ViewModel에서 `SharedFlow(replay = 0)`로 이벤트를 발행하면, **수집기가 차단되어 있어 이벤트를 수신하지 못하고 이벤트가 영구적으로 유실(Event Loss)**된다.

2. **Replay 설정 시의 재방행(Re-emission) 부작용**
   - 유실을 막기 위해 `replay = 1`을 부여할 경우, 화면이 회전되어 UI가 재구독될 때 이미 처리한 화면 이동이나 스낵바 이벤트가 **다시 노출되는 부작용**이 발생한다.

### 최신 권장 해결 방안 (Recommended Architecture)

- **UDF 기반 UI State 패턴 전환 (Best Practice)**:
  - 일회성 이벤트도 별도의 이벤트 스트림이 아닌 **UI State 내부의 데이터(예: `isSnackbarVisible = true`, `userMessage = "..."`)로 모델링**한다.
  - UI가 상태를 받아 메시지를 표시한 후, 완료 시점에 ViewModel에 이벤트 처리 완료 이벤트를 전달하여 UI State를 다시 클리어(`isSnackbarVisible = false`)하는 [single-source-of-truth](single-source-of-truth.md) 원칙을 준수한다.
- **Channel 패턴 활용 (필요 시)**:
  - 진정으로 일회성 버퍼링 이벤트 전송이 불가피한 경우 `Channel`을 열고 `receiveAsFlow()` 형태로 노출하여 1개 이상의 수집자가 준비될 때까지 소비를 대기시키는 구조를 채택한다.

---
## 연관 문서
- [binder-ipc](../01_system_internals/binder-ipc.md)
- [single-source-of-truth](single-source-of-truth.md)
