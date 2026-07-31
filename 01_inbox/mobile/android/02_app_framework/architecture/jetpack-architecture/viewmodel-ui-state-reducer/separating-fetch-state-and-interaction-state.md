# Fetch 상태와 Interaction 상태를 꼭 합쳐야 하나

상위 노트: [viewmodel-ui-state-reducer](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer.md)

같은 화면에 보인다고 해서 모든 상태를 반드시 하나의 ViewModel에 합칠 필요는 없습니다. 기준은 "같은 화면인가"보다 **상태의 수명, 소유자, 변경 주기,
재사용 범위가 같은가**입니다.

수명별 API 선택을 더 넓게 보려면 [jetpack-compose-state-lifetime-api-selection](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection.md)를 함께 봅니다.

```text
같은 화면의 최종 UI 상태를 함께 결정한다
-> 한 ViewModel에서 조합해도 된다

수명, 소유자, 변경 주기, 재사용 범위가 다르다
-> ViewModel 또는 state holder를 분리하는 편이 낫다
```

예를 들어 `DataStore`에서 session이나 app setting을 읽는 흐름은 특정 화면 interaction이라기보다 앱 전역 상태 관찰에 가깝습니다. 이런 상태는
root/app scope의 `AppSessionViewModel`, 별도 observer, Repository Flow가 소유하는 편이 자연스럽습니다.

반대로 로그인 form, 회원가입 form, 결제 form의 입력값, validation, submit loading은 화면 단위 interaction state입니다. 이런 상태는 해당
screen 또는 navigation entry의 ViewModel이 소유하는 편이 좋습니다.

둘이 한 화면에 같이 필요하다면 route composable에서 각각 구독해 화면에 전달할 수 있습니다.

```kotlin
@Composable
fun SignInRoute(
    appSessionViewModel: AppSessionViewModel,
    signInViewModel: SignInViewModel,
) {
    val sessionState by appSessionViewModel.sessionState.collectAsStateWithLifecycle()
    val signInState by signInViewModel.uiState.collectAsStateWithLifecycle()

    SignInScreen(
        sessionState = sessionState,
        uiState = signInState,
        onSignInClick = signInViewModel::signIn,
    )
}
```

이 구조에서는 session 상태와 sign-in form 상태의 소유자가 다릅니다. 화면은 두 상태를 동시에 사용할 뿐입니다.

반대로 fetched data와 interaction state가 강하게 얽히면 한 ViewModel에서 조합하는 편이 더 읽기 쉽습니다.

```text
쿠폰 목록 fetch
+ 검색어
+ 정렬
+ 필터
+ 선택 상태
+ 새로고침
```

이런 화면은 `CouponViewModel` 하나가 Repository Flow와 사용자 입력 Flow를 `combine`해서 `CouponUiState` 하나를 만드는 구조가 자연스럽습니다.

판단 기준:

- `DataStore`/Room/Repository Flow 자체는 data layer가 소유합니다.
- 앱 전역 session/settings 관찰은 root/app ViewModel 또는 observer가 소유합니다.
- 화면 입력, 선택, validation, submit 상태는 screen ViewModel이 소유합니다.
- 두 상태가 하나의 화면 정책을 함께 결정하면 screen ViewModel에서 조합합니다.
- 단지 같은 화면에 보인다는 이유만으로 하나의 ViewModel에 합치지 않습니다.
- 단순 fetch-only 변환이 반복된다면 별도 ViewModel보다 Repository Flow, observer, 기존 screen ViewModel의 `stateIn` 중 무엇이 가장 단순한지 먼저 봅니다.

---
