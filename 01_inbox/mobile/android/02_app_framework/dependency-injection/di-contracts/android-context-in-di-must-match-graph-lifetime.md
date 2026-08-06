---
title: android-context-in-di-must-match-graph-lifetime
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:28:45 +09:00
---

## DI graph 에 넣는 Android Context 는 graph lifetime 과 맞아야 한다

`Context` 는 단순 dependency 가 아니라 resource, service, permission, theme, lifecycle 과 연결된 platform capability 다. Application graph 에는 `applicationContext` 처럼 app lifetime 과 맞는 Context 만 넣어야 한다.

Activity 나 Fragment Context 를 app-wide graph 에 넣으면 화면이 사라진 뒤에도 UI owner 가 붙잡힐 수 있다. 반대로 theme, window, UI-bound service 가 필요한 작업에는 Application Context 가 충분하지 않을 수 있으므로 더 짧은 owner boundary 에서 받아야 한다.

### 최소 예시

```kotlin
class AssetReader @Inject constructor(
    @ApplicationContext private val context: Context,
)

@ActivityScoped
class DialogHost @Inject constructor(
    @ActivityContext private val context: Context,
)
```

`AssetReader`는 process 동안 살아도 되는 app capability만 사용한다. `DialogHost`는 window와 theme가 있는 현재 Activity에 묶고 `ActivityComponent`보다 길게 보관하지 않는다. qualifier는 같은 `Context` 타입의 의미를 구분할 뿐 lifetime을 자동으로 줄이지 않으므로 scope와 저장 위치를 함께 본다.

### 실패와 관찰 신호

- singleton이 `@ActivityContext`를 잡으면 화면 종료 뒤에도 Activity가 남아 LeakCanary retained-object 경고로 보일 수 있다.
- `applicationContext`로 dialog를 띄우면 window token 오류가 나거나 화면 theme와 다른 UI가 만들어질 수 있다.
- Hilt binding의 scope가 설치 component와 맞지 않으면 build에서 scope/component mismatch가 난다.

관련 노트: [Context boundaries](../../architecture/context-and-modularity/android-context-boundaries.md)

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Hilt component lifetimes](https://developer.android.com/training/dependency-injection/hilt-android#component-lifetimes)
