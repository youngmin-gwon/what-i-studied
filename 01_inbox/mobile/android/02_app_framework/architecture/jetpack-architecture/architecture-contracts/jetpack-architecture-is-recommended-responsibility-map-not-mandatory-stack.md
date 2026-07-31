---
title: "Jetpack Architecture는 필수 stack이 아니라 책임 분리 지도다"
tags: [android, android/architecture, android/jetpack]
aliases: ["Jetpack Architecture는 필수 stack이 아니라 책임 분리 지도다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Jetpack Architecture는 필수 stack이 아니라 책임 분리 지도다

Android architecture guidance는 모든 앱이 같은 class 이름과 layer를 가져야 한다는 규칙이 아니다. 핵심은 관심사 분리, UI를 data에서 drive하기, single source of truth, 명확한 data flow 같은 책임 배치 원칙이다.

Jetpack은 라이브러리 묶음이고 architecture는 그 라이브러리를 어떤 owner, lifetime, boundary로 배치할지에 대한 설계다. ViewModel, Room, WorkManager, Navigation, Hilt를 썼다고 자동으로 좋은 구조가 되지는 않는다.

권장 구조는 앱 크기와 복잡도에 맞게 조정한다. domain layer는 중복이나 복잡한 business rule을 줄일 때 도입하고, repository도 framework 의무 클래스가 아니라 data boundary를 명확히 하는 패턴이다.

관련 노트: [UI/domain/data layer 경계](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/architecture-contracts/ui-domain-data-layers-separate-rendering-policy-and-source-of-truth.md), [state-management 정본](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md), [persistence 정본](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md).

공식 문서: [Guide to app architecture](https://developer.android.com/topic/architecture)
