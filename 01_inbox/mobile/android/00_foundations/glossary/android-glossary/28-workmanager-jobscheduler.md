---
title: 28-workmanager-jobscheduler
tags: ["android", "android/glossary"]
aliases: ["JobScheduler", "WorkManager"]
date modified: 2026-08-03 17:21:17 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## WorkManager 와 JobScheduler 는 조건에 맞춰 백그라운드 작업을 안정적으로 예약하고 실행한다

정의: WorkManager 는 앱이나 device 가 재시작되어도 지속해야 하는 지연 가능한 app work 를 표현하는 Jetpack API 이고, JobScheduler 는 OS 가 제약 조건과 battery policy 에 맞춰 job 을 실행하는 platform scheduler 다.

혼동 방지: `guaranteed` 는 즉시 실행이나 무조건 성공을 뜻하지 않는다. WorkManager 는 등록된 작업의 실행 시도를 지속할 수 있지만 제약 조건, quota, retry 정책에 따라 지연되며, 성공 조건과 idempotency 는 앱이 설계해야 한다.

정본 링크:

- [WorkManager guaranteed work](../../../04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
- [Background work API selection](../../../04_system_services/background-and-notifications/background-work-contracts/background-work-api-selection-is-a-failure-cost-decision.md)
