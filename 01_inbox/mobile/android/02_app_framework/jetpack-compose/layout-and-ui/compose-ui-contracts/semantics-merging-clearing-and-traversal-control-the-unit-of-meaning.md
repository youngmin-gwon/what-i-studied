---
title: Semantics merging clearing and traversal control the unit of meaning
tags: [android, jetpack-compose, compose/ui]
aliases: [mergeDescendants, clearAndSetSemantics, traversalIndex]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

`mergeDescendants`는 여러 child semantics를 하나의 의미 단위로 합쳐 카드나 row를 한 항목처럼 읽게 만든다. 반대로 너무 많이 병합하면 사용자가 필요한 세부 action에 접근하지 못할 수 있다.

`clearAndSetSemantics`는 기존 semantics를 지우고 새 의미로 대체할 때 쓰며, 장식 요소를 접근성 서비스에서만 숨기는 `hideFromAccessibility`와 다르다. 두 API는 목적이 다르므로 “숨기기”로 뭉개면 안 된다.

비정상적인 시각 배치나 복잡한 pane에서는 traversal group과 index로 읽기 순서를 조정할 수 있다. 실제 TalkBack과 device에서 읽기 순서를 확인해야 한다.

관련 노트: [Semantics Tree는 UI 의미를 접근성 서비스와 테스트에 드러낸다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/semantics-tree-makes-ui-meaning-visible-to-accessibility-and-tests.md), [시각 정보와 제스처에는 읽을 수 있는 의미와 대체 동작이 필요하다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/visual-information-and-gestures-need-readable-meaning-and-alternate-actions.md)

출처: [Merging and clearing semantics](https://developer.android.com/develop/ui/compose/accessibility/merging-clearing), [Traversal order](https://developer.android.com/develop/ui/compose/accessibility/traversal)
