# Kotlin Coroutine & Flow/StateFlow 완전 가이드

이 문서는 현대 Android 개발에서 거의 모든 비동기 처리의 기반이 되는 **Kotlin Coroutine**, **Flow**, **StateFlow**를 바닥부터
설명합니다. "이게 뭔데?", "실제로는 어디에 쓰는데?", "어떤 패턴으로 설계해야 하는데?"라는 질문에 답하는 것을 목표로 합니다.

---

## 원자 노트

- [왜 Coroutine, Flow, StateFlow가 필요해졌나?](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/why-coroutine-flow-stateflow.md)
- [Coroutine: 가벼운 비동기 작업 단위](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/coroutine-as-lightweight-async-work.md)
- [Structured Concurrency: 부모가 자식을 책임지는 패턴](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/structured-concurrency-parent-owns-children.md)
- [Flow: 시간이 지나며 여러 값을 내보내는 비동기 스트림](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/flow-as-async-stream.md)
- [StateFlow: 현재 상태를 들고 있는 Flow](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/stateflow-as-current-state-flow.md)
- [SharedFlow와 Channel: 상태가 아니라 이벤트를 다루는 도구](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/sharedflow-channel-for-events.md)
- [Android에서 자주 쓰는 실전 패턴](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/android-coroutine-flow-practical-patterns.md)
- [자주 하는 실수](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/kotlin-coroutine-flow-common-mistakes.md)
- [선택 기준 요약](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/kotlin-coroutine-flow-selection-guide.md)
- [전체 그림](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/kotlin-coroutine-flow-overall-map.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, 각 H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
