---
title: architecture-decisions-start-from-owner-lifetime-and-survival-requirements
tags: [android, android/architecture, android/jetpack]
aliases: ["아키텍처 결정은 owner, lifetime, survival 요구에서 시작한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 아키텍처 결정은 owner, lifetime, survival 요구에서 시작한다

안드로이드 앱에서 **특정 상태(State)나 작업(Task)을 "어느 클래스/레이어에 둘 것인가?"에 대한 아키텍처적 결정은 라이브러리 선호도가 아니라 소유자(Owner), 유효 수명(Lifetime), 그리고 OS 이벤트로부터의 생존 요구조건(Survival Requirements)에 기초**한다.

---

### 1. 개념 및 핵심 명제 (What)

- **소유자 수명 (Owner Lifetime)**:
  - **Composition Lifetime**: 컴포저블 노드가 UI 트리에 활성화되어 있는 동안만 유효 (`remember`, `rememberSaveable`).
  - **[viewmodel](../../../viewmodel.md) Lifetime**: 화면 회전(Configuration Change)을 넘어서 살아남는 UI 관산자 수명.
  - **Process Lifetime**: 앱 프로세스 시작부터 종료까지 지속되는 수명 (Application Context, Hilt Singleton Component).
  - **Persistent Storage Lifetime**: 기기 재부팅, 앱 업데이트, 프로세스 사멸 시에도 보존되는 영속 수명 (Room, DataStore).
- **생존 요구조건 (Survival Requirements)**:
  화면 회전에 살아남아야 하는가? 프로세스 데스(Process Death)에 살아남아야 하는가? 아니면 재부팅 후에도 유지되어야 하는가?

---

### 2. 왜 소유자와 수명 기준인가? (Why)

1. **상태 유실 및 앱 크래시 예방**: 단순 인메모리 필드에 저장된 중요한 결제 정보나 입력 서식이 백그라운드 프로세스 사멸 시 유실되는 비극을 방지한다.
2. **과도한 영속성 사용 억제**: 스크롤 위치나 임시 애니메이션 토글 상태를 굳이 Disk DataStore 에 기록하여 I/O 오버헤드와 렌더링 지연을 초과 발생시키지 않도록 적절한 수명 계층에 매핑한다.

---

### 3. 수명 주기 및 상태 배치 매트릭스 (How)

```mermaid
flowchart TD
    A["새로운 데이터/상태 설계"] --> B{"화면 회전에 생존 필요한가?"}
    B -- "아니오 (UI 렌더링 노드에 종속)" --> C["Composition Scoped (remember)"]
    B -- "예" --> D{"프로세스 데스(Process Death)에 생존 필요한가?"}
    D -- "예 (소량의 상태: ID, 입력 텍스트)" --> E["ViewModel SavedStateHandle"]
    D -- "예 (대용량/핵심 도메인 데이터)" --> F["Repository + Persistent Storage (Room / DataStore)"]
    D -- "아니오 (화면 회전에만 대응)" --> G"ViewModel In-Memory [stateflow"]
```

---

### 4. 현대 표준 코드 예시 (수명 요구별 상태 분리)

```kotlin
@HiltViewModel
class OrderViewModel @Inject constructor(
    private val savedStateHandle: SavedStateHandle,
    private val orderRepository: OrderRepository
) : ViewModel() {

    // 1. Process Death 생존 필요 소량 상태 -> SavedStateHandle
    val orderId: StateFlow<String> = savedStateHandle.getStateFlow("order_id", "")

    // 2. Persistent 생존 대용량 상태 -> Repository single source of truth
    val orderDetail: StateFlow<OrderDetailUiState> = orderId
        .flatMapLatest { id -> orderRepository.observeOrderDetail(id) }
        .map { order -> OrderDetailUiState.Success(order) }
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5000),
            initialValue = OrderDetailUiState.Loading
        )
}
```

---

### 5. 관측 가능 증거 및 진단 (Observability)

- **Process Death 수명 생존성 검증**:
  `adb shell am kill <package_name>` 실행 후 앱 복구 시 `SavedStateHandle` 및 DataStore 에서 데이터가 정상 복원되는지 관측.

---

### 6. 관련 문서 및 참조

- 상위 문서: [Architecture Contracts](./architecture-contracts.md)
- 관련 계약 문서:
  - [UI, domain, data layer는 rendering, policy, source of truth를 분리한다](./ui-domain-data-layers-separate-rendering-policy-and-source-of-truth.md)
  - [SavedStateHandle은 프로세스 데스의 소량 상태를 복구한다](../../state-management/viewmodel/savedstatehandle-restores-small-process-death-state.md)
- 공식 문서: [UI State persistence](https://developer.android.com/topic/architecture/ui-layer/stateholder#save-state)

검증일: 2026-08-05. Owner Lifetime 및 Survival Requirements 원문 대조 완료.
