---
title: semantics-tree-makes-ui-meaning-visible-to-accessibility-and-tests
tags: [android, compose/ui, jetpack-compose]
aliases: [Accessibility, Semantics]
date modified: 2026-08-06 14:45:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Semantics 트리는 UI 의미를 접근성 서비스와 테스트에 드러낸다

내부 동작에서 Composition tree가 무엇을 그릴지 나타낸다면 Semantics tree는 노드의 역할·상태·설명·action을 나타낸다. `Text`, `Button`, `Switch`와 foundation modifier는 많은 정보를 자동 제공하지만, 직접 그린 custom control은 의미를 직접 구성해야 한다.

```kotlin
@Composable
fun SoundToggle(
    checked: Boolean,
    onCheckedChange: (Boolean) -> Unit,
) {
    Box(
        Modifier
            .testTag("sound_toggle")
            .toggleable(
                value = checked,
                role = Role.Switch,
                onValueChange = onCheckedChange,
            )
            .semantics {
                stateDescription = if (checked) "소리 켜짐" else "소리 꺼짐"
            },
    ) {
        Canvas(Modifier.size(48.dp)) { /* custom pixels */ }
    }
}
```

`toggleable`이 toggle action, checked state, role을 만든다. 같은 정보를 `semantics` 블록에서 다시 수동 작성하면 값이 어긋날 수 있으므로, 예제는 사용자에게 필요한 상태 문장만 보충한다.

```kotlin
@Test
fun custom_toggle_exposes_state_and_action() {
    rule.onNodeWithTag("sound_toggle")
        .assertIsOff()
        .performClick()
        .assertIsOn()
}
```

Compose test는 기본적으로 merged tree를 조회한다. 예상 노드를 찾지 못하면 곧바로 `useUnmergedTree = true`를 고정하기 전에 `printToLog()`와 Layout Inspector에서 병합 원인을 확인한다. 접근성 서비스도 unmerged tree를 바탕으로 자체 병합하므로 테스트 결과와 TalkBack 발화가 항상 일치한다고 가정하지 않는다.

장식 이미지는 `contentDescription = null`로 두고, 의미 있는 이미지는 주변 문맥과 중복되지 않는 설명을 제공한다. 관찰 증거는 semantics assertion, merged/unmerged tree 로그, TalkBack의 실제 발화 세 가지다.

관련 노트: [Semantics 병합·재정의·탐색 순서는 의미 단위를 조절한다](./semantics-merging-clearing-and-traversal-control-the-unit-of-meaning.md), [Testing quality contracts](../../../../06_testing_performance/testing/testing-quality/testing-quality.md)

출처: [Compose Semantics](https://developer.android.com/develop/ui/compose/accessibility/semantics)
