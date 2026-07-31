# 여러 데이터 합치기: combine

홈 화면은 여러 출처의 데이터를 합쳐서 만드는 경우가 많습니다.

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

`combine`은 각 Flow의 최신값을 모아 하나의 UI 상태로 만듭니다.
