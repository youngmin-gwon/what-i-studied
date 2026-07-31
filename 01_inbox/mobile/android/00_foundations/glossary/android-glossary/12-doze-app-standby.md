---
title: "Doze와 App Standby"
tags: ["android", "android/glossary"]
aliases: ["Doze", "App Standby"]
---

# Doze와 App Standby

정의: Doze와 App Standby는 device idle 상태와 앱 사용 패턴에 따라 background execution, network, alarm 실행을 제한하는 power policy다.

혼동 방지: 이 정책은 permission 부족과 다르다. 작업이 지연되거나 배치되는 것은 OS resource policy의 결과일 수 있으므로, 보장된 작업은 WorkManager/JobScheduler 같은 persistent scheduler로 표현해야 한다.

정본 링크:
- [Background restrictions](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-restrictions-require-persistent-work-state.md)
- [WorkManager default contract](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
