# Route Key 설계

상위 노트: [[jetpack-navigation-3-guide]]

Navigation 3의 route는 문자열 주소가 아니라 Kotlin 타입입니다. 이 프로젝트에서는 marker interface로 route의 의미를 구분하는 편이 좋습니다.

```kotlin
interface AuthRoute : NavKey
interface MainFeatureTopLevelRoute : NavKey

@Serializable
data object SignInRoute : AuthRoute

@Serializable
data object DashboardRoute : MainFeatureTopLevelRoute

@Serializable
data object TrainingRoute : MainFeatureTopLevelRoute

@Serializable
data class TrainingDetailRoute(
    val id: String,
) : NavKey
```

권장 기준:

- route key에는 화면을 복원하는 데 필요한 최소 식별자만 둡니다.
- 큰 객체, repository 객체, callback은 key에 넣지 않습니다.
- 로그인 필요 여부는 marker가 아니라 정책 함수로 시작해도 충분합니다.
- top-level destination 여부는 별도 marker로 분리합니다.

```kotlin
fun requiresSignedIn(route: NavKey): Boolean {
    return route !is AuthRoute
}
```

---
