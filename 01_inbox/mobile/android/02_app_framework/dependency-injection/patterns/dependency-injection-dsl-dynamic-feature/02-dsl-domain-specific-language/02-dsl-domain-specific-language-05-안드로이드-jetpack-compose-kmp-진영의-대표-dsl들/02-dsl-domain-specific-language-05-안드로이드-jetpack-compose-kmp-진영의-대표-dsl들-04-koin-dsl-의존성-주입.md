# Koin DSL (의존성 주입)

```kotlin
val appModule = module {
    single { RestaurantRepository() }        // Singleton 등록
    factory { RestaurantViewModel(get()) }   // 매번 새로 생성
}
```
