---
title: navkey-and-back-stack-are-app-owned-navigation-state
tags: [android, android/navigation, android/navigation3]
aliases: ["NavKey와 back stack은 앱이 소유하는 navigation 상태다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## NavKey 와 back stack 은 앱이 소유하는 navigation 상태다

상위 문서: [Navigation 3 계약](navigation3.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - **`NavKey`**는 목적지의 정체성과 복원에 필요한 최소 인자를 불변(Immutable) 상태로 캡슐화한 개체이며, **`NavBackStack`**은 이 키들이 쌓여 있는 상태 컬렉션으로, 프레임워크 라이브러리가 아닌 **애플리케이션이 직접 소유하는 Compose State**이다.
2. **필요성 (Why)**:
   - 화면 이동이 더 이상 뷰 프레임워크 API 호출(`navController.navigate()`)이 아니라, 앱이 소유한 스택 상태를 변경(`backStack.add(Key)`)하는 단방향 데이터 흐름(UDF) 상태 전이로 명확해진다.

---

### 핵심 구현 코드 예시

```kotlin
@Serializable
data class ProductDetailRoute(val productId: String) : NavKey

// 앱이 직접 소유하는 백스택 상태
val backStack = rememberNavBackStack(DashboardRoute)

// 명시적인 상태 전이
fun onProductClick(id: String) {
    backStack.add(ProductDetailRoute(productId = id))
}

fun onBackClick() {
    backStack.removeLastOrNull()
}
```

---

### 관련 상위 및 연관 노트

- 상위 계약: [Navigation 3 계약](navigation3.md)
- 연관 가이드: [Jetpack Navigation 3 가이드](../jetpack-navigation-3-guide.md)
