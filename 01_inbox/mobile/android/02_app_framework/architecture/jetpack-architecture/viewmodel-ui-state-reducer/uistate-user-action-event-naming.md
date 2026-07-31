# UiState, User Action, Event 이름 구분

상위 노트: [[viewmodel-ui-state-reducer]]

Android에는 이미 플랫폼 `Intent`가 있습니다. 그래서 화면 내부 user action 이름으로 `Intent`를 쓰면 딥 링크나 시스템 인텐트 문서와 헷갈릴 수
있습니다.

이 프로젝트 문서에서는 다음 이름을 권장합니다.

| 개념                          | 권장 이름                       | 예시                                          |
|:----------------------------|:----------------------------|:--------------------------------------------|
| 화면이 그릴 최신 상태                | `UiState`                   | `SignInUiState`                             |
| UI에서 ViewModel로 올라가는 사용자 행동 | `UiAction` 또는 명시적 함수        | `SignInUiAction.IdChanged`, `onIdChanged()` |
| 한 번 처리하고 사라지는 신호            | `UiEvent` 또는 feature별 event | `SignInEvent.SignInSucceeded`               |
| Android OS 컴포넌트 요청          | `Intent`                    | `android.content.Intent`                    |

단순 화면에서는 sealed `UiAction`을 만들 필요가 없습니다. 아래처럼 명시적 함수가 더 읽기 쉽습니다.

```kotlin
fun onEmailChanged(email: String)
fun onPasswordChanged(password: String)
fun onSubmitClick()
```

action 타입은 다음 상황에서 도입합니다.

- user action 종류가 많아져서 reducer나 handler로 모아야 할 때
- 테스트에서 `oldState + action -> newState`를 명확히 검증하고 싶을 때
- 같은 action을 ViewModel, Reducer, preview fixture에서 공유해야 할 때

---
