---
title: compose-state-read-location-controls-recomposition-scope
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Compose 상태 읽기 위치는 recomposition 범위를 결정한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](../../../../06_testing_performance/performance/android-performance-quality-and-build-optimization.md)

관련 지도: [Compose 성능 계약](./compose-performance-contracts.md)

관련 노트: [렌더링 성능은 프레임 지연의 원인을 분리한다](../../../../06_testing_performance/performance/performance-contracts/rendering-jank-is-frame-deadline-failure.md)

Compose Runtime 은 Snapshot State 를 읽은 composable 범위를 관찰한다.

상태를 너무 높은 곳에서 읽으면 작은 변경도 넓은 UI 를 다시 실행하게 만든다.

상태를 실제로 필요한 하위 composable 가까이에서 읽으면 변경 범위가 작아진다.

예를 들어 상위 Composable에서 `val count = counter.value` 로 읽어 여러 자식에게 파라미터로 넘기면 상위 scope 전체가 다시 실행되지만, `Text(text = "${counter.value}")` 처럼 실제로 값을 쓰는 자식 Composable 안에서 직접 읽으면 그 `Text` 노드만 다시 그려진다.

상태 객체를 전달해야 한다면 값 전체를 넘길지, 읽기 람다를 넘길지, 이벤트만 올릴지 구분한다.

스크롤 위치처럼 자주 변하는 값은 가능하면 layout 단계나 draw 단계에서 읽도록 지연할 수 있다.

다만 상태 읽기를 숨기기 위해 구조를 복잡하게 만들면 유지보수성이 떨어진다.

먼저 trace 와 recomposition 정보를 보고 실제 병목인지 확인한다.

공식 참고: [Defer reads as long as possible](https://developer.android.com/develop/ui/compose/performance/bestpractices#defer-reads)
