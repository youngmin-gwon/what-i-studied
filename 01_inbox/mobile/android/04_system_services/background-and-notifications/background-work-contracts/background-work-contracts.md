---
title: "백그라운드 작업 계약"
tags: ["android", "android/system-services"]
---

# 백그라운드 작업 계약

이 지도는 Android 백그라운드 실행을 API 목록이 아니라 실행 보장, 지연 허용도, 사용자 가시성, 시간 정확성의 판단 단위로 나눈다.

## 읽는 순서

1. [Android 백그라운드 실행은 보장, 지연, 사용자 가시성으로 선택한다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-execution-is-selected-by-guarantee-delay-and-visibility.md)로 요구사항을 분류한다.
2. [백그라운드 제한은 작업 상태를 영속적으로 설계하게 만든다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-restrictions-require-persistent-work-state.md)로 프로세스 종료와 재실행 경계를 잡는다.
3. 지연 가능한 작업은 [WorkManager](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md), 사용자 가시 지속 작업은 [foreground service](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/foreground-service-is-for-visible-continuous-work.md), 시각 자체가 기능이면 [AlarmManager](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/alarmmanager-is-for-time-based-user-events.md)를 읽는다.
4. [백그라운드 실행 수단은 실패 비용으로 결정한다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-api-selection-is-a-failure-cost-decision.md)로 선택과 테스트를 기록한다.

## 문제 분류

| 문제 | 분류 기준 | 진입 노트 |
| --- | --- | --- |
| 프로세스 종료 뒤 작업이 사라짐 | 요청과 진행 상태가 메모리에만 있는가 | 백그라운드 제한 |
| 작업이 늦게 시작됨 | 지연이 정상 스케줄링인지 실패인지 | WorkManager |
| 특정 시각을 놓침 | inexact로 충분한지 exact 권한이 필요한지 | AlarmManager |
| 서비스 시작 예외 | 백그라운드 시작 제한, FGS type, while-in-use 권한 | foreground service |
| 같은 업로드가 중복됨 | 재시도 가능한 도메인 작업이 멱등적인가 | 실패 비용 결정 |

## API 경계

- WorkManager의 보장은 조건이 충족되는 동안 영속적으로 스케줄을 관리한다는 뜻이지 즉시 실행, 정확한 시각, 앱 강제 중지 이후 실행을 보장한다는 뜻이 아니다.
- foreground service는 사용자가 알아야 하는 진행 중 작업을 위한 실행 상태다. 단순히 프로세스 우선순위를 올리는 우회 수단이 아니다.
- AlarmManager는 시간을 트리거하지만 긴 작업의 실행 컨테이너는 아니다. 수신 뒤 필요한 작업은 적절한 컴포넌트에 위임한다.

## 노트 목록

- [Android 백그라운드 실행은 보장, 지연, 사용자 가시성으로 선택한다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-execution-is-selected-by-guarantee-delay-and-visibility.md)
- [백그라운드 제한은 작업 상태를 영속적으로 설계하게 만든다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-restrictions-require-persistent-work-state.md)
- [WorkManager는 지연 가능한 보장 작업의 기본 선택이다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
- [Foreground service는 사용자에게 보이는 지속 작업에 쓴다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/foreground-service-is-for-visible-continuous-work.md)
- [AlarmManager는 시간 자체가 기능인 이벤트에 쓴다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/alarmmanager-is-for-time-based-user-events.md)
- [백그라운드 실행 수단은 실패 비용으로 결정한다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-api-selection-is-a-failure-cost-decision.md)

관련 지도: [알림과 FCM 메시징 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md)
