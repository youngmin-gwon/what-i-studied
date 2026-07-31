---
title: 28-workmanager-jobscheduler
tags: ["android", "android/glossary"]
aliases: ["JobScheduler", "WorkManager"]
date modified: 2026-08-01 01:07:52 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## WorkManager 와 JobScheduler

정의: WorkManager 는 지연 가능하고 보장되어야 하는 app work 를 표현하는 Jetpack API 이고, JobScheduler 는 OS 가 제약 조건과 battery policy 에 맞춰 job 을 실행하는 platform scheduler 다.

혼동 방지: 즉시 실행 UI event 와 persistent background work 를 같은 방식으로 처리하면 안 된다. 실패해도 재시도되어야 하는 작업은 durable work state 로 표현해야 한다.

정본 링크:

- [WorkManager guaranteed work](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
- [Background work API selection](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-api-selection-is-a-failure-cost-decision.md)
