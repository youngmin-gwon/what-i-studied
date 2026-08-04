---
title: broadcastreceiver-is-short-lived-event-entry-point-not-background-worker
tags: [android, android/app-components, android/architecture]
aliases: ["BroadcastReceiver는 짧은 이벤트 entry point이지 background worker가 아니다"]
date modified: 2026-08-04 13:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## BroadcastReceiver 는 짧은 이벤트 entry point 이지 background worker 가 아니다

BroadcastReceiver 는 system 이나 app 이 보낸 broadcast message 를 받는 짧은 실행 경계다. `onReceive` 안에서 오래 걸리는 작업을 직접 처리하는 구조가 아니다.

Manifest-declared receiver 와 context-registered receiver 는 발견 방식, lifetime, export 정책이 다르다. Android 8 이후 manifest implicit broadcast 에는 제한이 있으므로 "모든 implicit broadcast 가 항상 온다"는 식의 모델은 맞지 않다.

Receiver 에서 받은 이벤트가 후속 작업을 필요로 하면 WorkManager, foreground service, app state update 같은 적절한 경계로 넘긴다. 내부 화면 이벤트 전달은 Flow/StateFlow/SharedFlow 같은 앱 내부 모델로 다루고, broadcast 를 내부 event bus 처럼 쓰지 않는다.

`adb shell dumpsys activity broadcasts` 로 대기/이력 broadcast 큐를 확인할 수 있다. `onReceive` 가 짧게 끝나지 않고 오래 실행되면, foreground 상태 기준 5 초 안에 [ANR runbook](../../../../00_foundations/diagnostic-runbooks/02-anr.md) 의 "Broadcast of intent" 트리거로 나타난다.

관련 노트: [background work 정본](../../../../04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md), [Flow/StateFlow 정본](../../../data/async-flow/flow-state-contracts/flow-state-contracts.md), [context-registered receiver 수명](./context-registered-receiver-lifetime-follows-registering-context.md).

공식 문서: [Broadcasts overview](https://developer.android.com/develop/background-work/background-tasks/broadcasts)
