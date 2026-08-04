---
title: standard-adaptive-scaffolds-should-precede-custom-layouts
tags: [android, android/adaptive, android/navigation]
aliases: ["표준 adaptive scaffold를 먼저 검토하고 custom layout은 명시적 이유가 있을 때 둔다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 표준 adaptive scaffold 를 먼저 검토하고 custom layout 은 명시적 이유가 있을 때 둔다

Material 3 Adaptive library 는 navigation suite, list-detail, supporting pane 같은 표준 scaffold 를 제공한다. 이들은 window size class 와 posture 에 맞춰 흔한 adaptive UI 문제를 이미 모델링한다.

Custom layout 은 표준 scaffold 가 표현하지 못하는 product-specific structure 가 있을 때 선택한다. 표준 component 와 같은 상태를 중복 소유하거나, window 변화마다 별도 route tree 를 만들어야 한다면 custom layout 의 비용을 다시 검토한다.

### 판단 기준

- top-level chrome 문제는 navigation suite scaffold 로 먼저 검토한다.
- list-detail/supporting pane 문제는 canonical layout 과 adaptive scaffold 로 먼저 검토한다.
- custom layout 은 상태 소유자, back policy, resize behavior 를 문서화할 수 있을 때만 둔다.
- custom layout 이 표준 scaffold 와 같은 상태를 중복 관리하면 버그 비용이 커진다.

### 예시

top-level chrome 은 custom `Row`/`Column` 분기 대신 `material3-adaptive-navigation-suite` 의존성을 추가하고 `NavigationSuiteScaffold` 로 먼저 시도한다.

```kotlin
NavigationSuiteScaffold(
    navigationSuiteItems = {
        destinations.forEach { dest ->
            item(
                icon = { Icon(dest.icon, contentDescription = null) },
                selected = dest == current,
                onClick = { current = dest },
            )
        }
    }
) { DestinationContent(current) }
```

이 컴포넌트는 `windowSizeClass` 에 따라 compact 에서 bottom navigation bar, expanded 에서 navigation rail 로 자동 전환한다. 같은 동작을 custom `if (isExpanded)` 분기로 재구현하면 두 코드 경로가 각자 버그를 갖게 된다.

관련 노트: [Top-level destination은 adaptive navigation chrome의 단위다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/top-level-destination-owns-adaptive-navigation-chrome.md)

공식 문서: [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation), [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)
