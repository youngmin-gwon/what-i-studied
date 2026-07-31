# 5 `LocalMyBenefitLayoutMetrics.kt`

상위 노트: [06-각-파일의-역할](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/06-%EA%B0%81-%ED%8C%8C%EC%9D%BC%EC%9D%98-%EC%97%AD%ED%95%A0.md)

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/LocalMyBenefitLayoutMetrics.kt
```

역할:

- 현재 window size에 맞는 `MyBenefitLayoutMetrics`를 하위 화면에 전달합니다.
- UI 코드에서 가장 자주 쓰는 adaptive 값이라 `LocalMyBenefitWindowAdaptivity.current.layoutMetrics`와 별도로 제공합니다.

읽는 위치 예:

```kotlin
val layoutMetrics = LocalMyBenefitLayoutMetrics.current
```

사용 예:

```kotlin
Arrangement.spacedBy(layoutMetrics.contentGap)
Modifier.padding(layoutMetrics.contentGap)
```

---
