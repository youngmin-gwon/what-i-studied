# Top-level destination과 adaptive navigation chrome

상위 문서: [Adaptive Navigation 계약](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-contracts.md)
관련 정본: [NavKey와 back stack은 앱이 소유하는 navigation 상태다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navkey-and-back-stack-are-app-owned-navigation-state.md)


## top-level은 앱의 persistent frame이다

로그인 후 앱에는 Dashboard, Measure, Training, Settings처럼 사용자가 반복해서 오가는 top-level destination이 있다.
이 destination은 단순히 현재 화면 하나를 뜻하지 않고, 각 feature 흐름의 진입점과 선택 상태를 뜻한다.

top-level 선택과 detail navigation을 같은 동작으로 처리하면 탭 전환 때 하위 문맥이 손실된다.
각 destination이 자신의 stack을 유지하고, 선택된 destination의 stack을 표시하는 모델이 적합하다.

```text
Dashboard: DashboardRoute
Training: TrainingRoute -> TrainingDetailRoute(id)
Settings: SettingsRoute -> AccountSettingsRoute
```

탭 전환은 `replaceTopLevel()`로 전체 stack을 지우는 명령이 아니다.
`selectedDestination`를 바꾸고 해당 destination의 stack을 `NavDisplay`에 연결하는 상태 전환이다.

## chrome은 window에 적응한다

`NavigationSuiteScaffold`는 같은 top-level destination 집합을 window 조건에 맞는 chrome으로 표시한다.
compact window에서는 navigation bar, 넓은 window에서는 rail 또는 drawer를 사용할 수 있다.
항목의 의미와 선택 상태는 공유하고, chrome의 배치만 적응시킨다.

```kotlin
NavigationSuiteScaffold(
    navigationSuiteItems = {
        item(
            selected = selected == MainDestination.Training,
            onClick = { selected = MainDestination.Training },
            icon = { TrainingIcon() },
            label = { Text("Training") },
        )
    },
) {
    SelectedDestinationContent(selected)
}
```

chrome은 content route의 세부 화면을 모두 알아야 하지 않는다.
top-level marker나 별도 destination enum으로 선택 상태를 관리하고, detail route는 feature stack 안에서 처리한다.
dialog나 full-screen 예외처럼 chrome을 숨겨야 하는 경우에는 entry metadata를 scene decorator가 해석하게 할 수 있다.

이 구조는 앱 frame의 navigation과 feature 내부의 content layout을 분리한다.
adaptive navigation의 기본 방향은 [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation)에서 확인할 수 있다.
