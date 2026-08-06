---
title: [viewmodel](../../../viewmodel.md)
tags: [android, android/architecture, android/state-management, android/viewmodel]
aliases: ["Android ViewModel"]
date modified: 2026-08-03 17:28:02 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## ViewModel 은 화면 상태와 외부 작업의 조율자다

ViewModel 은 화면 단위 상태와 외부 작업의 조율자다. 화면 객체를 보관하는 곳도, 프로세스 사망 복원 장치도, 영속 저장소도 아니다.

### 정본 노트

- [ViewModel은 화면 단위 상태와 외부 작업을 조율한다](./viewmodel-orchestrates-screen-state-and-external-work.md)
- [ViewModel은 UI 컨트롤러와 Android Context를 장기 보관하지 않는다](./viewmodel-does-not-retain-ui-controller-or-context.md)
- [ViewModel은 설정 변경 동안 유지되지만 프로세스 사망 복원은 보장하지 않는다](./viewmodel-survives-configuration-change-not-process-death.md)
- [SavedStateHandle은 프로세스 사망 후 복원해야 하는 작은 상태에 사용한다](./savedstatehandle-restores-small-process-death-state.md)
- [ViewModel은 외부 작업을 viewModelScope의 수명에 묶는다](./viewmodelscope-binds-external-work-to-viewmodel-lifetime.md)
- [ViewModel은 mutable 상태를 내부에 숨기고 읽기 전용 상태만 노출한다](./viewmodel-exposes-read-only-state.md)

상위 지도: [Android 상태 관리 정본 지도](../android-state-management.md)
