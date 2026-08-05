---
title: navigation3-back-stack-needs-saveable-restoration
tags: [android, android/navigation, android/navigation3]
aliases: ["Navigation 3 back stack은 저장 가능한 navigation state로 복원해야 한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Navigation 3 back stack 은 저장 가능한 navigation state 로 복원해야 한다

배경 지식: [가상 메모리](../../../../../../operating-systems/virtual-memory.md), [프로세스 생명주기](../../../../../../operating-systems/process-states-lifecycle.md)

Navigation 3 에서는 앱이 back stack 을 소유한다. 따라서 configuration change 와 **process death**(메모리가 부족할 때 백그라운드 앱 프로세스를 OS가 강제로 종료하는 시스템 동작) 뒤에도 사용자가 있던 navigation 위치를 복원하려면 saveable back stack 전략이 필요하다.

`rememberNavBackStack` 은 `NavKey` 기반 back stack 을 기억하고 저장/복원하는 편의 API 다. 이 API 를 쓰려면 key 가 `NavKey` 를 구현하고 serialization 요구사항을 만족해야 한다.

Back stack state 와 screen UI state 는 다르다. 어떤 화면이 stack 에 있는지와 그 화면 안의 form/input/loading state 를 같은 객체에 섞으면 복원과 deep link 처리가 불안정해진다.

### 판단 기준

- key 에는 화면 복원에 필요한 최소 식별자만 둔다.
- detail 화면의 form state, scroll state, loading state 는 별도 UI state 로 분리한다.
- deep link 는 최종 key 만 push 하지 말고 필요한 root stack 을 함께 구성한다.
- process death 복원 뒤 사용할 수 없는 key 는 fallback destination 으로 수렴시킨다.

### 예시

```kotlin
@Serializable
data class OrderDetailRoute(val orderId: String, val scrollIndex: Int) : NavKey

val backStack = rememberNavBackStack(DashboardRoute)
```

`scrollIndex` 같은 화면 내부 UI state 를 `OrderDetailRoute` key 에 넣으면, key 가 바뀔 때마다 `equals()` 비교와 저장된 stack 이 함께 흔들린다. scroll/loading state 는 key 가 아니라 해당 destination composable 안의 `**rememberSaveable**(프로세스 재시작이나 화면 회전 시에도 UI 상태 값을 복원 가능하도록 Bundle에 저장하는 Compose 도구)` 로 분리해야 한다.

관련 노트: [NavKey와 back stack은 앱이 소유하는 navigation 상태다](navkey-and-back-stack-are-app-owned-navigation-state.md), [Android 상태 관리 정본 지도](../../../architecture/state-management/android-state-management.md)

공식 문서: [Save and manage navigation state](https://developer.android.com/guide/navigation/navigation-3/save-state), [rememberNavBackStack](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/rememberNavBackStack.composable)
