---
title: 12-doze-app-standby
tags: ["android", "android/glossary"]
aliases: ["App Standby", "Doze"]
date modified: 2026-08-03 17:21:37 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Doze 와 App Standby 는 백그라운드 앱의 리소스 접근을 제한하여 배터리를 절약한다

정의: Doze 와 App Standby 는 device idle 상태와 앱 사용 패턴에 따라 background execution, network, alarm 실행을 제한하는 power policy 다.

혼동 방지: 이 정책은 permission 부족과 다르다. 작업이 지연되거나 배치되는 것은 OS resource policy 의 결과일 수 있으므로, 보장된 작업은 WorkManager/JobScheduler 같은 persistent scheduler 로 표현해야 한다.

정본 링크:

- [Background restrictions](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-restrictions-require-persistent-work-state.md)
- [WorkManager default contract](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
