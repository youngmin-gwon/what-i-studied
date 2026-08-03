---
title: foreground-service-is-user-visible-ongoing-work-contract
tags: [android, android/app-components, android/architecture]
aliases: ["Foreground Service는 사용자에게 보이는 진행 중 작업 계약이다"]
date modified: 2026-08-03 17:27:05 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Foreground Service 는 사용자에게 보이는 진행 중 작업 계약이다

Foreground Service 는 사용자가 인지해야 하는 즉시성, 진행 중 작업을 OS 에 알리는 계약이다. notification 을 통해 사용자에게 노출되며, Android 버전과 target SDK 에 따라 foreground-service type, permission, start restriction, timeout 조건이 달라진다.

따라서 "백그라운드에서 오래 실행하고 싶다"는 이유만으로 Foreground Service 를 선택하면 안 된다. 음악 재생, active navigation, ongoing call, 사용자 시작 데이터 전송처럼 사용자 가시성과 즉시성이 있는지 먼저 확인해야 한다.

지연 가능하고 네트워크/충전/재시도 제약을 가진 작업은 WorkManager 가 더 적합한 경우가 많다. Foreground Service 는 background-work API 선택표의 한 칸이지 우회 수단이 아니다.

관련 노트: [background-work의 foreground service 정본](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/foreground-service-is-for-visible-continuous-work.md), [background work 정본](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md), [Android 권한 계약](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md).

공식 문서: [Foreground services](https://developer.android.com/develop/background-work/services/fgs)
