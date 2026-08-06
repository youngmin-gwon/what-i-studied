---
title: compose-runtime-and-state-model
tags: [android, compose/runtime, jetpack-compose]
aliases: [Compose mental model, Compose Runtime]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Compose runtime and state model
배경 지식: [메모리 레이아웃 및 캐시](../../../../../../02_references/computer-science/memory-layout-and-cache.md)

Compose Runtime은 Composable을 개별 UI 뷰 객체로 다루지 않고, 상태(State) 변화에 따라 UI 트리 구조를 선언적으로 생성 및 갱신하는 함수 실행 런타임 엔진이다. 이 문서는 Compose Runtime의 코어 작동 원리(Slot Table, Compiler 코드 변환, Snapshot State 관찰, 3-Phase 파이프라인)를 체계적으로 바인딩하는 정본 안내서다.

정본 묶음: [Compose runtime contracts](./compose-runtime-contracts/compose-runtime-contracts.md)

---

### 핵심 동작 메커니즘 요약 (What / Why / How)

1. **선언적 상태 모델 ($UI = f(State)$)**
   - **What**: UI를 직접 변경(`textView.text = ...`)하지 않고, 현재 앱 상태를 인수로 받아 UI 구조를 묘사하는 함수식 모델이다.
   - **Why**: 상태 변화와 UI 갱신 간의 상태 불일치(State-UI Desynchronization) 버그를 구조적으로 방지한다.
   - **How**: Compose Compiler가 `@Composable` 함수에 `$composer` 객체를 주입하여 실행 결과를 Slot Table에 기록하고, 상태 변경 시 무효화된 Scope만 선별 재실행([recomposition](recomposition.md))한다.

2. **Snapshot 기반 자동 상태 관찰 시스템**
   - **What**: 개발자가 리스너나 `setState()`를 명시하지 않아도, Composition 단계에서 읽어들인 State 객체를 런타임이 자동으로 추적하는 메커니즘이다.
   - **Why**: 수동 구독 관리의 번거로움과 누수(Memory Leak)를 완전히 차단하고 최소 범위 Recomposition을 보장한다.
   - **How**: `Snapshot.takeMutableSnapshot()` 기반 트랜잭션 관찰기(Read Observer)가 State 획득 시 해당 `RecomposeScope`를 스냅샷 의존성 맵에 래핑·등록한다.

3. **Positional Memoization과 Slot Table (Gap Buffer)**
   - **What**: 호출 위치(Callsite)의 소스 코드 구조적 위치 정보와 Key를 조합하여 `remember` 값과 노드 트리를 유지하는 인메모리 저장소다.
   - **Why**: 잦은 UI 재구성에도 매번 메모리를 재할당하지 않고 이전 연산 결과와 UI 노드를 효율적으로 재사용한다.
   - **How**: 선형 배열 구조의 Gap Buffer를 기반으로 `$composer.startReplaceableGroup(key)`를 통해 슬롯 커서를 이동시키며 개별 데이터를 읽고 쓴다.

---

### 정본 계약 읽는 순서

- [Compose UI는 상태를 입력으로 계산되는 선언적 결과다](./compose-runtime-contracts/compose-ui-is-declarative-function-of-state.md)
- [Recomposition은 전체 UI redraw가 아니라 필요한 Composable scope 재실행이다](./compose-runtime-contracts/recomposition-scope-control.md)
- [Composable body는 빠르고 idempotent하며 side-effect free 해야 한다](./compose-runtime-contracts/composable-body-purity.md)
- [Snapshot State 관찰은 State를 읽은 scope를 invalidation 대상으로 만든다](./compose-runtime-contracts/snapshot-state-observation-invalidates-state-read-scopes.md)
- [remember는 일반 cache가 아니라 Composition에 귀속된 저장공간이다](./compose-runtime-contracts/remember-is-composition-scoped-storage-not-general-cache.md)
- [Composition은 호출 위치 identity로 remember 값을 보존한다](./compose-runtime-contracts/composition-uses-callsite-identity-to-preserve-remembered-values.md)
- [@Composable 컴파일 결과는 restart와 skip 제어를 가능하게 한다](./compose-runtime-contracts/composable-compiler-restart-skip.md)
- [Compose frame pipeline은 composition, layout, drawing으로 나뉜다](./compose-runtime-contracts/compose-frame-pipeline-is-split-into-composition-layout-and-drawing.md)
- [Compose state owner는 읽고 쓰는 범위의 가장 낮은 공통 owner다](./compose-runtime-contracts/compose-state-owner-is-the-lowest-common-owner-that-needs-read-or-write.md)
- [Automatic State Observation이 Flutter rebuild 사고와 Compose를 가른다](./compose-runtime-contracts/automatic-state-observation-is-the-compose-flutter-rebuild-difference.md)
- [Compose Runtime은 state, effect, performance, tooling 정본으로 이어지는 중심 모델이다](./compose-runtime-contracts/compose-runtime-links-state-effects-performance-and-tooling.md)

---

### 범위 및 연관 정본 묶음

이 묶음은 Compose Runtime 멘탈 모델의 정본이다.
- API 바인딩과 상태/이펙트 수명주기는 [Compose 상태와 Effect 계약](../state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)에서 다룬다.
- Recomposition 건너뛰기 최적화 및 Stability 판단은 [Compose 성능 계약](../performance/compose-performance-contracts/compose-performance-contracts.md)으로 보낸다.
- Layout 측정/배치, Animation, Semantics는 [Compose UI 계약](../layout-and-ui/compose-ui-contracts/compose-ui-contracts.md)에서 다룬다.

---

### Subsystem Contract Maps
- [ui-system-contracts](../../ui/system/ui-system-contracts/ui-system-contracts.md)
- [compose-ui-contracts](../layout-and-ui/compose-ui-contracts/compose-ui-contracts.md)
- [compose-design-system-contracts](../design-system-and-architecture/compose-design-system-contracts/compose-design-system-contracts.md)
- [navigation3-contracts](../../navigation/navigation3/navigation3-contracts/navigation3-contracts.md)
- [navigation-contracts](../../navigation/navigation-contracts/navigation-contracts.md)
- [intent-manifest-contracts](../../navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md)
- [deep-link-contracts](../../navigation/intents-and-deep-links/deep-link-contracts/deep-link-contracts.md)
- [adaptive-navigation-contracts](../../navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-contracts.md)
- [context-contracts](../../architecture/context-and-modularity/context-contracts/context-contracts.md)
- [architecture-contracts](../../architecture/jetpack-architecture/architecture-contracts/architecture-contracts.md)
- [app-component-contracts](../../architecture/app-components/app-component-contracts/app-component-contracts.md)
- [file-access-contracts](../../data/storage/file-access-contracts/file-access-contracts.md)
- [persistence-contracts](../../data/storage/persistence-contracts/persistence-contracts.md)
- [flow-state-contracts](../../data/async-flow/flow-state-contracts/flow-state-contracts.md)
- [coroutine-contracts](../../data/async-flow/coroutines/coroutine-contracts.md)
- [flow-contracts](../../data/async-flow/flow/flow-contracts.md)
- [paging-contracts](../../data/paging/paging-contracts/paging-contracts.md)
- [di-contracts](../../dependency-injection/di-contracts/di-contracts.md)
- **dsl-syntax-does-not-change-ownership-lifetime-contracts**
- **modular-di-follows-module-dependency-direction-and-feature-entry-contracts**
