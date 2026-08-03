---
title: navkey-and-back-stack-are-app-owned-navigation-state
tags: [android, android/navigation, android/navigation3]
aliases: ["NavKey 와 back stack 은 앱 내부 상태다"]
date modified: 2026-08-03 18:12:03 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## NavKey 와 back stack 은 앱 내부 상태다

상위 문서: [Navigation 3 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-contracts.md)

### 핵심 주장

Navigation 3 에서 화면 이동은 문자열 주소를 해석하는 일이 아니라 `NavKey` 목록을 바꾸는 일이다.

`NavKey` 는 현재 화면의 정체성과 복원에 필요한 최소 인자를 표현한다.

`NavBackStack` 은 그 key 들이 쌓인 순서이며 앱이 소유하는 Compose 상태다.

```kotlin
@Serializable
data class TrainingDetailRoute(val id: String) : NavKey

val backStack = rememberNavBackStack(DashboardRoute)
backStack.add(TrainingDetailRoute(id = "123"))
backStack.removeLastOrNull()
```

### 설계 규칙

- key 에는 화면 복원에 필요한 식별자만 넣는다.
- repository, 화면 객체, callback, 거대한 도메인 객체는 key 에 넣지 않는다.
- route 의 타입이 화면에 필요한 인자를 직접 드러내게 한다.
- 인증 흐름과 로그인 후 흐름의 key 집합을 구분한다.
- top-level destination 은 하위 detail route 와 다른 정책 축으로 표시한다.
- push 와 pop 은 임의의 UI 이벤트가 아니라 명시적인 상태 전이로 다룬다.

`NavBackStack` 을 여러 composable 이 직접 수정하면 전이 규칙이 흩어진다.

대신 feature 별 명령 함수를 두어 허용되는 변경을 이름으로 표현한다.

```kotlin
fun NavBackStack<NavKey>.openTraining(id: String) {
    add(TrainingDetailRoute(id))
}
```

로그인 후 앱에서는 top-level destination 별 stack 을 보존할 수 있다.

탭을 바꿀 때 현재 stack 을 지우고 새 root 만 넣으면 detail 상태가 사라진다.

각 destination 의 stack 을 저장하고 선택된 stack 만 렌더링하면 사용자가 돌아왔을 때 문맥이 유지된다.

이 상태 모델은 UI 보다 오래 살아야 하는 이동 의도를 표현한다.

화면은 현재 key 를 렌더링하고, 이동 callback 은 새 key 를 상태에 추가한다.

따라서 화면이 어떤 navigation library API 를 호출하는지보다 어떤 상태 전이를 허용하는지가 먼저다.

### 점검 질문

- 이 route 를 프로세스 복원 뒤 다시 만들 수 있는가?
- back 동작이 마지막 key 제거로 설명되는가?
- top-level 전환이 다른 destination 의 상태를 불필요하게 폐기하지 않는가?
- 외부 URI 나 인증 결과도 결국 명확한 key 목록으로 수렴하는가?
