---
title: top-level-destination-owns-adaptive-navigation-chrome
tags: []
aliases: []
date modified: 2026-07-31 18:20:33 +09:00
date created: 2026-07-31 17:13:53 +09:00
---

## Top-level destination 과 adaptive navigation chrome

상위 문서: [Adaptive Navigation 계약](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-contracts.md)

관련 정본: [NavKey와 back stack은 앱이 소유하는 navigation 상태다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navkey-and-back-stack-are-app-owned-navigation-state.md)

### top-level 은 앱의 persistent frame 이다

로그인 후 앱에는 Dashboard, Measure, Training, Settings 처럼 사용자가 반복해서 오가는 top-level destination 이 있다.

이 destination 은 단순히 현재 화면 하나를 뜻하지 않고, 각 feature 흐름의 진입점과 선택 상태를 뜻한다.

top-level 선택과 detail navigation 을 같은 동작으로 처리하면 탭 전환 때 하위 문맥이 손실된다.

각 destination 이 자신의 stack 을 유지하고, 선택된 destination 의 stack 을 표시하는 모델이 적합하다.

```text
Dashboard: DashboardRoute
Training: TrainingRoute -> TrainingDetailRoute(id)
Settings: SettingsRoute -> AccountSettingsRoute
```

탭 전환은 `replaceTopLevel()` 로 전체 stack 을 지우는 명령이 아니다.

`selectedDestination` 를 바꾸고 해당 destination 의 stack 을 `NavDisplay` 에 연결하는 상태 전환이다.

### chrome 은 window 에 적응한다

`NavigationSuiteScaffold` 는 같은 top-level destination 집합을 window 조건에 맞는 chrome 으로 표시한다.

compact window 에서는 navigation bar, 넓은 window 에서는 rail 또는 drawer 를 사용할 수 있다.

항목의 의미와 선택 상태는 공유하고, chrome 의 배치만 적응시킨다.

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

chrome 은 content route 의 세부 화면을 모두 알아야 하지 않는다.

top-level marker 나 별도 destination enum 으로 선택 상태를 관리하고, detail route 는 feature stack 안에서 처리한다.

dialog 나 full-screen 예외처럼 chrome 을 숨겨야 하는 경우에는 entry metadata 를 scene decorator 가 해석하게 할 수 있다.

이 구조는 앱 frame 의 navigation 과 feature 내부의 content layout 을 분리한다.

adaptive navigation 의 기본 방향은 [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation) 에서 확인할 수 있다.
