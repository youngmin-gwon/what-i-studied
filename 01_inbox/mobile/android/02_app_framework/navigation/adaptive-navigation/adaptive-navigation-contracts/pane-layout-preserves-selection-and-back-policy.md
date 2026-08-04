---
title: pane-layout-preserves-selection-and-back-policy
tags: [android, android/adaptive, android/navigation]
aliases: ["Pane layout은 선택 상태와 back policy를 분리해 보존해야 한다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Pane layout 은 선택 상태와 back policy 를 분리해 보존해야 한다

List-detail 이나 supporting pane layout 에서는 보이는 pane 수와 선택된 content state 가 같은 것이 아니다. Expanded window 에서는 list 와 detail 을 동시에 보여줄 수 있지만 compact window 에서는 같은 선택 상태를 단일 pane navigation 으로 표현해야 한다.

따라서 pane visibility, selected item, detail route, back action 을 분리해서 설계한다. 창 크기가 바뀌어도 사용자가 선택한 대상과 back 의미가 바뀌지 않아야 한다.

### 판단 기준

- selected item 은 pane visibility 보다 오래 살아야 하는 screen state 로 둔다.
- compact 에서 detail 로 들어간 뒤 back 이 list 로 돌아오는지 검증한다.
- expanded 에서 list 와 detail 을 동시에 보여도 route stack 의미는 유지한다.
- back policy 와 pane transition 을 별도 boolean 으로 흩뜨리지 말고 상태 전이로 표현한다.

### 예시

`selectedItem` 은 pane 개수와 무관하게 살아남는 state 로 hoist 한다.

```kotlin
var selectedId by rememberSaveable { mutableStateOf<String?>(null) }

NavigableListDetailPaneScaffold(
    navigator = navigator,
    listPane = { ItemList(onSelect = { selectedId = it }) },
    detailPane = { selectedId?.let { ItemDetail(it) } },
)
```

compact 에서 detail 로 진입한 뒤 back 을 누르면 `navigator.navigateBack()` 이 list pane 으로 돌아가야 하고, `selectedId` 자체는 지워지지 않아야 expanded 로 회전했을 때 같은 항목이 선택된 채로 보인다.

관련 노트: [Navigation 3 Scene과 adaptive scaffold는 서로 다른 레이아웃 문제를 푼다](./navigation3-scenes-and-adaptive-scaffolds-solve-different-layout-problems.md)

공식 문서: [Build a list-detail layout](https://developer.android.com/develop/adaptive-apps/guides/list-detail)
