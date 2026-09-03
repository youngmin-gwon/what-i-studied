---
title: compose-runtime
tags: [android, compose/runtime, jetpack-compose]
aliases: [Compose runtime contracts]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Compose Runtime 계약은 상태 소유권과 리컴포지션을 다룬다
배경 지식: [메모리 레이아웃 및 캐시](../../../../../../02_references/computer-science/memory-layout-and-cache.md)

- [Compose UI는 상태를 입력으로 계산되는 선언적 결과다](compose-declarative-ui.md)
- [Recomposition은 전체 UI redraw가 아니라 필요한 Composable scope 재실행이다](recomposition-scope-control.md)
- [Composable body는 빠르고 idempotent하며 side-effect free 해야 한다](composable-body-purity.md)
- [Snapshot State 관찰은 State를 읽은 scope를 invalidation 대상으로 만든다](snapshot-state-observation.md)
- [remember는 일반 cache가 아니라 Composition에 귀속된 저장공간이다](remember-storage-semantics.md)
- [Composition은 호출 위치 identity로 remember 값을 보존한다](composition-callsite-identity.md)
- [@Composable 컴파일 결과는 restart와 skip 제어를 가능하게 한다](composable-compiler-restart-skip.md)
- [Compose frame pipeline은 composition, layout, drawing으로 나뉜다](compose-frame-pipeline.md)
- [Compose state owner는 읽고 쓰는 범위의 가장 낮은 공통 owner다](compose-state-ownership.md)
- [Automatic State Observation이 Flutter rebuild 사고와 Compose를 가른다](automatic-state-observation.md)
- [Compose Runtime은 state, effect, performance, tooling 정본으로 이어지는 중심 모델이다](compose-runtime-links.md)
