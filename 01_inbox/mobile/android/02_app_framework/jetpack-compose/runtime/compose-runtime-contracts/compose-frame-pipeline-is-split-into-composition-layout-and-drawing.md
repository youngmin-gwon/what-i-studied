---
title: compose-frame-pipeline-is-split-into-composition-layout-and-drawing
tags: [android, compose/runtime, jetpack-compose]
aliases: [Compose phases]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Compose 프레임 파이프라인은 Composition, Layout, Drawing 단계로 분리된다

Compose 가 frame 을 만들 때의 큰 단계는 composition, layout, drawing 이다. Composition 은 무엇을 보여줄지 결정하고, layout 은 측정과 배치를 수행하며, drawing 은 화면에 그릴 내용을 만든다.

State read 는 phase 별로 추적될 수 있다. Composition 에서 읽은 state 가 바뀌면 Composable 재실행이 필요할 수 있고, layout/draw 에서 늦게 읽으면 그 phase 의 작업만 다시 할 여지가 생긴다.

`BoxWithConstraints`, lazy layout 처럼 layout 정보가 child composition 에 영향을 주는 예외가 있다. 따라서 phases 는 성능 판단을 위한 모델이지 모든 Composable 이 항상 같은 순서와 비용으로 동작한다는 보장은 아니다.

phase 를 늦추면 상위 recomposition 을 건너뛸 수 있다는 것은 코드로 바로 대비된다.

```kotlin
// composition phase 에서 읽음: offset 이 바뀔 때마다 이 Composable이 재구성된다
Box(Modifier.offset(x = offset.dp))

// drawing phase 에서 읽음: 재구성 없이 다시 그리기만 한다
Box(Modifier.graphicsLayer { translationX = offset })
```

두 코드는 최종 화면은 비슷해 보이지만, 위쪽은 매 프레임 composition 을 다시 타고 아래쪽은 draw 단계만 다시 실행한다. Layout Inspector 의 recomposition count 나 systrace 의 `Compose:composition`/`Compose:drawing` 구간을 비교하면 이 차이를 직접 관찰할 수 있다.

관련 노트: [Compose 상태 읽기 위치는 recomposition 범위를 결정한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-state-read-location-controls-recomposition-scope.md), [Compose layout과 image 비용은 프레임 예산 안에서 관리한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-layout-and-image-cost-must-be-budgeted.md)

출처: [Compose phases](https://developer.android.com/develop/ui/compose/phases)
