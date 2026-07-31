# SharedFlow와 Channel은 상태 저장소가 아니라 일회성 신호 전달 수단이다

상위 문서: [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)


상태는 새 구독자가 다시 받아야 하지만, 이벤트는 발생한 순간 한 번 처리하면 끝난다.
Snackbar, Toast, Navigation, 외부 화면 열기는 현재 화면 상태가 아니라 일회성 신호다.
이 신호를 `StateFlow`에 넣으면 화면 재생성 때 같은 이벤트가 다시 실행될 위험이 있다.

## SharedFlow와 Channel

`SharedFlow`는 여러 구독자에게 이벤트를 방송하는 hot stream이다.
기본 `replay = 0`이면 늦게 들어온 구독자는 과거 이벤트를 받지 않는다.
`Channel`은 보내는 쪽과 받는 쪽 사이의 전달 순서를 보장하는 큐다.
이벤트를 반드시 한 소비자가 처리해야 하는 의미라면 `Channel.receiveAsFlow()`를 고려한다.

```kotlin
private val _events = MutableSharedFlow<ProfileEvent>()
val events: SharedFlow<ProfileEvent> = _events.asSharedFlow()

private val _navigation = Channel<NavEvent>()
val navigation: Flow<NavEvent> = _navigation.receiveAsFlow()

fun save() {
    viewModelScope.launch {
        repository.save()
        _events.emit(ProfileEvent.Saved)
    }
}
```

화면에 계속 보여야 하는 로딩과 오류는 `StateFlow`의 `UiState`로 유지한다.
이벤트 수집은 화면이 이벤트를 처리하는 스코프에서 별도로 실행한다.
Compose에서는 `LaunchedEffect`에서 이벤트를 수집하고, 상태는 `collectAsStateWithLifecycle`로 수집한다.

`SharedFlow`의 `replay`와 버퍼 설정은 이벤트 유실 허용 여부에 맞춰 명시한다.
여러 구독자가 모두 받아야 하는 이벤트인지, 한 곳만 처리해야 하는 이벤트인지 먼저 결정한다.

이벤트에 식별 가능한 sealed 타입을 사용하면 소비자가 처리할 종류를 빠뜨리기 어렵다.
이벤트 처리 실패를 재시도해야 한다면 신호를 상태나 영속 큐로 바꾸는 별도 정책을 세운다.

화면 재생성 뒤 같은 Snackbar가 다시 떠야 하는지 먼저 결정한다.
다시 떠야 한다면 이벤트가 아니라 화면 상태로 모델링한다.
소비자가 화면 lifecycle에 맞춰 이벤트를 처리하는지도 함께 확인한다.
이벤트의 유실 허용 여부를 문서화하면 replay 설정을 임의로 바꾸기 어렵다.
상태와 이벤트를 같은 모델에 섞지 않는 것이 재수집 버그를 줄이는 핵심이다.
공개 API는 읽기 전용 `SharedFlow` 또는 `Flow`로 제한한다.
