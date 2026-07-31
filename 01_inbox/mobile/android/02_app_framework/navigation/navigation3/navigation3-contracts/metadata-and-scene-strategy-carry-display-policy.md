---
title: "Metadata 와 SceneStrategy 는 표시 정책을 전달한다"
tags: [android, android/navigation, android/navigation3]
aliases: ["Metadata 와 SceneStrategy 는 표시 정책을 전달한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Metadata 와 SceneStrategy 는 표시 정책을 전달한다

상위 문서: [Navigation 3 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-contracts.md)

### metadata 의 의미

Navigation 3 의 metadata 는 route content 자체가 아니라 entry 를 배치하는 방법을 설명한다.

`NavEntry` 에서 `SceneStrategy` 와 decorator 로 전달되는 typed map 이라고 이해하면 된다.

```kotlin
entry<TrainingRoute>(
    metadata = ListDetailSceneStrategy.listPane(),
) {
    TrainingListScreen()
}
```

metadata 로 표현할 수 있는 정책은 다음과 같다.

- list pane, detail pane, supporting pane 같은 scene 역할
- dialog 나 overlay 로 표시할지 여부
- entry 별 transition override
- app chrome 을 표시하거나 숨길지 여부

metadata key 는 값을 읽는 컴포넌트 안에 둔다.

그러면 key 의 의미와 소비자가 함께 발견되고, 서로 관련 없는 전역 문자열 key 가 생기지 않는다.

```kotlin
object HideChromeKey : NavMetadataKey<Boolean>
```

### strategy 순서

`NavDisplay` 는 현재 entry 집합을 scene 으로 만들 수 있는 strategy 를 평가한다.

어떤 strategy 도 적용하지 못하면 마지막 entry 하나를 보여주는 single-pane 동작으로 돌아간다.

overlay 성격의 strategy 는 일반 multi-pane strategy 보다 먼저 평가하는 편이 안전하다.

dialog route 가 list-detail strategy 에 의해 일반 pane 으로 소비되는 일을 막을 수 있기 때문이다.

```kotlin
sceneStrategies = listOf(
    remember { DialogSceneStrategy<NavKey>() },
    rememberListDetailSceneStrategy(),
)
```

단순 push/pop 흐름에는 scene strategy 가 필요하지 않다.

list 와 detail 을 동시에 다루거나 supporting pane 이 실제 요구사항이 될 때만 도입한다.

strategy 는 window 상태에 따라 같은 back stack 을 다른 visual arrangement 로 바꾼다.

따라서 route key 를 화면 폭별로 다르게 만들 필요는 없다.

metadata 는 UI content 가 container 의 결정을 조작하는 통로가 아니다.

entry 가 자신의 의미를 선언하고 container 가 그 의미를 해석하는 계약이다.

지원되지 않는 metadata 는 조용히 무시되거나 기본 scene 으로 fallback 되어야 한다.

공식 scene 모델은 [Navigation 3 Scenes](https://developer.android.com/guide/navigation/navigation-3/scenes) 에서 확인할 수 있다.

### 공식 문서

- [Navigation 3 Scenes](https://developer.android.com/guide/navigation/navigation-3/scenes)
