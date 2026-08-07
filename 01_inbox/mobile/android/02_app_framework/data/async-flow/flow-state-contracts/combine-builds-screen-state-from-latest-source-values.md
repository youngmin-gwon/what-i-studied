---
title: combine-builds-screen-state-from-latest-source-values
tags: [android, android/async, android/flow, android/state]
aliases: ["combine은 최신 소스 값으로 화면 상태를 만든다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## combine은 최신 소스 값으로 화면 상태를 만든다

### 개념 (What)
`combine`은 **두 개 이상의 독립적인 `Flow` 스트림을 하나로 결합**하는 연산자다. 결합 대상이 되는 소스 Flow들 각각에서 최소 1개 이상의 데이터가 발행된 후부터 동작하며, **소스 Flow 중 어느 하나라도 새로운 값을 발행할 때마다 각 소스의 '최신 값(Latest Value)'들을 모아 연산 람다를 재실행**한다.

### 왜 필요한가 (Why)
1. **복수 데이터 소스 기반의 화면 합성**: 실제 안드로이드 앱 화면은 "유저 프로필 DB", "쇼핑카트 카운트 DataStore", "실시간 네트워크 상태" 등 여러 곳에서 오는 데이터를 융합해서 만들어진다. `combine`을 쓰면 상태 파편화를 막고 단일 `UiState`로 합성할 수 있다.
2. **`zip`과의 명확한 차이점**: `zip`은 소스 A와 소스 B의 데이터가 1:1로 짝을 맞춰 발행될 때까지 기다린다. 반면 `combine`은 짝을 기다리지 않고 한쪽이 업데이트되면 즉시 최신 상태로 화면을 갱신하므로 UI 상태 합성에 적합하다.

### 내부 메커니즘 (How)
1. **`combineInternal`과 채널 어레이**:
   - `combine`은 각 소스 Flow마다 전용 채널 버퍼를 할당하여 비동기로 수집한다.
   - 각 소스의 최신 값을 저장하는 배열(`latestValues`)을 유지한다. 모든 소스가 최소 1번 값을 방출하여 배열이 채워지면, 이후 소스 중 하나라도 새 값을 내놓을 때마다 합성 람다 함수를 실행하여 결과를 하류로 emit 한다.

```mermaid
graph TD
    A["Flow 1: User Profile"] --> C["combine(flow1, flow2, flow3)"]
    B["Flow 2: Cart Items"] --> C
    D["Flow 3: Network Status"] --> C
    
    C -->|"Any source updates -> Compute with latest values"| E["HomeScreenUiState"]
    E --> F"[stateflow -> Jetpack Compose UI"]

    style A fill:#e1f5fe,stroke:#0288d1,color:#01579b
    style B fill:#e1f5fe,stroke:#0288d1,color:#01579b
    style C fill:#fff3e0,stroke:#f57c00,color:#e65100
    style F fill:#e8f5e9,stroke:#388e3c,color:#1b5e20
```

### 현대 표준 vs 레거시 비교

| 비교 항목 | 레거시 (RxJava combineLatest / MediatorLiveData) | 현대 표준 (Kotlin combine) |
| :--- | :--- | :--- |
| **결합 방식** | `Observable.combineLatest()` 또는 `MediatorLiveData.addSource()` 수동 수집 | `combine(flow1, flow2) { f1, f2 -> UiState(f1, f2) }` |
| **파라미터 확장** | 최대 9개까지 다중 연산자 람다 서술 가능 | 2~5개 및 Array 기반 n개 수 합성 지원 |
| **예외 처리** | 소스 하나 실패 시 전역 onError 발생 | `catch` 연산자와 결합하여 각 소스 단위 안전한 에러 핸들링 |

### Idiomatic Kotlin 코드 예시

```kotlin
data class CartUiState(
    val user: User,
    val cartItems: List<CartItem>,
    val totalPrice: BigDecimal
)

class CartViewModel(
    userRepository: UserRepository,
    cartRepository: CartRepository
) : ViewModel() {

    val uiState: StateFlow<CartUiState?> = combine(
        userRepository.userStream,
        cartRepository.cartItemsStream
    ) { user, items ->
        val total = items.sumOf { it.price * it.quantity.toBigDecimal() }
        CartUiState(
            user = user,
            cartItems = items,
            totalPrice = total
        )
    }.stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = null
    )
}
```

공식 문서: [Flow combine](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/combine.html)
