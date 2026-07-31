# Route Marker

현재는 다음 두 marker만 유지하는 것을 추천합니다.

```kotlin
interface AuthRoute : NavKey
interface MainFeatureTopLevelRoute : NavKey
```

`MainFeatureTopLevelRoute`는 로그인 필요 여부가 아니라 adaptive navigation item 여부를 의미합니다.

```text
MainFeatureTopLevelRoute
= phone에서는 bottom bar item
= tablet/foldable에서는 rail/drawer item
= 각 main feature의 root route
```

`ProtectedRoute`는 당장 도입하지 않는 편이 좋습니다. 현재 규칙이 "AuthRoute가 아니면 로그인 필요"라면 helper로 충분합니다.

```kotlin
fun requiresSignedIn(route: NavKey): Boolean {
    return route !is AuthRoute
}
```

나중에 로그인 없이 볼 수 있는 non-auth route가 생기면 `ProtectedRoute` 또는 `PublicRoute`를 도입합니다.

---
