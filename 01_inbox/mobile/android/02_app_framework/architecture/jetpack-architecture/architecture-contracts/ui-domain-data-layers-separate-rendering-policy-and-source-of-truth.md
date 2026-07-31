---
title: "UI, domain, data layer는 rendering, policy, source of truth를 분리한다"
tags: [android, android/architecture, android/jetpack]
aliases: ["UI, domain, data layer는 rendering, policy, source of truth를 분리한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# UI, domain, data layer는 rendering, policy, source of truth를 분리한다

UI layer는 상태를 그리고 사용자 action을 올린다. ViewModel/state holder는 화면 state와 외부 작업을 조율한다. Domain layer는 여러 화면이나 repository에 걸친 business rule이 실제 복잡도를 줄일 때만 둔다. Data layer는 repository와 data source를 통해 source of truth와 동기화 정책을 가진다.

이 구분은 package 이름보다 ownership이 중요하다. 화면이 사라져도 살아야 하는 데이터는 UI layer가 소유하지 않고, user-visible immediate work와 deferrable durable work는 background-work 정책으로 분리한다.

앱 컴포넌트는 이 layer를 시작하거나 연결하는 entry point다. Activity가 곧 ViewModel은 아니고, Service가 곧 repository는 아니며, Receiver가 곧 worker도 아니다.

관련 노트: [앱 컴포넌트 허브](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components.md), [ViewModel 정본](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md), [background work 정본](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md).

공식 문서: [Guide to app architecture](https://developer.android.com/topic/architecture)
