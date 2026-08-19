---
title: C1-background-and-scheduling
tags: [android/background, android/scheduling, android/system-services]
aliases: [백그라운드 실행과 스케줄링 선택, Background and Scheduling, 백그라운드 처리]
date created: 2026-08-04 16:00:00 +09:00
date modified: 2026-08-10 21:30:00 +09:00
---

## 백그라운드 실행과 스케줄링 선택

이 문서는 안드로이드 시스템에서 백그라운드 작업을 실행하고, 이를 스케줄링하며, 시스템과 사용자에게 알림을 전달하는 과정을 종합적으로 설명한다. 안드로이드의 백그라운드 실행은 시스템 자원(배터리, 메모리) 보존을 위해 매우 엄격하게 통제되며, 작업의 특성(지연 가능 여부, 정확한 시간 요구 여부, 사용자 인지 필요 여부)에 따라 적절한 API를 선택하는 것이 핵심이다.

### 이 주제를 읽기 전에
이 주제를 이해하기 위해 다음 선수 지식을 권장합니다.
- 안드로이드 4대 컴포넌트의 생명주기 및 프로세스 생명주기
- 시스템 서비스 조회 및 바인더 IPC 통신 구조

### 전체 조망도

```mermaid
flowchart TD
    App[App] -->|"Time-critical User Event"| AM[AlarmManager]
    App -->|"Deferrable Guaranteed Work"| WM[WorkManager]
    App -->|"Visible Continuous Work"| FS[Foreground Service]
    
    Cloud[Server] -->|"Push Message"| FCM[Firebase Cloud Messaging]
    FCM -->|"Data Payload"| App
    FCM -->|"Notification Payload"| NM[NotificationManager]
    App -->|"Local Notification"| NM
    
    NM --> UI[System UI / Lockscreen]
```

### 백그라운드 작업 API, 알림 및 메시징

#### 백그라운드 작업 API 선택 기준
작업의 지연 가능성과 실행 보장성, 그리고 사용자 가시성에 따라 백그라운드 실행 수단을 선택해야 한다. 각 수단은 실패 비용과 시스템 제약(Doze 모드 등)을 고려해 설계되었다.
- [백그라운드 작업 계약](../../04_system_services/background-and-notifications/background-work/background-work.md)
- [Background Work API selection is a failure cost decision](../../04_system_services/background-and-notifications/background-work/background-api-selection.md)
- [Background execution is selected by guarantee, delay, and visibility](../../04_system_services/background-and-notifications/background-work/background-execution-selection.md)
- [WorkManager is default for deferrable guaranteed work](../../04_system_services/background-and-notifications/background-work/work-manager.md)
- [AlarmManager is for time-based user events](../../04_system_services/background-and-notifications/background-work/alarm-manager.md)
- [Foreground Service is for visible continuous work](../../04_system_services/background-and-notifications/background-work/foreground-service.md)
- [Background restrictions require persistent work state](../../04_system_services/background-and-notifications/background-work/background-restrictions-state.md)

#### 알림 및 메시징 처리 (FCM & Notification)
FCM(Firebase Cloud Messaging)과 알림은 사용자의 주의를 끌고 작업을 재개하는 진입점이다. FCM 메시지는 페이로드 유형에 따라 처리 주체가 다르며, 메시지 전달 자체는 비즈니스 로직 실행을 보장하지 않는다.
- [알림과 FCM 메시징 계약](../../04_system_services/background-and-notifications/notification-messaging/notification-messaging.md)
- [Android notification permission and channel control visibility](../../04_system_services/background-and-notifications/notification-messaging/notification-permission-channel.md)
- [FCM operations observe delivery, display, tap, and recovery separately](../../04_system_services/background-and-notifications/notification-messaging/fcm-delivery-lifecycle.md)
- [FCM registration identifier targets app instance, not user account](../../04_system_services/background-and-notifications/notification-messaging/fcm-registration-token.md)
- [FCM high priority is justified by user-visible notification](../../04_system_services/background-and-notifications/notification-messaging/fcm-high-priority.md)
- [FCM notification and data payloads have different handling points](../../04_system_services/background-and-notifications/notification-messaging/fcm-payload-handling.md)
- [FCM is message delivery, not business execution guarantee](../../04_system_services/background-and-notifications/notification-messaging/fcm-delivery-guarantee.md)

### 이 주제와 연결된 Worked Example
- [04-fcm-to-notification-display-and-tap-recovery.md](../worked-examples/04-fcm-to-notification-display-and-tap-recovery.md)
- [05-process-death-recovery-of-edit-state-and-background-work.md](../worked-examples/05-process-death-recovery-of-edit-state-and-background-work.md)

### 이 주제와 연결된 Diagnostic Runbook
- [05-background-work-delayed-or-not-running.md](../diagnostic-runbooks/05-background-work-delayed-or-not-running.md)
- [06-notification-missing.md](../diagnostic-runbooks/06-notification-missing.md)

### 더 깊이 들어갈 때 (Learning Spine)
- [10-device-capability-discovery-and-background-execution.md](../learning-spine/10-device-capability-discovery-and-background-execution.md)
