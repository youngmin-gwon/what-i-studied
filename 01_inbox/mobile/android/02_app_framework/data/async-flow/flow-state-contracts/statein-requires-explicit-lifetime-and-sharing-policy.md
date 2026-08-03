---
title: Flow를 StateFlow로 바꿀 때는 stateIn의 수명과 공유 정책을 명시한다
tags: [android, android/data, android/async, android/flow-state-contracts]
aliases: ["Flow를 StateFlow로 바꿀 때는 stateIn의 수명과 공유 정책을 명시한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Flow를 StateFlow로 바꿀 때는 stateIn의 수명과 공유 정책을 명시한다

상위 문서: [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)


`stateIn`은 cold `Flow`를 특정 CoroutineScope에서 공유되는 `StateFlow`로 바꾼다.
이 변환은 단순한 타입 변환이 아니라 수명, 시작 시점, 초기값을 결정하는 설계다.

```kotlin
val uiState: StateFlow<BenefitUiState> =
    repository.observeBenefits()
        .map { BenefitUiState.Ready(it) }
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5_000),
            initialValue = BenefitUiState.Loading,
        )
```

`scope`는 공유된 흐름이 언제 취소되는지를 결정한다.
화면 단위 상태라면 보통 `viewModelScope`를 사용해 구성 변경에도 상태를 유지한다.
`initialValue`는 첫 원천 값이 오기 전 화면이 그릴 값이어야 한다.

## 공유 정책

- `Eagerly`는 `stateIn`을 만든 즉시 시작하고 scope가 끝날 때까지 유지한다.
- `Lazily`는 첫 구독자 이후 시작하며 구독자가 없어도 시작된 흐름을 유지한다.
- `WhileSubscribed(5_000)`은 구독자가 없어진 뒤 5초 후 upstream을 중지한다.

`WhileSubscribed`의 지연 시간은 회전 같은 짧은 구독 공백에서 재실행을 줄이는 정책이다.
백그라운드에서도 반드시 최신화해야 한다면 화면 수명보다 긴 scope와 다른 정책이 필요하다.
반대로 비용이 큰 원천 작업은 구독자가 없을 때 중지하는 편이 적절하다.

`stateIn` 전에 `catch`를 두어 upstream 오류를 화면 상태로 변환한다.
공유 정책을 생략한 축약 호출은 기본값을 숨기므로, 화면 상태에서는 인자를 이름으로 명시한다.

선택한 정책은 데이터 비용과 화면 요구사항으로 설명할 수 있어야 한다.
특히 구독자가 사라졌을 때 upstream을 계속 돌려야 하는지 여부를 코드 리뷰에서 확인한다.

초기값은 임시 빈 목록인지 실제 로딩 상태인지 구분한다.
공유 정책을 바꾸면 네트워크 호출 횟수와 회전 시 동작을 함께 테스트한다.
구독자가 없는 동안 최신값을 유지해야 하는지 제품 요구사항을 기준으로 결정한다.
수명 정책은 상태의 소유자인 scope와 함께 읽어야 한다.
이 정책은 테스트에서 시작과 중지 시점을 검증할 수 있는 명시적 계약이다.
초기 상태가 사용자에게 보이는 첫 프레임을 결정한다.
따라서 빈 값과 로딩을 혼동하지 않는다.
화면 계약에 필요한 초기값을 선택한다.
