---
title: component-communication-uses-intent-binder-uri-and-pendingintent-by-boundary
tags: [android, android/app-components, android/architecture]
aliases: ["컴포넌트 통신은 Intent, Binder, URI, PendingIntent 경계로 나눈다"]
date modified: 2026-08-03 17:26:59 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 컴포넌트 통신은 Intent

Android component communication 은 하나의 event bus 가 아니다. Activity, Service, Receiver 시작은 Intent 가 맡고, bound service 호출은 Binder 가 맡으며, provider 데이터 접근은 URI 와 `ContentResolver` 가 맡고, 미래의 system-mediated 실행 위임은 PendingIntent 가 맡는다.

통신 수단은 수명과 신뢰 경계로 고른다. 같은 앱 화면 상태 변경은 ViewModel/Flow 로 충분하고, 앱 외부 entry point 는 Intent/Manifest 계약이 필요하며, cross-process method call 은 Binder/AIDL 부담을 받아들여야 한다.

특히 Service 시작에는 explicit Intent 를 선호해야 한다. implicit Intent 는 resolution 과 hijacking 위험이 있고, 공개 component 와 권한 경계를 명확히 하지 못하면 보안 문제가 된다.

관련 노트: [intent/manifest 정본](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md), [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md), [PendingIntent 정본](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/pendingintent-is-delegated-future-intent-token.md).

공식 문서: [Application fundamentals](https://developer.android.com/guide/components/fundamentals)
