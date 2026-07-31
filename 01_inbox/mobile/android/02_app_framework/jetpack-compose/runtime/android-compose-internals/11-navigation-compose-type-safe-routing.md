# Navigation Compose (Type-Safe Routing)

상위 노트: [android-compose-internals](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals.md)

>[!WARNING] **Devil's Advocate : String Route 는 이제 그만**
>과거 Compose Navigation 은 `"detail/{id}"` 와 같은 String URL 기반 라우팅을 사용하여 오타에 취약하고 인수 전달이 불편했습니다.
>**Navigation 2.8+ 버전부터는 `kotlinx.serialization` 기반의 Type-Safe 라우팅으로 완전히 대체**되었습니다. String 기반 라우팅 코드를 발견하면 리팩토링 대상입니다.

```kotlin
// 1. Route 타겟을 Serializable 데이터 구조로 정의
@Serializable object Home
@Serializable data class Detail(val userId: String)

@Composable
fun AppNavigation() {
    val navController = rememberNavController()
    
    NavHost(navController = navController, startDestination = Home) {
        composable<Home> {
            HomeScreen(
                onNavigateToDetail = { id ->
                    navController.navigate(Detail(userId = id))
                }
            )
        }
        
        composable<Detail> { backStackEntry ->
            // 2. Type-safe하게 인자 추출
            val detail = backStackEntry.toRoute<Detail>()
            DetailScreen(userId = detail.userId)
        }
    }
}
```
