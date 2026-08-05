---
title: compose-runtime-contracts
tags: [android, compose/runtime, jetpack-compose]
aliases: [Compose runtime contracts]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Compose Runtime 계약은 상태 소유권과 리컴포지션을 다룬다
배경 지식: [메모리 레이아웃 및 캐시](../../../../../../../02_references/computer-science/memory-layout-and-cache.md)

- [Compose UI is a declarative function of state](./compose-ui-is-declarative-function-of-state.md)
- [**Recomposition**(상태 변경 시 영향을 받는 Composable 스코프만 선택적으로 재실행하여 UI 트리를 갱신하는 과정) reruns needed Composable scopes not the whole UI](./recomposition-reruns-needed-composable-scopes-not-the-whole-ui.md)
- [Composable body must be fast, idempotent, and side-effect-free](./composable-body-must-be-fast-idempotent-and-side-effect-free.md)
- [**Snapshot**(상태 읽기/쓰기 변경을 트랜잭션 단위로 추적하여 영향받는 스코프에 무효화 알림을 보내는 상태 관찰 시스템) State observation invalidates state read scopes](./snapshot-state-observation-invalidates-state-read-scopes.md)
- [remember is Composition-scoped storage, not a general cache](./remember-is-composition-scoped-storage-not-general-cache.md)
- [Composition uses callsite identity to preserve remembered values](./composition-uses-callsite-identity-to-preserve-remembered-values.md)
- [Composable compiler output enables restart and skip control](./composable-compiler-output-enables-restart-and-skip-control.md)
- [Compose frame pipeline is split into composition, layout, and drawing](./compose-frame-pipeline-is-split-into-composition-layout-and-drawing.md)
- [Compose state owner is the lowest common owner that needs read or write](./compose-state-owner-is-the-lowest-common-owner-that-needs-read-or-write.md)
- [Automatic State Observation is the Compose Flutter rebuild difference](./automatic-state-observation-is-the-compose-flutter-rebuild-difference.md)
- [Compose runtime links state, effects, performance, and tooling](./compose-runtime-links-state-effects-performance-and-tooling.md)
