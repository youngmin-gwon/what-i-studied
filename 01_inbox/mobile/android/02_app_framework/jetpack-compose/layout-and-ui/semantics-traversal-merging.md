---
title: semantics-traversal-merging
tags: [android, compose/ui, jetpack-compose]
aliases: [clearAndSetSemantics, mergeDescendants, traversalIndex]
date modified: 2026-08-06 14:45:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Semantics 병합·재정의·탐색 순서는 의미 단위를 조절한다

병합 메커니즘에서 `mergeDescendants`는 여러 자식의 정보를 한 노드로 모은다. `clickable`과 `toggleable` 같은 modifier 및 일부 Material 컴포넌트도 자식을 자동 병합한다. 자식마다 독립 action이 필요하면 병합하면 안 된다.

```kotlin
@Composable
fun AccountSummary(name: String, balance: String, onOpen: () -> Unit) {
    Row(
        Modifier
            .semantics(mergeDescendants = true) {}
            .clickable(onClickLabel = "계좌 상세 보기", onClick = onOpen)
            .testTag("account_summary"),
    ) {
        Text(name)
        Text(balance)
    }
}
```

`clearAndSetSemantics`는 현재 노드와 자손의 기존 semantics를 지우고 새 의미로 대체한다. 빈 블록이면 접근성·autofill·테스트를 포함한 모든 semantics 소비자에게 정보가 전달되지 않는다. 접근성 서비스에서만 장식을 숨기는 `hideFromAccessibility()`와 범위가 다르다.

```kotlin
Row(
    Modifier
        .toggleable(value = enabled, role = Role.Switch, onValueChange = onChange)
        .clearAndSetSemantics {
            role = Role.Switch
            toggleableState = ToggleableState(enabled)
            stateDescription = if (enabled) "자동 백업 사용" else "자동 백업 사용 안 함"
            onClick(label = "자동 백업 전환") {
                onChange(!enabled)
                true
            }
        },
) { /* custom drawing */ }
```

시각 순서와 읽기 순서가 다를 때만 `isTraversalGroup`과 `traversalIndex`를 제한적으로 사용한다. index를 전체 화면에 남발하면 UI 재배치와 함께 순서가 쉽게 깨진다.

두 트리는 로그로 비교한다.

```kotlin
rule.onRoot().printToLog("MERGED")
rule.onRoot(useUnmergedTree = true).printToLog("UNMERGED")
```

테스트 프레임워크는 기본적으로 merged tree를 사용한다. 접근성 서비스는 unmerged tree를 바탕으로 자체 병합을 적용할 수 있으므로, 로그 차이를 확인한 뒤 TalkBack에서 최종 의미 단위와 action 수를 관찰한다.

관련 노트: [Semantics 트리는 UI 의미를 접근성 서비스와 테스트에 드러낸다](semantics-tree-accessibility.md), [시각 정보와 제스처에는 읽을 수 있는 의미와 대체 동작이 필요하다](accessibility-gestures-meaning.md)

출처: [Semantics 병합과 재정의](https://developer.android.com/develop/ui/compose/accessibility/merging-clearing), [접근성 탐색 순서](https://developer.android.com/develop/ui/compose/accessibility/traversal)
