---
title: worker-injection-crosses-workmanager-factory-boundary
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:09:48 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Worker 주입은 WorkManager factory boundary 를 지난다

Worker 는 앱 코드가 직접 생성하는 일반 객체가 아니라 WorkManager 가 필요 시점에 생성하는 framework-managed 객체다. 그래서 Repository 같은 dependency 를 넣으려면 WorkerFactory 또는 Hilt WorkManager integration 같은 생성 boundary 를 통과해야 한다.

Worker 에 Activity, Fragment, screen-scoped object 를 넣으면 background execution lifetime 과 맞지 않는다. Worker dependency 는 작업이 실행되는 동안 안전한 app-level 또는 task-level dependency 로 제한한다.

관련 노트: [WorkManager](../../../04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md).

### 판단 기준

- WorkManager 의 Worker 는 백그라운드 환경에서 시스템에 의해 인스턴스화되므로, 커스텀 WorkerFactory 나 Hilt 의 `@HiltWorker` 를 통해 Worker 생성 시점에 의존성을 주입하도록 연결해야 한다.

### 경계

- Worker 생성자에는 일반적인 비즈니스 의존성뿐만 아니라 `Context` 와 `WorkerParameters` 를 반드시 함께 전달해야 하며, 시스템이 팩토리를 인식할 수 있도록 초기화 과정(Configuration)을 커스텀해야 한다.
