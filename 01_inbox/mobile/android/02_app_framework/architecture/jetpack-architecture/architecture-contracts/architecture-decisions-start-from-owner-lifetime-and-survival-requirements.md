---
title: "아키텍처 결정은 owner, lifetime, survival 요구에서 시작한다"
tags: [android, android/architecture, android/jetpack]
aliases: ["아키텍처 결정은 owner, lifetime, survival 요구에서 시작한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 아키텍처 결정은 owner, lifetime, survival 요구에서 시작한다

Android에서 "어디에 둘까"는 대부분 lifetime 질문이다. 누가 값을 읽고 쓰는가, 화면을 잃어도 살아야 하는가, process death 이후 복구해야 하는가, 다른 앱이나 시스템이 호출할 수 있는가, 테스트에서 대체되어야 하는가를 먼저 답해야 한다.

UI-only state는 Composition이나 UI controller가 소유할 수 있고, screen state는 ViewModel이, durable app data는 repository/storage가, deferrable guaranteed work는 WorkManager가, external entry point는 Manifest component가 owner가 된다.

이 기준을 통과하지 않은 layer 추가는 구조를 좋아 보이게 만들 뿐이다. 예외를 둘 때도 "왜 이 owner와 lifetime이 맞는지"를 노트나 코드 경계에 남기는 것이 좋다.

관련 노트: [state-management 정본](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md), [프로세스 종료 복구](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/process-death-recovery-needs-saved-state-and-persistent-source-of-truth.md), [background work 정본](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md).

공식 문서: [Recommendations for Android architecture](https://developer.android.com/topic/architecture/recommendations)
