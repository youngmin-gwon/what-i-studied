---
title: flow-state
tags: [android, android/async, android/flow, android/state]
aliases: ["Flow와 StateFlow 상태 계약"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Flow와 StateFlow 상태 계약은 Repository 데이터 공급과 UI 화면 상태 유도를 연결한다

본 정본 클러스터는 Android 앱 아키텍처에서 **Repository 레이어의 Cold Flow 스트림**을 **ViewModel의 Hot StateFlow 화면 상태(UiState)**로 변환하고, **Compose / View UI 레이어에서 수명주기 안전(Lifecycle-aware)하게 수집**하기 위한 상태 관리 계약을 정의한다.

### 정본 노트

- [StateFlow는 화면의 현재 상태를 다루고 Flow는 데이터 저장소 스트림을 다룬다](stateflow-vs-flow.md) - StateFlow와 Flow의 역할 분담 및 conflation 특성.
- [Repository는 Flow를 노출하고 ViewModel은 화면 상태를 조합한다](../../architecture/state-management/viewmodel.md)-composes-screen-state.md) - 단방향 데이터 흐름(UDF)과 레이어별 캡슐화 규칙.
- [stateIn은 명시적 수명 scope와 sharing policy를 요구한다](flow-statein-policy.md) - WhileSubscribed(5000)를 활용한 백그라운드 리소스 방지.
- [SharedFlow와 Channel은 상태 저장소가 아니라 이벤트 신호다](sharedflow-and-channel-signals.md) - 1회성 UI 이벤트(Snackbar, Navigation)의 올바른 모델링과 Anti-pattern 피하기.
- [flatMapLatest는 새 입력이 오면 이전 입력을 취소한다](flow-flatmaplatest-search.md) - 검색어 입력 및 탭 전환 시의 구작업 자동 취소.
- [combine은 최신 소스 값으로 화면 상태를 만든다](flow-combine-screen-state.md) - 복수 데이터 소스를 합성하여 단일 UiState 생성.
- [UI는 lifecycle-aware API로 Flow를 수집해야 한다](lifecycle-aware-flow-collection.md) - repeatOnLifecycle 및 collectAsStateWithLifecycle을 통한 백그라운드 크래시/자원 누수 차단.
