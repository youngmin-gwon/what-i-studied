---
title: component-context-lifetime-follows-service-receiver-provider-boundary
tags: [android, android/architecture, android/context]
aliases: ["컴포넌트 Context의 수명은 Service, Receiver, Provider 경계를 따른다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 컴포넌트 Context 의 수명은 Service, Receiver, Provider 경계를 따른다

상위 문서: [Android Context Boundaries](../android-context-boundaries.md)
Service, BroadcastReceiver, ContentProvider 도 각자 Context 를 얻지만 의미와 수명이 다르다. Service context 는 service lifecycle 의 작업 경계에 묶이고, receiver callback context 는 짧은 `onReceive` 실행 경계에 묶이며, provider context 는 provider lifecycle 과 process 초기화 순서에 묶인다.

Receiver context 는 보관하지 않는다. Provider 초기화를 앱 전체 startup hook 처럼 남용하지 않는다. Service context 도 긴 background execution 보장을 뜻하지 않는다.

component context 는 "Android API 를 호출할 수 있다"는 공통점은 있지만, 어떤 callback 과 수명에 귀속되는지가 다르다. 오래 살아야 하는 작업은 application context, scheduler, repository abstraction 같은 더 적절한 owner 로 넘긴다.

`goAsync()` 없이 `onReceive` 안에서 콜백을 비동기로 넘겨 나중에 실행하면, 시스템이 이미 receiver 를 비활성 처리한 뒤이므로 해당 시점에 Context 기반 API 를 호출하면 실패하거나 예외로 이어질 수 있다. 이는 receiver context 의 수명이 `onReceive` 실행 구간 자체로 끝난다는 것을 보여주는 관찰 가능한 신호다.

관련 노트: [Service 경계](../../app-components/app-component-contracts/service-is-background-or-remote-work-entry-point-not-general-task-runner.md), [BroadcastReceiver 경계](../../app-components/app-component-contracts/broadcastreceiver-is-short-lived-event-entry-point-not-background-worker.md), [ContentProvider 경계](../../app-components/app-component-contracts/contentprovider-publishes-uri-addressed-data-with-permission-boundary.md).

공식 문서: [Application fundamentals](https://developer.android.com/guide/components/fundamentals)
