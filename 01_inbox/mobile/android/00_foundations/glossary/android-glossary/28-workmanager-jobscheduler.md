---
title: 28-workmanager-jobscheduler
tags: ["android", "android/glossary"]
aliases: ["JobScheduler", "WorkManager"]
date modified: 2026-08-01 01:07:52 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## WorkManager 와 JobScheduler

정의: WorkManager는 앱이나 device가 재시작되어도 지속해야 하는 지연 가능한 app work를 표현하는 Jetpack API이고, JobScheduler는 OS가 제약 조건과 battery policy에 맞춰 job을 실행하는 platform scheduler다.

혼동 방지: `guaranteed`는 즉시 실행이나 무조건 성공을 뜻하지 않는다. WorkManager는 등록된 작업의 실행 시도를 지속할 수 있지만 제약 조건, quota, retry 정책에 따라 지연되며, 성공 조건과 idempotency는 앱이 설계해야 한다.

정본 링크:

- [WorkManager guaranteed work](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
- [Background work API selection](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-api-selection-is-a-failure-cost-decision.md)
