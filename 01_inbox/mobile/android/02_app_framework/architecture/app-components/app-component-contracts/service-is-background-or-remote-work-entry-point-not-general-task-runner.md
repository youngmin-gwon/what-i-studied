---
title: service-is-background-or-remote-work-entry-point-not-general-task-runner
tags: [android, android/app-components, android/architecture]
aliases: ["Service는 UI 없는 컴포넌트이지 일반 background task runner가 아니다"]
date modified: 2026-08-04 13:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Service 는 UI 없는 컴포넌트이지 일반 background task runner 가 아니다

Service 는 UI 없이 실행되는 앱 컴포넌트이며 started service, bound service, foreground service 같은 사용 형태를 가진다. 그러나 Service 자체가 worker thread 를 만들어 주지는 않는다. 콜백은 기본적으로 앱의 main thread 에서 실행된다.

그래서 Service 를 오래 걸리는 일반 작업 실행기로 보면 안 된다. 즉시 사용자 가시성이 필요한 연속 작업은 foreground service 를 검토하고, 지연 가능하고 보장되어야 하는 작업은 WorkManager 같은 background-work API 로 보내는 것이 보통 더 맞다.

Service 의 의미는 "작업을 어디서 실행할까"보다 "OS 와 어떤 실행 경계를 맺는가"에 있다. remote binding 이 필요하면 Binder 계약이 생기고, 사용자 가시성이 필요하면 notification 과 foreground-service 제약이 생긴다.

`adb shell dumpsys activity services <pkg>` 로 실행 중인 service 목록과 이를 소유한 process, started/bound 여부를 함께 확인할 수 있다. main thread 콜백이 오래 걸리면 이 service 는 별도 스레드 없이 그 자체로 ANR 후보가 된다.

관련 노트: [Foreground Service 경계](./foreground-service-is-user-visible-ongoing-work-contract.md), [Bound Service 경계](./bound-service-exposes-process-dependency-and-ipc-api.md), [background work 정본](../../../../04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md).

공식 문서: [Services overview](https://developer.android.com/develop/background-work/services)
