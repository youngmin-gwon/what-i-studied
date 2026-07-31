---
title: "여러 원천의 최신값으로 화면 상태를 만들 때 combine을 사용한다"
tags: [android, android/data, android/async, android/flow-state-contracts]
aliases: ["여러 원천의 최신값으로 화면 상태를 만들 때 combine을 사용한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 여러 원천의 최신값으로 화면 상태를 만들 때 combine을 사용한다

상위 문서: [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)


홈 화면처럼 사용자, 혜택 목록, 읽지 않은 알림처럼 독립적인 원천을 함께 그릴 때 `combine`을 사용한다.
`combine`은 각 Flow가 최소 한 번 값을 방출한 뒤, 어느 원천이 바뀔 때마다 각 원천의 최신값을 묶어 내보낸다.

```kotlin
val uiState: StateFlow<HomeUiState> =
    combine(
        userRepository.observeUser(),
        benefitRepository.observeBenefits(),
        notificationRepository.observeUnreadCount(),
    ) { user, benefits, unreadCount ->
        HomeUiState(
            userName = user.name,
            benefits = benefits,
            unreadCount = unreadCount,
        )
    }.stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = HomeUiState(),
    )
```

화면은 여러 Repository를 직접 수집하지 않고 ViewModel의 단일 `UiState`를 수집한다.
각 원천의 최신값을 조합하는 규칙도 ViewModel에 모이므로 화면 코드가 단순해진다.

초기값이 없는 원천은 `onStart`, `stateIn`의 초기값 또는 도메인 기본값으로 준비한다.
오류를 화면 전체 오류로 볼지 일부 영역의 오류로 볼지도 조합 전에 결정한다.
한 원천의 방출 빈도가 높으면 필요한 경우 `distinctUntilChanged`로 불필요한 상태 생성을 줄인다.

`zip`처럼 같은 순번의 값을 기다리는 것이 아니라 최신 스냅샷을 만드는 것이 `combine`의 목적이다.

조합 결과의 기본값은 실제 화면의 빈 상태와 일치해야 한다.
원천 Flow의 오류와 로딩을 조합할 필요가 있다면 각 원천의 상태 타입을 먼저 정의한다.

조합 순서보다 각 값의 의미와 초기 방출 조건을 테스트한다.
한 원천이 값을 내지 않으면 전체 화면 상태가 아직 만들어지지 않을 수 있다.
각 원천에 적절한 초기값이나 로딩 모델을 제공한다.
조합 후 최종 상태는 UI가 직접 이해할 수 있는 값으로 유지한다.
원천의 변경이 화면 전체 갱신을 요구하는지 영역별 상태가 필요한지도 판단한다.
필요하면 더 작은 상태로 나누되 최종 수집 경계는 lifecycle-aware하게 둔다.
조합 로직은 순수 변환으로 유지하면 테스트하기 쉽다.
각 원천의 최신값으로 같은 화면 상태가 재현되는지 검증한다.
