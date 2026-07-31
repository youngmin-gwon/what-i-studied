# Kotlin Coroutine & Flow/StateFlow 완전 가이드

이 문서는 현대 Android 개발에서 거의 모든 비동기 처리의 기반이 되는 **Kotlin Coroutine**, **Flow**, **StateFlow**를 바닥부터
설명합니다. "이게 뭔데?", "실제로는 어디에 쓰는데?", "어떤 패턴으로 설계해야 하는데?"라는 질문에 답하는 것을 목표로 합니다.

---

## 원자 노트

- [[why-coroutine-flow-stateflow|왜 Coroutine, Flow, StateFlow가 필요해졌나?]]
- [[coroutine-as-lightweight-async-work|Coroutine: 가벼운 비동기 작업 단위]]
- [[structured-concurrency-parent-owns-children|Structured Concurrency: 부모가 자식을 책임지는 패턴]]
- [[flow-as-async-stream|Flow: 시간이 지나며 여러 값을 내보내는 비동기 스트림]]
- [[stateflow-as-current-state-flow|StateFlow: 현재 상태를 들고 있는 Flow]]
- [[sharedflow-channel-for-events|SharedFlow와 Channel: 상태가 아니라 이벤트를 다루는 도구]]
- [[android-coroutine-flow-practical-patterns|Android에서 자주 쓰는 실전 패턴]]
- [[kotlin-coroutine-flow-common-mistakes|자주 하는 실수]]
- [[kotlin-coroutine-flow-selection-guide|선택 기준 요약]]
- [[kotlin-coroutine-flow-overall-map|전체 그림]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, 각 H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
