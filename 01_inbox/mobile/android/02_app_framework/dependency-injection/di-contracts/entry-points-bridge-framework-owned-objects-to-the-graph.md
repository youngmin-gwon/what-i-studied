---
title: "Entry point는 framework-owned 객체와 DI graph를 잇는 예외 경계다"
tags: ["android", "android/app-framework"]
---

# Entry point는 framework-owned 객체와 DI graph를 잇는 예외 경계다

Android에는 앱 코드가 생성자를 호출하지 않는 객체가 많다. ContentProvider, BroadcastReceiver, Worker, 일부 framework callback 주변 코드는 DI graph 안에서 자연스럽게 생성되지 않을 수 있다.

Entry point는 이런 framework-owned 객체가 graph의 dependency를 꺼내야 할 때 쓰는 명시적 bridge다. 하지만 entry point를 아무 곳에서나 service locator처럼 쓰면 DI의 장점이 사라지므로, framework가 소유한 경계에서만 제한적으로 사용한다.

관련 노트: [Hilt integration](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/hilt-is-official-android-dagger-integration.md), [Worker injection](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/worker-injection-crosses-workmanager-factory-boundary.md).

## 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

## 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime을 먼저 확인한다.
