# Deep Link

상위 노트: [jetpack-navigation-3-guide](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide.md)

Navigation 3에서는 deep link도 최종적으로 `NavKey`로 변환해야 합니다. Android OS가 앱을 여는 입구는 여전히 `Activity`이므로, `MainActivity`가 `intent.data`를 받고 app layer가 이를 route key로 파싱합니다.

```kotlin
fun Uri.toNavKeyOrNull(): NavKey? {
    return when {
        scheme == "https" &&
            host == "example.com" &&
            pathSegments.firstOrNull() == "training" -> {
            TrainingDetailRoute(id = pathSegments.getOrNull(1) ?: return null)
        }

        else -> null
    }
}
```

초기 진입:

```kotlin
val startRoute = intent?.data?.toNavKeyOrNull() ?: DashboardRoute

setContent {
    val backStack = rememberNavBackStack(startRoute)
    MyBenefitApp(backStack = backStack)
}
```

실무에서는 session 상태를 함께 고려합니다.

```text
Signed in deep link:
TrainingDetailRoute(id)
 -> selectedDestination = Training
 -> trainingBackStack = [TrainingRoute, TrainingDetailRoute(id)]

Signed out deep link:
TrainingDetailRoute(id)
 -> pendingRoute = TrainingDetailRoute(id)
 -> authBackStack = [SignInRoute]
 -> 로그인 성공 후 pendingRoute 적용
```

Deep link 설계 기준:

- URL parsing은 app layer에 둡니다.
- feature module은 자신이 받을 `NavKey`와 화면을 제공하고, 외부 URL 스키마는 몰라도 되게 합니다.
- path/query argument는 `NavKey` 생성 시 타입 변환을 끝냅니다.
- 잘못된 URL은 fallback route 또는 error route로 명시적으로 보냅니다.
- synthetic back stack은 자동으로 생기지 않습니다. 앱이 원하는 `[root, detail]` stack을 직접 만듭니다.

Manifest, intent filter, Android App Links 자체는 [intent-and-deep-link](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-and-deep-link.md)를 참조합니다.

---
