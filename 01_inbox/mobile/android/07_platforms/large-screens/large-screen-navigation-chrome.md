---
title: large-screen-navigation-chrome
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## 큰 화면 내비게이션은 목적지 중요도와 창 폭에 따라 chrome 을 바꾼다

상위 문서: [큰 화면 적응 계약](./large-screen.md)

큰 화면 내비게이션은 같은 top-level destination 을 다른 chrome 으로 표현하는 문제다. compact 의 bottom bar 가 medium 이상에서는 navigation rail 이나 drawer 로 바뀌어도 앱의 목적지 모델은 유지되어야 한다.

### 언제 중요한가

앱이 phone, tablet, foldable, desktop window 를 모두 지원하면 navigation chrome 과 back stack 책임이 쉽게 뒤섞인다. chrome 은 창 폭에 적응하지만, 어떤 화면이 목적지인지와 deep link 가 어디로 들어오는지는 별도 계약으로 남아야 한다.

### 내비게이션 스위칭 메커니즘 (Compose Navigation Suite)

```kotlin
@Composable
fun AdaptiveNavigationApp(
    windowSizeClass: WindowSizeClass = currentWindowAdaptiveInfo().windowSizeClass
) {
    val navSuiteType = NavigationSuiteScaffoldDefaults.calculateFromAdaptiveInfo(
        currentWindowAdaptiveInfo()
    )

    NavigationSuiteScaffold(
        navigationSuiteItems = {
            Destinations.entries.forEach { dest ->
                item(
                    icon = { Icon(dest.icon, contentDescription = dest.label) },
                    label = { Text(dest.label) },
                    selected = currentDestination == dest,
                    onClick = { onNavigateTo(dest) }
                )
            }
        }
    ) {
        // App Content Pane
        MainContentScreen()
    }
}
```

### 실무 규칙

- top-level destination 목록은 창 크기와 독립적으로 정의한다.
- 창이 넓어질수록 navigation rail, permanent drawer, supporting pane 을 검토한다.
- adaptive navigation 은 앱 내부 navigation graph 나 deep link 해석을 대신하지 않는다.
- navigation chrome 전환이 현재 선택 상태, focus, accessibility traversal 을 잃지 않는지 확인한다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 창 폭 변경에 따른 내비게이션 바/레일 레이아웃 노드 관측
adb shell dumpsys activity service AccessibilityManagerService

# 화면 전환 시 Focus 엔티티 유지 검증
adb shell dumpsys input | grep -i "focused"
```

### 관련 문서

- [적응형 레이아웃은 같은 화면을 늘리는 것이 아니라 구조를 바꾼다](adaptive-layout-structure.md)

공식 문서: [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)

