---
title: "Context leak은 참조가 컴포넌트 수명보다 오래 살 때 발생한다"
tags: [android, android/architecture, android/context]
aliases: ["Context leak은 참조가 컴포넌트 수명보다 오래 살 때 발생한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Context leak은 참조가 컴포넌트 수명보다 오래 살 때 발생한다

Context leak의 핵심은 Activity context라는 타입 이름 자체가 아니라 참조 수명이다. 오래 사는 singleton, callback, coroutine, cache가 짧은 Activity/Receiver/Provider context를 잡으면 component가 종료된 뒤에도 해제되지 않을 수 있다.

해결책은 무조건 application context로 치환하는 것이 아니다. UI가 필요한 작업은 UI owner에서 끝내고, 오래 살아야 하는 작업은 application context나 좁은 platform abstraction으로 분리하며, 등록한 callback/receiver/listener는 owner lifecycle에 맞춰 해제한다.

Context 선택은 memory leak, theme/window 정확성, permission/source identity를 동시에 결정한다. 따라서 "compile error를 없애기 위한 인자"가 아니라 architecture boundary로 다뤄야 한다.

관련 노트: [Activity Context](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/activity-context-carries-window-theme-and-short-lifetime.md), [Application Context](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/application-context-fits-process-lifetime-work-not-themed-ui.md), [context-registered receiver 수명](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/context-registered-receiver-lifetime-follows-registering-context.md).

공식 문서: [Context reference](https://developer.android.com/reference/android/content/Context)
