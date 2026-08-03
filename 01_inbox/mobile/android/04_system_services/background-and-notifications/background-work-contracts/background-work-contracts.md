---
title: "백그라운드 작업 계약"
tags: ["android", "android/system-services"]
---

# 백그라운드 작업 계약

이 지도는 Android 백그라운드 실행을 API 목록이 아니라 **작업이 살아야 하는 범위, 시작 시급성, 사용자 가시성, 시간 정확성, 전용 API 존재 여부**로 나눈다. `WorkManager`·foreground service·`AlarmManager`의 3분법은 충분하지 않다.

## 포함 범위와 제외 범위

- 포함: 화면에 종속된 비동기 작업, 영속 작업 스케줄링, 사용자 시작 전송, 사용자 가시 지속 작업, 시각 기반 이벤트, 시스템이 소유하는 다운로드.
- 제외: 각 API의 전체 구현법, FCM 전달 의미, notification UI 세부 정책. 이 지도는 먼저 올바른 실행 계약을 고르는 진입점이다.

## 첫 분기

1. 플랫폼이나 도메인 전용 API가 작업 전체를 맡을 수 있으면 먼저 사용한다. 예를 들어 단순 장시간 HTTP 다운로드는 `DownloadManager`가 연결 변화, 실패 재시도, 재부팅을 처리한다.
2. 화면을 떠날 때 버려도 되는 작업은 coroutine을 `lifecycleScope`나 `viewModelScope` 등 필요한 소유자의 생명주기에 묶는다.
3. 화면을 떠나도 완료돼야 하면 [실패 비용에 따른 선택](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-api-selection-is-a-failure-cost-decision.md)으로 이동한다.

## 지속 작업 선택 경로

| 요구의 핵심 | 먼저 읽을 계약 |
| --- | --- |
| 지연·재시도를 허용하며 앱/기기 재시작 뒤에도 예약을 복구 | [WorkManager](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md) |
| Android 14+에서 사용자가 시작한 장시간 업로드·다운로드를 즉시 진행하고 진행 알림 제공 | `RUN_USER_INITIATED_JOBS` 권한과 실행 중 notification을 갖춘 `JobScheduler` user-initiated data transfer job(UIDT) |
| WorkManager에 없는 `JobInfo` 기능이나 플랫폼 수준 job 제어가 필요 | 직접 `JobScheduler`; 편의·호환·영속 상태 관리는 앱 책임이 커진다 |
| 진행 중임을 사용자가 계속 알아야 하고 허용된 foreground service type에 해당 | [foreground service](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/foreground-service-is-for-visible-continuous-work.md) |
| 특정 시각에 깨우는 행위 자체가 사용자 기능 | [AlarmManager](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/alarmmanager-is-for-time-based-user-events.md) |
| 시스템 소유 HTTP 다운로드나 연결 기기·미디어 같은 전용 기능 | `DownloadManager` 또는 task-specific API |

## 공통 실패 모델

- 스케줄러의 "영속"은 예약을 보존하고 다시 실행한다는 뜻이다. 프로세스 메모리, 즉시 시작, 중단 없는 실행, 강제 중지 이후 실행까지 보장하지 않는다.
- callback 없이 프로세스가 죽을 수 있으므로 입력, 진행 위치, 중복 방지 키를 영속화하고 재실행을 멱등적으로 만든다.
- quota, Doze, standby bucket, constraint, 열 상태와 시스템 건강 때문에 시작이 늦거나 실행 중 중단될 수 있다.
- 알림은 단지 UI가 아니다. UIDT와 foreground service에서는 사용자 가시성 및 중지 가능성 계약의 일부다.

## 문제별 진입점

| 관찰한 문제 | 먼저 확인할 증거 | 진입 노트 |
| --- | --- | --- |
| 화면을 닫자 요청이 취소됨 | coroutine 소유 scope와 취소 시점 | [실패 비용에 따른 선택](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-api-selection-is-a-failure-cost-decision.md) |
| Worker가 실행되지 않음 | `WorkInfo`, `dumpsys jobscheduler`의 unsatisfied constraint·quota | [WorkManager](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md) |
| 긴 전송이 중단됨 | stop reason, 저장된 byte offset, notification 중지 경로 | 실패 비용에 따른 선택 |
| 서비스 시작 예외 | background start 제한, FGS type·permission | foreground service |
| 특정 시각을 놓침 | exact/inexact 선택과 exact alarm 권한 | AlarmManager |

## 관련 노트

- [백그라운드 제한은 작업 상태를 영속적으로 설계하게 만든다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-restrictions-require-persistent-work-state.md)
- [Android 백그라운드 실행은 보장, 지연, 사용자 가시성으로 선택한다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-execution-is-selected-by-guarantee-delay-and-visibility.md)
- [알림과 FCM 메시징 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md)

## 공식 근거

- [Background tasks overview](https://developer.android.com/develop/background-work/background-tasks)
- [Data transfer background task options](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options)
- [DownloadManager API](https://developer.android.com/reference/android/app/DownloadManager)

검증일: 2026-08-03.
