---
title: context-leaks-happen-when-reference-outlives-component-lifetime
tags: [android, android/architecture, android/context]
aliases: ["Context leak은 참조가 컴포넌트 수명보다 오래 살 때 발생한다"]
date modified: 2026-08-04 13:20:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Context leak 은 참조가 컴포넌트 수명보다 오래 살 때 발생한다

Context leak 의 핵심은 Activity context 라는 타입 이름 자체가 아니라 참조 수명이다. 오래 사는 singleton, callback, coroutine, cache 가 짧은 Activity/Receiver/Provider context 를 잡으면 component 가 종료된 뒤에도 해제되지 않을 수 있다.

해결책은 무조건 application context 로 치환하는 것이 아니다. UI 가 필요한 작업은 UI owner 에서 끝내고, 오래 살아야 하는 작업은 application context 나 좁은 platform abstraction 으로 분리하며, 등록한 callback/receiver/listener 는 owner lifecycle 에 맞춰 해제한다.

Context 선택은 memory leak, theme/window 정확성, permission/source identity 를 동시에 결정한다. 따라서 "compile error 를 없애기 위한 인자"가 아니라 architecture boundary 로 다뤄야 한다.

LeakCanary 같은 heap 분석 도구는 component 가 destroy 된 뒤에도 GC 대상이 되지 못한 참조 체인을 자동으로 찾아 보고한다. 이 보고서에 등장하는 retained object 체인이 바로 "무엇이 어떤 context 를 붙잡고 있는지"를 보여주는 관찰 가능한 신호다.

관련 노트: [Activity Context](./activity-context-carries-window-theme-and-short-lifetime.md), [Application Context](./application-context-fits-process-lifetime-work-not-themed-ui.md), [context-registered receiver 수명](../../app-components/app-component-contracts/context-registered-receiver-lifetime-follows-registering-context.md).

공식 문서: [Context reference](https://developer.android.com/reference/android/content/Context)
