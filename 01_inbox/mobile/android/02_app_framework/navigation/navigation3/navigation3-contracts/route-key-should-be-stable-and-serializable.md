---
title: route-key-should-be-stable-and-serializable
tags: [android, android/navigation, android/navigation3]
aliases: ["Navigation 3 route key는 UI 클래스가 아니라 안정적인 직렬화 식별자다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Navigation 3 route key 는 UI 클래스가 아니라 안정적인 직렬화 식별자다

Navigation 3 의 key 는 특정 Composable class 가 아니라 destination 을 식별하는 navigation state 다. key 는 equality 가 안정적이어야 하고, 필요한 argument 만 포함해야 하며, 저장/복원과 deep link 변환을 견딜 수 있어야 한다.

화면 구현 객체, Repository, ViewModel, callback 같은 runtime object 를 key 에 넣으면 저장과 비교가 깨진다. route key 는 domain identifier 와 primitive/serializable argument 중심으로 설계한다.

### 판단 기준

- key 는 process death 뒤에도 다시 만들 수 있는 값만 포함한다.
- 화면 표시용 객체나 callback 은 entry content 에서 주입한다.
- deep link parser 가 URI 를 typed key 로 변환할 수 있어야 한다.
- versioning 이 필요한 argument 는 기본값과 migration/fallback 을 함께 고려한다.

### 예시

```kotlin
// 피해야 하는 형태: repository와 콜백이 key 안에 들어 있다
data class BadDetailRoute(val order: Order, val onSave: () -> Unit) : NavKey

// 권장하는 형태: 복원 가능한 식별자만 남긴다
@Serializable
data class OrderDetailRoute(val orderId: String) : NavKey
```

`BadDetailRoute` 는 `Order` 나 lambda 를 저장/직렬화할 수 없으므로 `rememberNavBackStack` 의 saveable 복원이 런타임에 깨진다. `OrderDetailRoute` 처럼 primitive id 만 두면 딥 링크 파서와 process death 복원이 같은 값으로 key 를 재구성할 수 있다.

관련 노트: [Navigation 3 back stack은 저장 가능한 navigation state로 복원해야 한다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-back-stack-needs-saveable-restoration.md)

공식 문서: [Navigation 3 basics](https://developer.android.com/guide/navigation/navigation-3/basics)
