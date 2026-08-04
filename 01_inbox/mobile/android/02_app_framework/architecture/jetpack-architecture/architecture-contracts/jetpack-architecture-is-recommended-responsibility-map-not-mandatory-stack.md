---
title: jetpack-architecture-is-recommended-responsibility-map-not-mandatory-stack
tags: [android, android/architecture, android/jetpack]
aliases: ["Jetpack Architecture는 필수 stack이 아니라 책임 분리 지도다"]
date modified: 2026-08-04 16:32:59 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Jetpack Architecture 는 필수 stack 이 아니라 책임 분리 지도다

Android architecture guidance 는 모든 앱이 같은 class 이름과 layer 를 가져야 한다는 규칙이 아니다. 핵심은 관심사 분리, UI 를 data 에서 drive 하기, single source of truth, 명확한 data flow 같은 책임 배치 원칙이다.

Jetpack 은 라이브러리 묶음이고 architecture 는 그 라이브러리를 어떤 owner, lifetime, boundary 로 배치할지에 대한 설계다. ViewModel, Room, WorkManager, Navigation, Hilt 를 썼다고 자동으로 좋은 구조가 되지는 않는다.

권장 구조는 앱 크기와 복잡도에 맞게 조정한다. domain layer 는 중복이나 복잡한 business rule 을 줄일 때 도입하고, repository 도 framework 의무 클래스가 아니라 data boundary 를 명확히 하는 패턴이다.

"ViewModel, Room, WorkManager 를 썼는데도 구조가 좋아지지 않았다"는 관찰 가능한 실패 패턴이 있다. 예를 들어 ViewModel 에 네트워크 호출과 SQL 쿼리가 직접 들어 있으면 클래스 이름은 Jetpack 이지만 책임 분리는 이뤄지지 않은 것이다 — 이 경우 ViewModel 단위 테스트가 repository/DB mocking 없이는 불가능해진다는 것이 그 증거다.

관련 노트: [UI/domain/data layer 경계](./ui-domain-data-layers-separate-rendering-policy-and-source-of-truth.md), [state-management 정본](../../state-management/android-state-management.md), [persistence 정본](../../../data/storage/persistence-contracts/persistence-contracts.md).

공식 문서: [Guide to app architecture](https://developer.android.com/topic/architecture)
