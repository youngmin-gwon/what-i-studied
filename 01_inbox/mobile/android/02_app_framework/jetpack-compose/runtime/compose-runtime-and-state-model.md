---
title: Compose runtime and state model
tags: [android, jetpack-compose, compose/runtime]
aliases: [Compose Runtime, Compose mental model]
date modified: 2026-07-31 23:59:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

Compose Runtime은 Composable을 UI 객체로 보지 않고, state를 읽고 UI 설명을 만드는 함수 호출로 다룬다. 이 지도는 기존 Compose internals, Flutter 비교, compiler/slot table, phases 문서를 runtime 계약 단위로 다시 묶는다.

정본 묶음: [Compose runtime contracts](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-runtime-contracts.md)

## 읽는 순서

- [Compose UI는 상태를 입력으로 계산되는 선언적 결과다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-ui-is-declarative-function-of-state.md)
- [Recomposition은 전체 UI redraw가 아니라 필요한 Composable scope 재실행이다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/recomposition-reruns-needed-composable-scopes-not-the-whole-ui.md)
- [Composable body는 빠르고 idempotent하며 side-effect free 해야 한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composable-body-must-be-fast-idempotent-and-side-effect-free.md)
- [Snapshot State 관찰은 State를 읽은 scope를 invalidation 대상으로 만든다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/snapshot-state-observation-invalidates-state-read-scopes.md)
- [remember는 일반 cache가 아니라 Composition에 귀속된 저장공간이다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/remember-is-composition-scoped-storage-not-general-cache.md)
- [Composition은 호출 위치 identity로 remember 값을 보존한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composition-uses-callsite-identity-to-preserve-remembered-values.md)
- [@Composable 컴파일 결과는 restart와 skip 제어를 가능하게 한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composable-compiler-output-enables-restart-and-skip-control.md)
- [Compose frame pipeline은 composition, layout, drawing으로 나뉜다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-frame-pipeline-is-split-into-composition-layout-and-drawing.md)
- [Compose state owner는 읽고 쓰는 범위의 가장 낮은 공통 owner다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-state-owner-is-the-lowest-common-owner-that-needs-read-or-write.md)
- [Automatic State Observation이 Flutter rebuild 사고와 Compose를 가른다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/automatic-state-observation-is-the-compose-flutter-rebuild-difference.md)
- [Compose Runtime은 state, effect, performance, tooling 정본으로 이어지는 중심 모델이다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-runtime-links-state-effects-performance-and-tooling.md)

## 범위

이 묶음은 Runtime mental model의 정본이다. API 선택은 [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)으로, recomposition 비용과 stability 판단은 [Compose 성능 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-performance-contracts.md)으로 보낸다. Layout, animation, accessibility, Material, Glance는 다음 Compose UI 패스에서 별도로 정리한다.
