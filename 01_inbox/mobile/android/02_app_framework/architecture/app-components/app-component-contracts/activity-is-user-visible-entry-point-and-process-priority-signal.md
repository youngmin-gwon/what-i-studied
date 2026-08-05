---
title: activity-is-user-visible-entry-point-and-process-priority-signal
tags: [android, android/app-components, android/architecture]
aliases: ["Activity는 사용자에게 보이는 entry point이자 프로세스 우선순위 신호다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Activity 는 사용자에게 보이는 entry point 이자 프로세스 우선순위 신호다

상위 문서: [App Component Contracts](./app-component-contracts.md)
배경 지식: [프로세스 생명주기 및 메모리 회수](../../../../../../operating-systems/process-states-lifecycle.md)
Activity 는 사용자가 직접 보고 상호작용하는 앱 컴포넌트다. 런처 아이콘, notification, deep link, 다른 앱의 explicit/implicit Intent 는 Activity 를 통해 앱의 특정 화면으로 들어올 수 있다.

Activity 는 단순한 화면 클래스가 아니다. 현재 visible/resumed Activity 는 Android 가 프로세스 중요도를 판단하는 강한 신호가 된다. 사용자가 보는 화면을 잃으면 앱 프로세스는 더 쉽게 회수될 수 있고, 이때 화면 상태와 영속 데이터 복구 전략이 필요해진다.

Compose single Activity 구조를 쓰더라도 Activity 경계는 사라지지 않는다. multi-window, external intent, task/back stack, configuration change, process death 는 여전히 Activity 단위로 발생한다.

`adb shell dumpsys activity activities` 의 `mResumedActivity` 필드로 현재 최상단 Activity 를, `adb shell dumpsys activity processes` 의 importance/oom_adj 값으로 그 Activity 를 가진 프로세스의 우선순위를 직접 확인할 수 있다. Activity 를 잃은 프로세스는 이 값이 눈에 띄게 낮아진다.

관련 노트: [Activity lifecycle 콜백](./activity-lifecycle-callbacks-describe-visibility-and-interaction-boundaries.md), [Android task와 app back stack](../../../navigation/navigation3/navigation3-contracts/android-task-and-app-back-stack-are-different-stacks.md), [상태 관리 정본](../../state-management/android-state-management.md).

공식 문서: [Activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle)
