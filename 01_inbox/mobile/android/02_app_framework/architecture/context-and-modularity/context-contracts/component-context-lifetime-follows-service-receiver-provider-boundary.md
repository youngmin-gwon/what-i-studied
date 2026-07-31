---
title: "컴포넌트 Context의 수명은 Service, Receiver, Provider 경계를 따른다"
tags: [android, android/architecture, android/context]
aliases: ["컴포넌트 Context의 수명은 Service, Receiver, Provider 경계를 따른다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 컴포넌트 Context의 수명은 Service, Receiver, Provider 경계를 따른다

Service, BroadcastReceiver, ContentProvider도 각자 Context를 얻지만 의미와 수명이 다르다. Service context는 service lifecycle의 작업 경계에 묶이고, receiver callback context는 짧은 `onReceive` 실행 경계에 묶이며, provider context는 provider lifecycle과 process 초기화 순서에 묶인다.

Receiver context는 보관하지 않는다. Provider 초기화를 앱 전체 startup hook처럼 남용하지 않는다. Service context도 긴 background execution 보장을 뜻하지 않는다.

component context는 "Android API를 호출할 수 있다"는 공통점은 있지만, 어떤 callback과 수명에 귀속되는지가 다르다. 오래 살아야 하는 작업은 application context, scheduler, repository abstraction 같은 더 적절한 owner로 넘긴다.

관련 노트: [Service 경계](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/service-is-background-or-remote-work-entry-point-not-general-task-runner.md), [BroadcastReceiver 경계](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/broadcastreceiver-is-short-lived-event-entry-point-not-background-worker.md), [ContentProvider 경계](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/contentprovider-publishes-uri-addressed-data-with-permission-boundary.md).

공식 문서: [Application fundamentals](https://developer.android.com/guide/components/fundamentals)
