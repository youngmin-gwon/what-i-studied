---
title: explicit-intent-targets-known-component-implicit-intent-declares-capability
tags: [android, android/navigation, android/intent]
aliases: ["Explicit intent는 알려진 컴포넌트를 지정하고 implicit intent는 요구 능력을 선언한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Explicit intent 는 알려진 컴포넌트를 지정하고 implicit intent 는 요구 능력을 선언한다

상위 문서: [Intent & Manifest 계약](intent-manifest.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - **Explicit Intent (명시적 인텐트)**: 호출할 타겟 컴포넌트의 클래스명(`DetailActivity::class.java`)이나 패키지명을 직접 명시하여 특정 대상에만 1:1로 전달하는 Intent다.
   - **Implicit Intent (암시적 인텐트)**: 호출 대상 컴포넌트를 직접 지정하지 않고, 수행하고자 하는 **Action**(`ACTION_VIEW`, `ACTION_DIAL`)과 **Data**, **Category**만 선언하여 안드로이드 OS가 만족하는 가장 적합한 앱 컴포넌트를 찾도록 요청하는 메시지다.
2. **필요성 (Why)**:
   - **앱 내부 탐색 보안**: 앱 내부 화면 간 이동 시 암시적 Intent를 사용하면 타 악성 앱이 메시지를 가로챌 위험이 있으므로 Explicit Intent를 사용해야 한다.
   - **모듈 간 생태계 연동**: 전화 걸기, 지형 지도 보기, 카메라 촬영 등 외부 앱의 기능을 빌려 쓸 때는 Implicit Intent를 통해 확장 가능성을 확보한다.

---

### 비교 구문 체계 (How)

```kotlin
// Explicit Intent: 정확히 앱 내부 컴포넌트 직접 지정
val explicitIntent = Intent(context, OrderDetailActivity::class.java).apply {
    putExtra("order_id", 1024)
}
context.startActivity(explicitIntent)

// Implicit Intent: 요구 기능(Action) 선언 및 OS 매칭 요청
val implicitIntent = Intent(Intent.ACTION_VIEW, Uri.parse("https://example.com"))
context.startActivity(implicitIntent)
```

---

### 관련 상위 및 연관 노트

- 상위 계약: [Intent & Manifest 계약](intent-manifest.md)
- 연관 계약: [Intent filter는 action, category, data를 매칭한다](intent-filter-matches-action-category-data.md)
