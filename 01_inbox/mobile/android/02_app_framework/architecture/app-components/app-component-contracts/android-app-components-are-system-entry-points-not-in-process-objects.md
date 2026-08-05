---
title: android-app-components-are-system-entry-points-not-in-process-objects
tags: [android, android/app-components, android/architecture]
aliases: ["안드로이드 앱 컴포넌트는 OS가 호출하는 실행 경계다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 안드로이드 앱 컴포넌트는 OS 가 호출하는 실행 경계다

상위 문서: [App Component Contracts](./app-component-contracts.md)
배경 지식: [IPC (Inter-Process Communication)](../../../../../../operating-systems/ipc-mechanisms.md)
Android 앱 컴포넌트는 앱 내부 객체 모델이 아니라 OS 가 앱을 시작하거나 앱과 상호작용할 때 찾는 entry point 다.

고전적인 네 가지 컴포넌트는 Activity, Service, BroadcastReceiver, ContentProvider 다. Android 앱은 하나의 `main()` 에서만 시작하지 않고, Manifest 와 Intent, Binder, URI 같은 외부 계약을 통해 여러 지점에서 프로세스가 만들어지고 코드가 호출될 수 있다.

그래서 앱 아키텍처에서 컴포넌트는 비즈니스 로직의 집이 아니라 경계 어댑터로 보는 편이 안전하다. Activity 는 화면과 lifecycle 을 연결하고, Service 는 UI 없는 작업 경계를 제공하며, Receiver 는 짧은 이벤트를 받아 후속 작업을 위임하고, Provider 는 URI 기반 데이터 접근 계약을 공개한다.

App Functions 같은 최신 agent/assistant surface 는 별도 플랫폼 capability 다. 고전적인 네 컴포넌트 목록에 억지로 섞기보다 [assistant/agent 정본](../../../../04_system_services/agents-and-assistant/assistant-agent-contracts/assistant-agent-contracts.md) 으로 연결한다.

관련 노트: [컴포넌트 통신 경계](./component-communication-uses-intent-binder-uri-and-pendingintent-by-boundary.md), [수명 기준 아키텍처 결정](../../jetpack-architecture/architecture-contracts/architecture-decisions-start-from-owner-lifetime-and-survival-requirements.md).

공식 문서: [Application fundamentals](https://developer.android.com/guide/components/fundamentals)
