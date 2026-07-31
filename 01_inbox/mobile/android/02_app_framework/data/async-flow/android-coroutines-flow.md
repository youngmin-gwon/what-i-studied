# Android Coroutines and Flow

Android Coroutine/Flow 문서는 비동기 작업의 수명, 실행 위치, 실패 전파, stream sharing, UI state 수집을 분리해서 읽는다.

## 정본 지도

- [Coroutine Contracts](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/coroutine-contracts.md) - scope, dispatcher, exception/supervision.
- [Flow Contracts](01_inbox/mobile/android/02_app_framework/data/async-flow/flow/flow-contracts.md) - callbackFlow, shareIn, Flow/StateFlow 상태 계약.
- [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md) - repository stream과 screen state.
- [Coroutine/Flow 테스트 계약](01_inbox/mobile/android/06_testing_performance/testing/coroutine-flow-tests-control-dispatchers-and-virtual-time.md) - dispatcher와 virtual time 제어.

## 읽는 기준

작업이 언제 취소되어야 하는지 묻는다면 scope와 structured concurrency를 본다. 어느 thread에서 실행할지 묻는다면 dispatcher를 본다. 실패가 어디까지 전파되는지 묻는다면 supervision boundary를 본다. callback API를 stream으로 바꾼다면 callbackFlow를 본다. 같은 upstream을 여러 collector가 공유한다면 shareIn/stateIn을 구분한다.

관련 지도: [Android Data Layer Map](01_inbox/mobile/android/02_app_framework/data/android-data-layer-map.md), [Android State Management](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md).
