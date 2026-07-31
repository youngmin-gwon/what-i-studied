# 상태와 일회성 이벤트를 구분한다

상위 노트: [[viewmodel-ui-state-reducer]]

`UiState`는 "지금 화면이 무엇을 그려야 하는가"입니다. 새 collector가 들어왔을 때 다시 받아도 되는 값이어야 합니다.

```kotlin
data class ProfileUiState(
    val isLoading: Boolean = false,
    val name: String = "",
    val errorMessage: String? = null,
)
```

일회성 이벤트는 "한 번만 처리해야 하는 신호"입니다.

```kotlin
sealed interface SignInEvent {
    data object NavigateHome : SignInEvent
    data class ShowSnackbar(val message: String) : SignInEvent
}
```

주의할 점은 공식 UI events 가이드가 ViewModel에서 발생한 UI 동작도 가능하면 상태로 표현하라고 권장한다는 점입니다. 특히 프로세스 복원 후에도 이어져야 하는
흐름은 event stream보다 `UiState`가 안전합니다.

| 상황                            | 권장 표현                                               |
|:------------------------------|:----------------------------------------------------|
| 로딩, 입력값, 검증 오류, 선택된 탭         | `UiState`                                           |
| 화면 회전 후에도 유지되어야 하는 목적지 상태     | `UiState` 또는 navigation state                       |
| Snackbar 한 번 표시               | `SharedFlow` 또는 `Channel`, 필요 시 consume callback    |
| 로그인 완료 후 루트 화면 전환             | 단순 앱에서는 event 가능, 복원 가능성이 중요하면 session state 변화로 표현 |
| 결제, 본인인증처럼 중간 단계 복원이 중요한 flow | `UiState`에 현재 단계와 결과를 명시                            |

즉, `Channel`이나 `SharedFlow`가 틀린 것은 아닙니다. 다만 "놓치면 안 되는 상태"를 event로만 표현하면 화면 재생성, collector 재시작, 프로세스
복원에서 흐름이 약해집니다.

---
