---
title: context-registered-receiver-lifetime-follows-registering-context
tags: [android, android/app-components, android/architecture]
aliases: ["Context-registered Receiver의 수명은 등록한 Context를 따른다"]
date modified: 2026-08-03 17:27:02 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Context-registered Receiver 의 수명은 등록한 Context 를 따른다

동적으로 등록한 BroadcastReceiver 는 등록한 Context 의 수명과 export flag 정책을 따른다. Activity context 로 등록하면 화면 수명과 맞춰 해제해야 하고, application context 로 등록하면 더 오래 살아남을 수 있으므로 필요 범위를 좁혀야 한다.

이 차이는 memory leak 과 보안 경계로 이어진다. 짧은 화면 이벤트를 듣는 receiver 를 application context 에 묶으면 불필요하게 오래 남고, 외부 broadcast 를 받는 receiver 의 export/permission 결정을 흐리면 공격 surface 가 커진다.

Receiver 는 callback context 를 보관하지 않고 즉시 필요한 값만 추출한 뒤, 오래 걸리는 일은 lifecycle 에 맞는 owner 나 scheduler 로 넘긴다.

관련 노트: [component Context 수명](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/component-context-lifetime-follows-service-receiver-provider-boundary.md), [BroadcastReceiver 경계](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/broadcastreceiver-is-short-lived-event-entry-point-not-background-worker.md), [Android 권한 계약](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md).

공식 문서: [Broadcasts overview](https://developer.android.com/develop/background-work/background-tasks/broadcasts)
