---
title: "Worker 주입은 WorkManager factory boundary를 지난다"
tags: ["android", "android/app-framework"]
---

# Worker 주입은 WorkManager factory boundary를 지난다

Worker는 앱 코드가 직접 생성하는 일반 객체가 아니라 WorkManager가 필요 시점에 생성하는 framework-managed 객체다. 그래서 Repository 같은 dependency를 넣으려면 WorkerFactory 또는 Hilt WorkManager integration 같은 생성 boundary를 통과해야 한다.

Worker에 Activity, Fragment, screen-scoped object를 넣으면 background execution lifetime과 맞지 않는다. Worker dependency는 작업이 실행되는 동안 안전한 app-level 또는 task-level dependency로 제한한다.

관련 노트: [WorkManager](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md).

## 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

## 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime을 먼저 확인한다.
