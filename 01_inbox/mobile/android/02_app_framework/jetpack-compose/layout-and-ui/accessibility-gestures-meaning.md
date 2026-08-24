---
title: accessibility-gestures-meaning
tags: [android, compose/ui, jetpack-compose]
aliases: [contentDescription, CustomAccessibilityAction]
date modified: 2026-08-06 14:45:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## 시각 정보와 제스처에는 읽을 수 있는 의미와 대체 동작이 필요하다

색·아이콘·위치만으로 전달한 정보는 보조 기술이 해석하지 못할 수 있다. 아이콘 버튼의 설명은 모양이 아니라 동작을 말하고, 장식 아이콘은 설명하지 않는다.

```kotlin
IconButton(onClick = onDelete) {
    Icon(
        Icons.Default.Delete,
        contentDescription = "항목 삭제",
    )
}
```

대체 동작 메커니즘으로 swipe나 drag처럼 발견하기 어려운 제스처에는 `CustomAccessibilityAction`이나 보이는 보조 control을 제공한다. 다음 row는 swipe 삭제와 같은 함수를 접근성 action menu에도 노출한다.

```kotlin
@Composable
fun MessageRow(message: Message, onDelete: (Message) -> Unit) {
    SwipeToDismissBox(
        state = rememberSwipeToDismissBoxState(),
        backgroundContent = { /* delete background */ },
        modifier = Modifier.semantics {
            customActions = listOf(
                CustomAccessibilityAction(label = "메시지 삭제") {
                    onDelete(message)
                    true
                },
            )
        },
    ) {
        Text(message.subject)
    }
}
```

동일 action을 가진 자식 버튼을 row 안에 유지하면 TalkBack 탐색 항목이 중복될 수 있다. action을 부모의 custom action으로 옮겼다면 원래 자식 semantics를 `clearAndSetSemantics {}`로 제거할지, 보이는 버튼을 독립 탐색 항목으로 유지할지 의도적으로 선택한다.

```kotlin
rule.onNodeWithText(message.subject)
    .assert(SemanticsMatcher.keyIsDefined(SemanticsActions.CustomActions))
    .performSemanticsAction(SemanticsActions.CustomActions) { actions ->
        check(actions.single { it.label == "메시지 삭제" }.action())
    }
```

테스트는 action 실행 뒤 실제 state가 바뀌는지도 assert한다. 실제 기기에서는 TalkBack action menu와 Switch Access로 제스처 없이 동작 가능한지 관찰한다. 최소 touch target과 큰 font scale도 별도로 검사한다.

관련 노트: [Semantics 트리는 UI 의미를 접근성 서비스와 테스트에 드러낸다](semantics-tree-accessibility.md), [접근성 품질은 서비스·검사기·Semantics 검증을 함께 요구한다](accessibility-service-verification.md)

출처: [Compose Semantics](https://developer.android.com/develop/ui/compose/accessibility/semantics), [Compose 접근성 기본 API](https://developer.android.com/develop/ui/compose/accessibility/api-defaults)
