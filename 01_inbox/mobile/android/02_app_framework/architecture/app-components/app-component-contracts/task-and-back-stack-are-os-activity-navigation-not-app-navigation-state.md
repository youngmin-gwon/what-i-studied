---
title: task-and-back-stack-are-os-activity-navigation-not-app-navigation-state
tags: [android, android/app-components, android/architecture]
aliases: ["Task와 back stack은 OS가 관리하는 Activity 작업 기록이지 앱 내부 navigation state가 아니다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Task 와 back stack 은 OS 가 관리하는 Activity 작업 기록이지 앱 내부 navigation state 가 아니다

상위 문서: [App Component Contracts](./app-component-contracts.md)
Android task 와 back stack 은 사용자가 Activity 들을 어떤 작업 흐름으로 지나왔는지를 OS 가 관리하는 기록이다. Compose Navigation 이나 Navigation 3 의 route/back stack 은 앱 내부 화면 상태이고, Android task stack 과 같은 층위가 아니다.

`launchMode`, intent flags, document mode, deep link entry point 는 Activity 인스턴스가 어느 task 에 들어갈지 바꾼다. 하지만 앱 내부 화면 전환을 모두 launch mode 로 해결하려 하면 testability 와 상태 복구가 나빠진다.

일반 앱 화면 전환은 app-owned navigation state 로 다루고, 외부 진입점, task affinity, notification/deep link 복귀 정책처럼 OS 와 맞닿는 부분만 Activity task 정책으로 결정한다.

관련 노트: [Android task와 app back stack](../../../navigation/navigation3/navigation3-contracts/android-task-and-app-back-stack-are-different-stacks.md), [navigation 정본](../../../navigation/navigation-contracts/navigation-contracts.md), [intent/manifest 정본](../../../navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md).

공식 문서: [Tasks and back stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack)
