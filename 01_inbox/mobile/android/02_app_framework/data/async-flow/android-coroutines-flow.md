# Android Coroutines와 Flow

Android에서 Coroutine/Flow는 비동기 작업의 수명과 데이터 흐름을 표현하는 도구다. 화면 상태 계약과 직접 연결되는 내용은 별도 정본으로 분리했다.

## 정본

- [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)
- [화면에 그릴 Flow는 lifecycle-aware API로 수집한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/collect-flow-for-ui-with-lifecycle-aware-api.md)
- [Flow를 StateFlow로 바꿀 때는 stateIn의 수명과 공유 정책을 명시한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/statein-requires-explicit-lifetime-and-sharing-policy.md)
- [SharedFlow와 Channel은 상태 저장소가 아니라 일회성 신호 전달 수단이다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/sharedflow-and-channel-are-event-signals-not-state-stores.md)
