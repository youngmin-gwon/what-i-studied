# Kotlin Coroutine Flow와 StateFlow

이 문서는 Coroutine/Flow 계열 노트의 진입점이다. 화면 상태와 연결되는 Flow/StateFlow 내용은 정본 노트로 흡수했다.

## 상태 계약 정본

- [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)
- [Repository는 데이터 흐름을 Flow로 제공하고 ViewModel은 화면 상태로 조합한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/repository-exposes-flow-and-viewmodel-composes-screen-state.md)
- [StateFlow는 현재값이 필요한 화면 상태에 사용하고 Flow는 원천 데이터 흐름에 사용한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/stateflow-is-for-current-screen-state-flow-is-for-source-stream.md)
- [SharedFlow와 Channel은 상태 저장소가 아니라 일회성 신호 전달 수단이다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/sharedflow-and-channel-are-event-signals-not-state-stores.md)
- [Flow를 StateFlow로 바꿀 때는 stateIn의 수명과 공유 정책을 명시한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/statein-requires-explicit-lifetime-and-sharing-policy.md)

## Coroutine 기초

- [Coroutine은 가벼운 비동기 작업 단위다](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/coroutine-as-lightweight-async-work.md)
- [Flow는 비동기 스트림이다](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/flow-as-async-stream.md)
- [구조적 동시성은 부모가 자식 작업의 수명을 소유한다](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/structured-concurrency-parent-owns-children.md)
