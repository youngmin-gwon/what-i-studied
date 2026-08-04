---
title: top-level-destination-owns-adaptive-navigation-chrome
tags: [android, android/adaptive, android/navigation]
aliases: ["Top-level destination은 adaptive navigation chrome의 단위다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Top-level destination 은 adaptive navigation chrome 의 단위다

Top-level destination 은 bottom bar, navigation rail, drawer 같은 app chrome 에 노출되는 가장 큰 이동 단위다. Adaptive UI 에서는 chrome 모양이 window 조건에 따라 바뀌어도 선택된 destination 의 의미는 그대로 유지되어야 한다.

Compact window 에서는 navigation bar 가 자연스럽고, expanded window 에서는 rail 이나 drawer 가 더 적합할 수 있다. 하지만 chrome 전환이 각 destination 의 back stack 을 초기화하거나 route 의미를 바꾸면 안 된다.

### 판단 기준

- top-level destination 은 feature root 또는 앱의 주요 업무 단위로 제한한다.
- window 변화는 chrome component 를 바꾸지만 selected destination 은 유지한다.
- 각 top-level destination 의 내부 stack 을 보존할지 초기화할지 명시한다.
- detail screen 을 무리하게 top-level destination 으로 올리지 않는다.

### 예시

각 top-level destination 의 `NavBackStack` 을 map 으로 따로 보관하면, chrome 이 bottom bar 에서 rail 로 바뀌어도 선택된 destination 과 그 내부 stack 은 유지된다.

```kotlin
val backStacks = remember {
    mutableStateMapOf<AppDestination, NavBackStack<NavKey>>()
}
var current by rememberSaveable { mutableStateOf(AppDestination.Home) }

val activeStack = backStacks.getOrPut(current) { mutableStateListOf(current.root) }
```

탭을 바꿀 때 `current` 만 갱신하고 `backStacks[previous]` 를 지우지 않으면, 사용자가 이전 탭으로 돌아왔을 때 detail 화면이 그대로 보인다.

관련 노트: [Navigation 3 back stack은 저장 가능한 navigation state로 복원해야 한다](../../navigation3/navigation3-contracts/navigation3-back-stack-needs-saveable-restoration.md)

공식 문서: [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation)
