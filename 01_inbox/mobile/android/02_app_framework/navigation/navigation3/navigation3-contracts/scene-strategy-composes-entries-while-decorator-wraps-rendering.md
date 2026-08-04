---
title: scene-strategy-composes-entries-while-decorator-wraps-rendering
tags: [android, android/navigation, android/navigation3]
aliases: ["SceneStrategy는 entry를 조합하고 SceneDecorator는 렌더링을 감싼다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## SceneStrategy 는 entry 를 조합하고 SceneDecorator 는 렌더링을 감싼다

Navigation 3 에서 SceneStrategy 는 back stack 의 어떤 entry 들을 어떤 scene 으로 보여줄지 결정하는 확장 지점이다. Adaptive layout 이나 multi-pane 표시처럼 여러 entry 를 함께 읽는 정책은 strategy 쪽 책임이다.

SceneDecorator 나 entry decorator 는 이미 선택된 entry/scene 의 rendering 주변에 saveable state, ViewModel store, transition 같은 횡단 관심사를 더하는 지점이다. 표시할 entry 를 고르는 정책과 렌더링을 감싸는 정책을 섞지 않는다.

### 판단 기준

- 여러 entry 를 하나의 visual scene 으로 묶는 문제는 SceneStrategy 에서 해결한다.
- entry 별 saveable state, ViewModel store, transition wrapper 는 decorator 에서 해결한다.
- scene 선택 정책이 feature content 내부로 새면 route registry 와 layout policy 가 결합된다.
- adaptive scaffold 와 함께 쓸 때는 pane 상태와 scene 상태의 소유자를 하나로 정한다.

### 예시

```kotlin
NavDisplay(
    backStack = backStack,
    entryDecorators = listOf(
        rememberSaveableStateHolderNavEntryDecorator(),
        rememberViewModelStoreNavEntryDecorator(),
    ),
    sceneStrategy = rememberListDetailSceneStrategy(),
    entryProvider = entryProvider,
)
```

`sceneStrategy` 는 back stack 의 어떤 entry 들을 list pane 과 detail pane 으로 묶을지 결정하고, `entryDecorators` 는 그렇게 골라진 entry 각각의 saveable state 와 ViewModel store 를 감싼다. 두 책임을 같은 컴포저블 안에 합치면 pane 조합을 바꿀 때마다 상태 보존 코드도 함께 손대야 한다.

관련 노트: [Metadata와 SceneStrategy는 표시 정책을 전달한다](./metadata-and-scene-strategy-carry-display-policy.md), [Navigation 3 Scene과 adaptive scaffold는 서로 다른 레이아웃 문제를 푼다](../../adaptive-navigation/adaptive-navigation-contracts/navigation3-scenes-and-adaptive-scaffolds-solve-different-layout-problems.md)
