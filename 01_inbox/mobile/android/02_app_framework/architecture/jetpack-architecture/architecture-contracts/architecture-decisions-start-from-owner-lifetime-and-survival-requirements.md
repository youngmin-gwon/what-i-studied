---
title: architecture-decisions-start-from-owner-lifetime-and-survival-requirements
tags: [android, android/architecture, android/jetpack]
aliases: ["아키텍처 결정은 owner, lifetime, survival 요구에서 시작한다"]
date modified: 2026-08-04 13:30:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 아키텍처 결정은 owner, lifetime, survival 요구에서 시작한다

Android 에서 "어디에 둘까"는 대부분 lifetime 질문이다. 누가 값을 읽고 쓰는가, 화면을 잃어도 살아야 하는가, process death 이후 복구해야 하는가, 다른 앱이나 시스템이 호출할 수 있는가, 테스트에서 대체되어야 하는가를 먼저 답해야 한다.

UI-only state 는 Composition 이나 UI controller 가 소유할 수 있고, screen state 는 ViewModel 이, durable app data 는 repository/storage 가, deferrable guaranteed work 는 WorkManager 가, external entry point 는 Manifest component 가 owner 가 된다.

이 기준을 통과하지 않은 layer 추가는 구조를 좋아 보이게 만들 뿐이다. 예외를 둘 때도 "왜 이 owner 와 lifetime 이 맞는지"를 노트나 코드 경계에 남기는 것이 좋다.

이 판단을 잘못하면 관찰 가능한 증상으로 드러난다. 예를 들어 UI-only state 를 ViewModel 대신 Composition 에만 두면 화면 회전 시 값이 사라지고, screen state 를 ViewModel 대신 Composable 지역 상태로 두면 같은 문제가 재현된다. `adb shell am kill <pkg>` 로 process death 를 강제 재현했을 때 값이 복구되지 않으면, saved state 나 durable storage 가 아니라 in-memory owner 에만 값을 뒀다는 신호다.

관련 노트: [state-management 정본](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md), [프로세스 종료 복구](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/process-death-recovery-needs-saved-state-and-persistent-source-of-truth.md), [background work 정본](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md).

공식 문서: [Recommendations for Android architecture](https://developer.android.com/topic/architecture/recommendations)
