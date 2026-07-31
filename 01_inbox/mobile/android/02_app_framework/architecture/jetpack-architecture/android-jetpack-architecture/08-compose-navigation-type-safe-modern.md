# Compose Navigation (Type-safe / Modern ✅)

상위 노트: [android-jetpack-architecture](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture.md)

Android Gradle Plugin 8.2+ 및 Jetpack Navigation 2.8.0+ 부터는 Kotlin Serialization 을 활용한 **완전한 타입 안정성(Full Type-safety)**을 지원합니다.

```kotlin
// 1. Route 정의 (Serialization 필수)
@Serializable object Home
@Serializable data class Detail(val id: String)

// 2. NavHost 설정
val navController = rememberNavController()
NavHost(navController = navController, startDestination = Home) {
    composable<Home> {
        HomeScreen(onDetailClick = { id -> 
            navController.navigate(Detail(id)) 
        })
    }
    
    // 3. 타입 안정성이 보장된 인자 수집
    composable<Detail> { backStackEntry ->
        val detail: Detail = backStackEntry.toRoute<Detail>()
        DetailScreen(detail.id)
    }
}
```

>[!TIP] **왜 타입 안정성인가?**
 기존의 경로 문자열(`"detail/{id}"`) 방식은 오타에 취약하고 런타임 에러를 유발했습니다. Serialization 기반 방식은 컴파일 타임에 경로와 인자를 검증하므로 안전합니다.
```
