---
title: task-and-back-stack-are-os-activity-navigation-not-app-navigation-state.md
tags: [android, android/app-components, android/architecture, android/navigation]
aliases: ["Android task와 app back stack은 OS activity 내비게이션이다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android task와 app back stack은 OS activity 내비게이션이다

**안드로이드의 `Task` 와 `Back Stack` 은 OS 가 Activity 인스턴스들의 집합을 관리하는 레거시 및 멀티 윈도우 스택 매커니즘이다. 현대 Compose Single Activity 기반 애플리케이션 내부의 화면 내비게이션 상태(Navigation 3 BackStack)와 명확히 구분해야 한다.**

---

### 1. 개념 및 구별 (What)

- **OS Task & Back Stack**:
  Activity 의 `launchMode` (`singleTop`, `singleTask`, `singleInstance`) 및 Intent 플래그(`FLAG_ACTIVITY_NEW_TASK`)에 의해 OS 차원에서 Activity 히스토리를 스택으로 쌓는 구조.
- **App Internal Navigation Stack**:
  Compose 컴포저블 화면 전환을 관리하는 앱 내부 상태 스택 (`Navigation 3` / `NavHostController`).

---

### 2. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component-contracts.md)
- 관련 계약 문서:
  - [Navigation 3 Contracts](../../../navigation/navigation3/navigation3-contracts/navigation3-contracts.md)
- 공식 가이드: [Tasks and the Back Stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack)

검증일: 2026-08-05. OS Task 스택 및 앱 내비게이션 상태 구별 검증 완료.
