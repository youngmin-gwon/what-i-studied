---
title: entry-points-bridge-framework-owned-objects-to-the-graph
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:09:32 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Entry point 는 framework-owned 객체와 DI graph 를 잇는 예외 경계다

Android 에는 앱 코드가 생성자를 호출하지 않는 객체가 많다. ContentProvider, BroadcastReceiver, Worker, 일부 framework callback 주변 코드는 DI graph 안에서 자연스럽게 생성되지 않을 수 있다.

Entry point 는 이런 framework-owned 객체가 graph 의 dependency 를 꺼내야 할 때 쓰는 명시적 bridge 다. 하지만 entry point 를 아무 곳에서나 service locator 처럼 쓰면 DI 의 장점이 사라지므로, framework 가 소유한 경계에서만 제한적으로 사용한다.

관련 노트: [Hilt integration](./hilt-is-official-android-dagger-integration.md), [Worker injection](./worker-injection-crosses-workmanager-factory-boundary.md).

### 판단 기준

- ContentProvider, BroadcastReceiver 등 DI 프레임워크가 직접 지원하지 않는 프레임워크 소유 객체에서는 Entry Point 를 통해 직접 DI 그래프에 접근해 의존성을 가져와야 한다.

### 경계

- Entry Point 는 DI 그래프 외부에서 내부로 진입하는 최소한의 통로로만 사용되어야 하며, 일반적인 비즈니스 로직(ViewModel, Repository) 내부에서 남용해서는 안 된다.
