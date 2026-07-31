---
title: "WorkManager와 JobScheduler"
tags: ["android", "android/glossary"]
aliases: ["WorkManager", "JobScheduler"]
---

# WorkManager와 JobScheduler

정의: WorkManager는 지연 가능하고 보장되어야 하는 app work를 표현하는 Jetpack API이고, JobScheduler는 OS가 제약 조건과 battery policy에 맞춰 job을 실행하는 platform scheduler다.

혼동 방지: 즉시 실행 UI event와 persistent background work를 같은 방식으로 처리하면 안 된다. 실패해도 재시도되어야 하는 작업은 durable work state로 표현해야 한다.

정본 링크:
- [WorkManager guaranteed work](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
- [Background work API selection](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-api-selection-is-a-failure-cost-decision.md)
