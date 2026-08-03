---
title: flow-state-contracts
tags: [android, android/async, android/data, android/flow-state-contracts]
aliases: ["Flow와 StateFlow 상태 계약"]
date modified: 2026-08-03 18:07:38 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Flow 와 StateFlow 상태 계약

Flow 계열 노트는 데이터 흐름의 소유자와 화면 상태 계약을 구분한다. `Flow` 는 원천 데이터 흐름, `StateFlow` 는 현재값이 필요한 화면 상태에 주로 사용한다.

### 정본 노트

- [Repository는 데이터 흐름을 Flow로 제공하고 ViewModel은 화면 상태로 조합한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/repository-exposes-flow-and-viewmodel-composes-screen-state.md)
- [StateFlow는 현재값이 필요한 화면 상태에 사용하고 Flow는 원천 데이터 흐름에 사용한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/stateflow-is-for-current-screen-state-flow-is-for-source-stream.md)
- [SharedFlow와 Channel은 상태 저장소가 아니라 일회성 신호 전달 수단이다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/sharedflow-and-channel-are-event-signals-not-state-stores.md)
- [Flow를 StateFlow로 바꿀 때는 stateIn의 수명과 공유 정책을 명시한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/statein-requires-explicit-lifetime-and-sharing-policy.md)
- [새 입력이 이전 작업을 무효화하면 flatMapLatest로 이전 흐름을 취소한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flatmaplatest-cancels-obsolete-work-for-new-input.md)
- [여러 원천의 최신값으로 화면 상태를 만들 때 combine을 사용한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/combine-builds-screen-state-from-latest-source-values.md)
- [화면에 그릴 Flow는 lifecycle-aware API로 수집한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/collect-flow-for-ui-with-lifecycle-aware-api.md)

관련 지도: [Android 상태 관리 정본 지도](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md)
