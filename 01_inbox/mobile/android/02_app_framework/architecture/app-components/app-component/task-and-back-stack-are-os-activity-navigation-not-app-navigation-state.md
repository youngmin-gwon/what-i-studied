---
title: task-and-back-stack-are-os-activity-navigation-not-app-navigation-state
tags: [android, android/app-components, android/architecture, android/navigation]
aliases: ["Android task와 app back stack은 OS activity 내비게이션이다"]
date modified: 2026-08-06 15:03:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Task back stack은 OS Activity 기록이고 앱 내부 navigation state와 독립적이다

Task는 사용자가 하나의 일을 수행하며 연 Activity instance의 집합이고, OS back stack은 이를 LIFO 순서로 관리한다. Single-Activity 앱의 `NavController`나 Navigation 3 back stack은 한 Activity 안의 앱 상태다. 두 stack은 함께 움직일 때가 많지만 process death, deep link, multi-window, 외부 Activity 전환에서는 독립적으로 변할 수 있다.

### launch mode 메커니즘

| 규칙 | instance 선택 | 새 Intent 전달 |
| --- | --- | --- |
| 기본 `standard` | 호출할 때마다 새 instance | `onCreate()` |
| `singleTop` / `FLAG_ACTIVITY_SINGLE_TOP` | 대상이 현재 task top일 때만 재사용 | `onNewIntent()` |
| `FLAG_ACTIVITY_CLEAR_TOP` | 같은 task의 대상 위 Activity를 제거 | 대상이 `standard`면 대상도 재생성될 수 있음 |
| `singleTask` / `FLAG_ACTIVITY_NEW_TASK` 계열 | affinity와 기존 task를 찾아 전면 이동할 수 있음 | 기존 instance면 `onNewIntent()` |

`singleTask`와 `singleInstance`를 “중복 화면 방지” 도구로 습관적으로 쓰면 다른 앱에서 들어온 문서·인증 flow와 Recents 동작을 바꾼다. 기본 `standard`를 유지하고 요구되는 system-level task 동작이 있을 때만 device/API 조합별로 검증한다.

### `singleTop` 최소 처리

```xml
<activity
    android:name=".MainActivity"
    android:exported="true"
    android:launchMode="singleTop" />
```

```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
    routeDeepLink(intent)
}
```

instance가 재사용되면 `onCreate()`가 다시 호출되지 않으므로 새 deep link를 `onNewIntent()`에서도 소비해야 한다. `intent` property를 이후 코드가 읽으면 `setIntent()`도 갱신한다.

### 실패·관찰 신호

- 같은 deep link 두 번 실행 뒤 새 화면이 생기는지 기존 화면의 `onNewIntent()`가 호출되는지 instance ID로 기록한다.
- `adb shell dumpsys activity activities`에서 `Task{}`, `Hist`, `mResumedActivity`를 확인한다.
- `adb shell am start -W -n <package>/.MainActivity --es route first`를 반복해 launch mode별 stack 변화를 재현한다.
- Back이 예상치 못한 앱이나 빈 화면으로 이동하면 `taskAffinity`, `NEW_TASK`, `CLEAR_TOP`, manifest launch mode를 함께 조사한다.

관련 노트: [Navigation 3 Contracts](../../../navigation/navigation3/navigation3/navigation3.md)

상위 문서: [App Component Contracts](./app-component.md)

공식 문서: [Tasks and the back stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack)
