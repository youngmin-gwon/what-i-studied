# Adaptive Navigation

상위 노트: [[adaptive-layout-and-navigation]]

Adaptive navigation은 window size와 posture에 따라 navigation UI를 바꾸는 것입니다.

공식 문서의 대표 API는 `NavigationSuiteScaffold`입니다.

기본 동작:

- compact width/height 또는 tabletop posture: navigation bar
- 그 외 큰 window: navigation rail
- 필요하면 expanded window에서 navigation drawer로 커스터마이즈 가능

사용 dependency:

```kotlin
implementation("androidx.compose.material3:material3-adaptive-navigation-suite")
```

공식 문서 예시는 enum 등으로 top-level destination을 정의하고, `NavigationSuiteScaffold`의 `navigationSuiteItems`에서 bar/rail/drawer item을 공통 선언하는 방식을 보여줍니다.

관련 문서:

- [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation)

---
