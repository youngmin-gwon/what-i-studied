---
title: modifier-order-changes-layout-draw-and-input-wrappers
tags: [android, compose/ui, jetpack-compose]
aliases: [Modifier order]
date modified: 2026-08-03 18:10:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Modifier order changes layout draw and input wrappers

Modifier chain 은 같은 속성 목록의 순서 없는 집합이 아니다. 각 modifier element 는 layout, drawing, input, semantics 같은 wrapper 를 만들 수 있고, 체인 순서가 제약 전달과 시각 결과를 바꾼다.

Layout 에 관여하는 modifier 는 바깥쪽에서 안쪽으로 constraints 를 전달하고, 안쪽에서 바깥쪽으로 측정 결과를 보고한다. Drawing modifier 나 clickable/clip/padding 도 순서에 따라 터치 영역과 clipping 결과가 달라질 수 있다.

따라서 `padding().clickable()` 과 `clickable().padding()` 은 같은 의미가 아니다. modifier 순서는 "읽기 좋은 스타일"이 아니라 UI 계약의 일부다.

관련 노트: [Size modifier는 incoming constraint 안에서 요청 크기를 해석한다](./size-modifiers-interpret-requested-size-inside-incoming-constraints.md), [Semantics Tree는 UI 의미를 접근성 서비스와 테스트에 드러낸다](./semantics-tree-makes-ui-meaning-visible-to-accessibility-and-tests.md)

출처: [Constraints and modifier order](https://developer.android.com/develop/ui/compose/layouts/constraints-modifiers), [Compose modifiers](https://developer.android.com/develop/ui/compose/modifiers)
